# 實作架構圖 HTML

本文件為中文閱讀版；代理執行時使用上層英文同名指引。輸出語言依英文入口的設定，中文模式使用繁體中文，技術識別字保持原樣。

[審查與交付確認](review-delivery.md) 第二步的架構圖，以及逐檔審查時用來追進度的同一張圖，都從 [範本](../../assets/architecture-diagram.html) 開始。複製範本到 issue 文件旁，例如 `docs/development/issue-<n>-architecture.html`。版面、圖例、Part 分頁、測試開關、縮放、hover 說明與點擊卡片都已在範本內，不另寫 CSS／JS；只填下列資料區塊。

中文模式使用原中文範本；英文模式使用 [英文範本](../../assets/architecture-diagram.en.html)，設 `lang="en"`。可見文字、meaning、detail、funcs、Part 與連線說明使用所選語言；不改資料 key、節點 ID 或路徑。英文的第 0 個 tab 為 `All`，中文為「全部」；styles 的全形分隔符 `：` 維持原樣。

## 資料區塊

| 區塊 | 內容 |
|---|---|
| `<title>`、`<h1>` | `#<issue> 架構圖` |
| `<script type="text/plain" id="src">` | Mermaid `flowchart TD` 原始碼；`classDef` 照範本保留 |
| `<script type="application/json" id="details">` | 每個節點的說明，key 是節點 id |
| `<script type="application/json" id="parts">` | Part 分頁 |
| 「沒畫進圖的檔案」清單 | 每個變更檔案若不畫成節點：`<li data-file="repo 相對路徑"><code>路徑</code>原因</li>` |

範本內的訂單範例只示範寫法，全部換成本次內容；不保留範例節點。

## src：節點

- 由上到下分層：`L1 Frontend` → `L2` 後端 → `L3` 服務 → `L4` 資料庫，依專案實際結構命名；層內再分組，例如入口、頁面、共用元件、`Definitions`（純資料）、`Config`、`Outbound`／`Inbound`。
- 一個方框 = 一個真實檔案，或檔案內的一個 endpoint。不畫概念框；多個檔案共用的方法畫成各檔案上的箭頭。一個檔案拆成多個方框時，用以檔名命名的 subgraph 包起來，讓每個檔案都能在圖上用名字找到。
- 標籤寫檔名或類別名；細節放 details，方框只放名字。技術名詞用英文，和程式一致；連接說明可用中文。

| 種類 | 寫法 | class |
|---|---|---|
| 程式檔，已看過 | `id[Name.java]` | `seen` |
| 程式檔，還沒看 | `id[Name.java]` | `todo` |
| 純資料／設定／型別／路由表（本身不做事） | `id[/AgentTypes.ts/]` | `data`（還沒看：`datatodo`） |
| DB table | `db_id[(table)]` | `seen` |
| 外部服務 | `id[外部 LLM API]` | `ext` |
| 測試檔 | `t_id([test_x.py])` | `test` |

- 每個節點恰好出現在一行 `class` 中，用上表其中一個 class。測試節點、且只有測試節點的 id 以 `t_` 開頭：關掉「顯示測試」時，含 `t_` 的行整行移除。
- `fresh`（紫色粗框，這個 Part 新加的）由頁面依 Part 標記自動加上，不手寫。
- `.scss` 不畫方框，列在用到它的 tsx 方框的 `styles` 與 `files`。只包一層、沒有資料流的小 UI 元件可不畫，放進「沒畫進圖的檔案」並寫原因。

## src：箭頭

- `a -- 送什麼 → 拿回什麼 --> b`：呼叫或讀寫，label 寫資料（欄位、物件），不寫函式名。
- `a == 送什麼 ==> b`：跨層呼叫（前端 → 後端、後端 → 服務）。
- `a -. 結果 .-> b`：回傳結果、只讀定義檔、callback。虛線一定寫成 `-. 文字 .->`；`-. 文字 -->` 會被 Mermaid 誤判。
- 同一個來源依序做的步驟，label 以 ①②③ 開頭（編號只在同一來源內有效），不讓依序看起來像平行。
- 測試：`t_id -. tests 什麼 .-> 受測節點`。
- label 內避免 `( ) [ ] { } " =`，Mermaid 可能誤解析。

