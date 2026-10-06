"""Exercise bookkeeping in isolated repositories; never touch the product DB."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('workflow_check', Path(__file__).with_name('workflow_check.py'))
workflow = importlib.util.module_from_spec(spec)
spec.loader.exec_module(workflow)


class WorkflowChecks(unittest.TestCase):
    def test_changes_include_all_layers_and_rename(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)

            def git(*args):
                return subprocess.check_output(['git', '-C', directory, *args], stderr=subprocess.PIPE)

            git('init')
            for name in ('old name.txt', 'gone.txt', 'staged.txt', 'unstaged.txt'):
                (repo / name).write_text(name, encoding='utf-8')
            git('add', '.')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-m', 'base')
            base = git('rev-parse', 'HEAD').decode().strip()
            git('mv', 'old name.txt', 'new name.txt')
            git('rm', 'gone.txt')
            git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-m', 'rename and delete')
            (repo / 'staged.txt').write_text('changed', encoding='utf-8')
            git('add', 'staged.txt')
            (repo / 'unstaged.txt').write_text('changed', encoding='utf-8')
            (repo / '中文 file.txt').write_text('new', encoding='utf-8')
            report = workflow.inventory(repo, base, [])
            entries = {(item['source'], item['path']): item for item in report['changes']}
            self.assertEqual(entries['committed', 'new name.txt']['old_path'], 'old name.txt')
            self.assertEqual(entries['committed', 'gone.txt']['status'], 'D')
            self.assertIn(('staged', 'staged.txt'), entries)
            self.assertIn(('unstaged', 'unstaged.txt'), entries)
            self.assertIn(('untracked', '中文 file.txt'), entries)
            excluded = workflow.inventory(repo, base, ['staged.txt', 'absent.txt'])
            self.assertEqual(excluded['unused_exclusions'], ['absent.txt'])
            self.assertEqual(excluded['excluded'][0]['path'], 'staged.txt')
            with self.assertRaises(subprocess.CalledProcessError):
                workflow.inventory(repo, 'nonexistent-ref', [])

    def test_links_and_examples(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '存在 file.md').write_text('# Section', encoding='utf-8')
            (root / 'SKILL.md').write_text(
                '[ok](<存在 file.md#Section>) [bad](missing.md) [web](https://example.invalid)\n'
                '```md\n[example](not-a-real-link.md)\n```', encoding='utf-8')
            report = workflow.check_links(root)
            self.assertEqual(report['checked'], 2)
            self.assertEqual(report['missing'], [{'file': 'SKILL.md', 'target': 'missing.md'}])

    def test_coverage_requires_old_and_new_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            html = Path(directory) / 'architecture.html'
            report = {'changes': [{'path': 'new.py', 'old_path': 'old.py'}, {'path': 'test.py'}]}
            html.write_text('<li data-file="new.py">new</li><li data-file="old.py">removed</li>', encoding='utf-8')
            self.assertEqual(workflow.coverage(report, html)['missing'], ['test.py'])
            html.write_text(html.read_text() + '<li data-file="test.py">test</li>', encoding='utf-8')
            self.assertEqual(workflow.coverage(report, html)['missing'], [])
            html.write_text(html.read_text() + '<li data-file="test.py">duplicate</li>', encoding='utf-8')
            self.assertEqual(workflow.coverage(report, html)['duplicates'], ['test.py'])

    def test_coverage_reads_node_files_and_allows_one_file_in_several_boxes(self):
        with tempfile.TemporaryDirectory() as directory:
            html = Path(directory) / 'architecture.html'
            report = {'changes': [{'path': 'service.py'}, {'path': 'notes.md'}]}
            html.write_text('<script type="application/json" id="details">'
                            '{"a": {"files": ["service.py"]}, "b": {"files": ["service.py"]}}</script>'
                            '<li data-file="notes.md">not drawn</li>', encoding='utf-8')
            result = workflow.coverage(report, html)
            self.assertEqual((result['missing'], result['duplicates']), ([], []))

    def test_the_template_passes_and_a_broken_copy_does_not(self):
        template = Path(__file__).resolve().parent.parent / 'assets' / 'architecture-diagram.html'
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            details = workflow.read_page(template).blocks['details']
            paths = workflow.node_files(json.loads(details)) | set(workflow.read_page(template).paths)
            for path in paths:
                (repo / path).parent.mkdir(parents=True, exist_ok=True)
                (repo / path).write_text('', encoding='utf-8')
            report = workflow.check_diagram(template, repo)
            self.assertEqual(report['problems'], [])
            self.assertEqual(report['todo'], ['notifier'])
            broken = repo / 'broken.html'
            broken.write_text(template.read_text(encoding='utf-8')
                              .replace('    class mail ext\n', '')
                              .replace('t_repo -. tests .-> repo', 't_repo -. tests --> nowhere'),
                              encoding='utf-8')
            problems = workflow.check_diagram(broken, repo)['problems']
            self.assertTrue(any('node mail' in p for p in problems), problems)
            self.assertTrue(any('nowhere' in p for p in problems), problems)
            self.assertTrue(any('-. text -->' in p for p in problems), problems)


if __name__ == '__main__':
    unittest.main()
