"""Read-only workflow bookkeeping; Python standard library and Git only."""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)


def diff_files(repo: Path, source: str, *args: str) -> list[dict]:
    fields = git(repo, 'diff', '--name-status', '-z', '--find-renames', *args, '--').decode('utf-8', 'surrogateescape').split('\0')
    result = []
    i = 0
    while i < len(fields) and fields[i]:
        status, path = fields[i:i + 2]
        i += 2
        item = {'source': source, 'status': status, 'path': path}
        if status.startswith(('R', 'C')):
            item['old_path'] = path
            item['path'] = fields[i]
            i += 1
        result.append(item)
    return result


def inventory(repo: Path, base: str, excluded: list[str]) -> dict:
    repo = Path(git(repo, 'rev-parse', '--show-toplevel').decode().strip())
    base_sha = git(repo, 'rev-parse', '--verify', base + '^{commit}').decode().strip()
    head = git(repo, 'rev-parse', 'HEAD').decode().strip()
    changes = diff_files(repo, 'committed', base_sha, 'HEAD')
    changes += diff_files(repo, 'staged', '--cached')
    changes += diff_files(repo, 'unstaged')
    changes += [{'source': 'untracked', 'status': '?', 'path': p}
                for p in git(repo, 'ls-files', '--others', '--exclude-standard', '-z').decode('utf-8', 'surrogateescape').split('\0') if p]
    exclusion_set = set(excluded)
    ignored = [item for item in changes if item['path'] in exclusion_set or item.get('old_path') in exclusion_set]
    changes = [item for item in changes if item not in ignored]
    return {'repo': str(repo), 'base': base_sha, 'head': head,
            'comparison': 'base..HEAD plus staged, unstaged and untracked; no fetch or automatic merge-base',
            'changes': changes, 'excluded': ignored,
            'unused_exclusions': sorted(exclusion_set - {p for item in ignored for p in (item['path'], item.get('old_path')) if p})}


def check_links(root: Path) -> dict:
    """Check inline Markdown local file targets, not anchors or remote URLs."""
    if not root.is_dir():
        raise ValueError(f'Not a directory: {root}')
    issues = []
    checked = 0
    for doc in sorted(root.rglob('*.md')):
        content = doc.read_text(encoding='utf-8-sig')
        # Code examples do not declare document links.
        content = re.sub(r'```.*?```|~~~.*?~~~', '', content, flags=re.S)
        for match in re.finditer(r'\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', content):
            target = match.group(1).strip('<>')
            if target.startswith('#') or urlsplit(target).scheme:
                continue
            local = unquote(target.split('#', 1)[0].split('?', 1)[0])
            if not local:
                continue
            checked += 1
            if not (doc.parent / local).exists():
                issues.append({'file': str(doc.relative_to(root)), 'target': target})
    return {'checked': checked, 'missing': issues,
            'limits': 'Inline Markdown local file links only; anchors, reference-style links and remote URLs are not checked.'}


class FileMarkers(HTMLParser):
    """`data-file` attributes, plus the text of the page's `<script id=...>` data blocks."""

    def __init__(self):
        super().__init__()
        self.paths: list[str] = []
        self.blocks: dict[str, str] = {}
        self._block: str | None = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == 'script' and attributes.get('id'):
            self._block = attributes['id']
            self.blocks[self._block] = ''
        for key, value in attrs:
            if key == 'data-file' and value:
                self.paths.append(value)

    def handle_data(self, data):
        if self._block is not None:
            self.blocks[self._block] += data

    def handle_endtag(self, tag):
        if tag == 'script':
            self._block = None


def read_page(html: Path) -> FileMarkers:
    parser = FileMarkers()
    parser.feed(html.read_text(encoding='utf-8-sig'))
    return parser


def node_files(details: dict) -> set[str]:
    """Every path a diagram node declares; one file may be drawn as several boxes."""
    return {path for entry in details.values() for path in entry.get('files', [])}


def coverage(report: dict, html: Path) -> dict:
    page = read_page(html)
    expected = {p for item in report['changes'] for p in (item['path'], item.get('old_path')) if p}
    details = json.loads(page.blocks['details']) if 'details' in page.blocks else {}
    declared = set(page.paths) | node_files(details)
    return {'expected_count': len(expected), 'declared_count': len(declared),
            'missing': sorted(expected - declared), 'extra': sorted(declared - expected),
            'duplicates': sorted(p for p, count in Counter(page.paths).items() if count > 1),
            'limits': 'Checks data-file and node "files" declarations only, not diagram edges, node correctness, test coverage or rendering. Extra paths may be reused dependencies.'}


NODE_CLASSES = {'seen', 'todo', 'test', 'data', 'datatodo', 'ext'}
NODE_LINE = re.compile(r'^\s*(\w+)\s*[\[\(\{]')
ARROW = re.compile(r'-->|==>|\.->|\.-|---')