## src：Part 標記

- 一個 issue 拆成多個疊在一起的 branch 時，每個 Part 對應一個 branch，依合併順序編號。
- node、`subgraph`、`end` 行開頭加 `N|`（N = 第一次出現的 Part）；箭頭與 `class` 行不加，兩端節點都畫出來時才畫。
- Part N 分頁畫出 1..N；N > 1 時，第 N 個 Part 新加的節點加紫框，整個新 subgraph 只框外框。
- 只有一個 branch 時全部標 `1|`，`parts` 只放「全部」與 Part 1。

## details

```json
"repo": {
 "meaning": "一句白話中文：這個檔案在業務上做什麼",
 "detail": "技術重點，多行用 \n 分隔",
 "funcs": [["insert", "一句白話：這個函式做什麼"]],
 "styles": ["OrderForm.module.scss：放什麼樣式"],
 "files": ["api/order_repo.py"]
}
```

- 每個節點都要有 `meaning`；hover 顯示 `meaning` 與 `detail`，點擊卡片列出 `files`、`funcs`、`styles`。
- `funcs`：程式檔列每個函式；main 上已存在的檔案只列本次改到的。測試節點列每個 test 檢查什麼。資料、DB、endpoint 可省略。
- `files`：repo 相對路徑；同一檔案可出現在多個方框（例如同一 service 的多個 endpoint）。樣式檔、`__init__.py` 等附屬檔列在所屬方框。coverage 檢查讀這裡與 `data-file`。
- 既有 DB table、外部服務沒有對應檔案時可省略 `files`。

## parts

```json
[{"tab": "全部", "note": "完整架構圖：所有 part 合起來，不標新加的部分。"},
 {"tab": "Part 1 · #101", "note": "branch …：這一層加了什麼"}]
```

第 0 個固定是「全部」。`note` 用一兩句說這個 branch 加了什麼。

## 審查進度

- 逐檔走讀時，使用者看過的檔案從 `todo` 改成 `seen`（`datatodo` → `data`）。實線代表使用者看過；不因後面的 branch 又改了該檔而改回虛線。
- 只有使用者實際看過才改實線；只是被問到、尚未打開的檔案維持虛線。
- 換到下一個 branch 時，把該 branch diff 中還不在圖上的檔案補成 `todo`；補完後，虛線方框就是這一層還要看的清單。
- 程式改動會改變圖上行為時（新的狀態、箭頭、計數），同一次改動一起更新圖，包含 details 的 `funcs` 與測試清單。

## 檢查

每次改圖後執行，詳見 [可執行的流程核對](automation.md)：

```text
python "<skill-dir>/scripts/workflow_check.py" diagram --html <architecture.html>
python "<skill-dir>/scripts/workflow_check.py" inventory --base <base> --output <暫存目錄的changes.json>
python "<skill-dir>/scripts/workflow_check.py" coverage --inventory <changes.json> --html <architecture.html>
```

`diagram` 檢查結構並列出仍是虛線的節點；`coverage` 檢查每個變更檔案都在 `files` 或 `data-file` 中。兩者都不能判斷箭頭是否符合實際呼叫，仍需人工核對。

頁面從 jsDelivr 載入 Mermaid 11 與 ELK 版面，需要網路。使用現有瀏覽器或可用的瀏覽器自動化能力開啟 HTML，核對主圖、Part、測試切換、縮放與錯誤提示；取得真正渲染的 SVG 節點數，與 `diagram` 回報的 `nodes` 比較。不可把 HTML 結構檢查當成渲染驗證。

需要 headless CLI 時先定位實際瀏覽器執行檔，不固定作業系統或 Chrome 安裝路徑。沒有網路或瀏覽器時保留 Mermaid 原始碼與結構檢查結果，在交付紀錄明確寫出渲染及互動未驗證；不為檢查而自行安裝瀏覽器。
