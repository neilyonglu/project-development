# 可執行的流程核對

本文件為中文閱讀版；代理執行時使用上層英文同名指引。輸出語言依英文入口的設定，中文模式使用繁體中文，技術識別字保持原樣。

`<skill-dir>` 是本次實際載入的 skill 絕對目錄；將範例替換為真實路徑。產品路徑相對於 repository root，skill 資源相對於 skill 目錄，不假定 Claude 專用安裝路徑。需要 Python 3.9+ 與 Git；先核對現有 runtime。

`scripts/workflow_check.py` 使用 Python 標準函式庫與本機 Git，不讀產品檔案內容或完整 diff、不 fetch、不修改 Git／DB、不呼叫模型。只有 inventory 的 `--output` 會寫入指定 JSON。在 repository root 執行；使用現有 Python 環境，不為此安裝額外套件。

## 1. 變更清單

```text
python "<skill-dir>/scripts/workflow_check.py" inventory --base <已確認的commit或ref> --output <暫存目錄的changes.json>
```

先確認比較基準；腳本比較 `base..HEAD`，另列 staged、unstaged、未被 Git 忽略的 untracked 檔案。不自動猜 main 或 merge-base，包含新增／刪除／重新命名的舊與新路徑，保留各層來源而不誤當單一最終狀態。輸出放在 repository 外的暫存位置，避免下一次盤點把輸出自身列入。

用重複的 `--exclude <repo相對完整路徑>` 排除已確認無關異動；排除紀錄保留在 JSON，未知排除路徑會回報，不自動猜 issue 範圍。忽略的檔案不包含在清單；submodule 只列根 repository 的變更，若本期修改 submodule，需在其 repository 另跑並核對。

## 2. 架構檔案涵蓋比對

依 [實作架構圖 HTML](architecture-diagram.md) 建立的頁面，節點的 `files` 會被讀取，同一檔案可出現在多個節點；沒畫成節點的檔案放在可見清單，每項用 `data-file` 標記 repository 相對路徑，文字指向對應節點、配套說明或刪除／替代說明。例如：

```html
<li data-file="src/service.py">service 節點：處理請求</li>
<li data-file="tests/test_service.py">測試節點：驗證錯誤回應</li>
```

```text
python "<skill-dir>/scripts/workflow_check.py" coverage --inventory <changes.json> --html <architecture.html>
```

檢查所有清單路徑是否宣告，包含 renamed 的舊路徑，回報缺漏與重複；額外路徑可能是沿用依賴，交由 agent 核對。比對前更新 inventory，避免漏掉後續修正。這只證明檔案清單有對應宣告，**不證明**節點、箭頭、測試目標正確或 HTML 能渲染，仍按架構審查規則核對。

## 3. 架構圖結構

```text
python "<skill-dir>/scripts/workflow_check.py" diagram --html <architecture.html>
```

檢查依範本建立的頁面：`src`／`details`／`parts` 區塊存在；每個節點恰有一個合法 class 與含 `meaning` 的 details；測試節點與 `t_` 開頭一致；箭頭兩端都是已宣告的節點；Part 標記有對應分頁；虛線箭頭寫法；`files` 與 `data-file` 路徑存在（相對於 `--repo`，預設目前目錄）。輸出 `todo` 列出仍是虛線的節點，即尚待審查的檔案。只檢查結構，不判斷箭頭是否符合實際呼叫，也不渲染頁面。

## 4. Skill 內部檔案連結

```text
python "<skill-dir>/scripts/workflow_check.py" links
```

預設檢查此 skill 的 Markdown inline 本機檔案連結，略過 fenced code examples、外部 URL 與純錨點；不檢查標題錨點、reference-style links 或遠端可存取性。需要核對其他文件時可指定 `--root <目錄>`，限制掃描範圍，不預設掃整個 repository。

## 執行與判讀

退出碼 `0` 表示本項機械檢查無缺漏，`1` 表示有缺漏／重複／未匹配排除，`2` 表示執行錯誤。腳本與 skill 規則更新後，可用臨時 repository 的自測驗證：

```text
python "<skill-dir>/scripts/test_workflow_check.py"
```

先使用結構化輸出定位問題，再只讀必要檔案。需求是否成立、參數是否有業務用途、命名是否清楚、呼叫／資料流及測試有效性不能由此腳本判定；現有 lint／typecheck／build 依實作與驗證規則使用，不另建通用測試執行器。