def check_diagram(html: Path, repo: Path) -> dict:
    """Structure of an architecture page built from the skill's template."""
    page = read_page(html)
    problems: list[str] = []
    for block in ('src', 'details', 'parts'):
        if block not in page.blocks:
            problems.append(f'missing <script id="{block}"> block')
    if problems:
        return {'problems': problems, 'todo': []}
    details = json.loads(page.blocks['details'])
    parts = json.loads(page.blocks['parts'])
    nodes: list[str] = []
    classes: dict[str, list[str]] = {}
    edges: list[tuple[str, str]] = []
    for number, raw in enumerate(page.blocks['src'].split('\n'), start=1):
        tag = re.match(r'^(\d+)\|(.*)$', raw)
        line = tag.group(2) if tag else raw
        stripped = line.strip()
        if tag and not 1 <= int(tag.group(1)) < max(len(parts), 2):
            problems.append(f'line {number}: part tag {tag.group(1)} has no tab in "parts"')
        if not stripped or stripped.startswith(('%%', 'flowchart', 'graph', 'classDef', 'style', 'linkStyle', 'direction')):
            continue
        if stripped.startswith('class '):
            ids, name = stripped.split()[1:3]
            for node in ids.split(','):
                classes.setdefault(node, []).append(name)
            continue
        if stripped.startswith('subgraph') or stripped == 'end':
            if not tag:
                problems.append(f'line {number}: "{stripped[:30]}" needs a part tag')
            continue
        node = NODE_LINE.match(line)
        if node and not ARROW.search(line):
            nodes.append(node.group(1))
            if not tag:
                problems.append(f'line {number}: node {node.group(1)} needs a part tag')
            continue
        if ARROW.search(line):
            words = stripped.split()
            edges.append((words[0], words[-1]))
            if re.search(r'-\.\s[^.]*-->', line):
                problems.append(f'line {number}: dotted arrow written "-. text -->"; use "-. text .->"')
    node_set = set(nodes)
    for node in nodes:
        names = [name for name in classes.get(node, []) if name in NODE_CLASSES]
        if len(names) != 1:
            problems.append(f'node {node}: needs exactly one of {sorted(NODE_CLASSES)}, has {names}')
        elif (names[0] == 'test') != node.startswith('t_'):
            problems.append(f'node {node}: test nodes, and only test nodes, start with t_')
        entry = details.get(node)
        if not entry or not entry.get('meaning'):
            problems.append(f'node {node}: no details entry with a "meaning"')
            continue
        for path in entry.get('files', []):
            if not (repo / path).exists():
                problems.append(f'node {node}: file {path} does not exist')
    problems += [f'details {key}: no node with that id' for key in sorted(set(details) - node_set)]
    problems += [f'class line names unknown node {key}' for key in sorted(set(classes) - node_set)]
    problems += [f'edge {a} -> {b}: unknown node' for a, b in edges if a not in node_set or b not in node_set]
    for marker in page.paths:
        if not (repo / marker).exists():
            problems.append(f'data-file {marker} does not exist')
    todo = sorted(node for node in nodes if set(classes.get(node, [])) & {'todo', 'datatodo'})
    return {'nodes': len(nodes), 'edges': len(edges), 'parts': len(parts), 'todo': todo, 'problems': problems,
            'limits': 'Structure only: it cannot tell whether an arrow matches the real call, or render the page.'}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    inv = sub.add_parser('inventory', help='List changes without reading file contents')
    inv.add_argument('--repo', type=Path, default=Path.cwd())
    inv.add_argument('--base', required=True, help='Explicit comparison commit/ref; use --base=REF for unusual refs')
    inv.add_argument('--exclude', action='append', default=[], help='Exact repository-relative path; repeat as needed')
    inv.add_argument('--output', type=Path, help='Write UTF-8 JSON instead of printing the inventory')
    links = sub.add_parser('links', help='Check local Markdown file links')
    links.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    cov = sub.add_parser('coverage', help='Compare inventory with HTML data-file markers')
    cov.add_argument('--inventory', type=Path, required=True)
    cov.add_argument('--html', type=Path, required=True)
    dia = sub.add_parser('diagram', help='Check an architecture page built from the template')
    dia.add_argument('--html', type=Path, required=True)
    dia.add_argument('--repo', type=Path, default=Path.cwd(), help='Root that node "files" are relative to')
    args = parser.parse_args()
    try:
        if args.command == 'inventory':
            result = inventory(args.repo, args.base, args.exclude)
            failed = bool(result['unused_exclusions'])
        elif args.command == 'links':
            result = check_links(args.root)
            failed = bool(result['missing'])
        elif args.command == 'diagram':
            result = check_diagram(args.html, args.repo)
            failed = bool(result['problems'])
        else:
            result = coverage(json.loads(args.inventory.read_text(encoding='utf-8-sig')), args.html)
            failed = bool(result['missing'] or result['duplicates'])
        encoded = json.dumps(result, ensure_ascii=True, indent=2)
        if args.command == 'inventory' and args.output:
            args.output.write_text(encoded + '\n', encoding='utf-8')
            print(json.dumps({'output': str(args.output), 'changes': len(result['changes']),
                              'excluded': len(result['excluded']), 'unused_exclusions': result['unused_exclusions']}))
        else:
            print(encoded)
        return int(failed)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=True))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
