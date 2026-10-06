---
name: project-development
license: MIT
description: First integrate the current project conventions, architecture, workflow and available dependencies, then guide staged project development through issue analysis, framework and DB design, flows, interface contracts, acceptance scenarios, implementation planning, implementation and review. Use for explicit project-development workflows or their requested stages. Select only the requested stage; do not apply the entire process to routine small fixes or reviews.
---

# 專案開發流程集合

依使用者要完成的階段選擇細項流程，只讀取該階段需要的文件。這個 skill 是共同入口，細項持續分開維護。

## 中英文模式

英文 [SKILL.md](SKILL.md) 與 `references/` 是代理執行時的共同工作指令；本中文版與 `references/zh-TW/` 供閱讀及維護，不是第二個需要安裝的 skill。

- 預設輸出繁體中文（`zh-TW`），也可明確指定英文（`en`）。先採使用者本次明確選擇，其次沿用專案脈絡中的輸出偏好；沒有設定時使用繁體中文。
- 工作指令以英文撰寫，分析與核對依英文指令執行；不要求顯示內部思考，也不宣稱能控制或驗證模型內部思考的語言。交付具體結論、依據、假設與驗證結果。
- 所選語言適用於回覆、分析／設計／計畫文件、審查紀錄、圖表說明與 HTML 可見介面。程式識別字、API／DB 欄位、命令、路徑與來源引用保持原樣。
- 切換語言不另建同一需求的工作文件，也不自行翻譯既有全專案文件；只依要求改本次輸出或文件。
- 中文圖表使用 `assets/architecture-diagram.html`；英文圖表使用 `assets/architecture-diagram.en.html`。兩者沿用相同資料格式與互動行為。
- 中英文指引變動時同步更新；英文執行指令為維護主版，不以翻譯差異引入不同流程。

使用範例：「使用 project-development，輸出用繁體中文」；「Use project-development with English output」。

## 先整合專案特點與流程

首次進入專案，先依 [專案脈絡整合](references/zh-TW/project-context.md) 建立或更新本專案的脈絡文件：架構與模組特點、資料與介面慣例、需求／文件單位、開發與交付流程、驗證方式及工具依賴。後續各階段以該文件和原始來源為依據，沿用使用者的開發邏輯。

已有脈絡時只核對本次涉及的規則與變化，不重新盤點全專案。整合脈絡是閱讀及文件工作，不授權產品建構或對外操作；缺少不相關資料不阻擋當前階段。

## 階段與細項

| 階段 | 使用時機 | 細項流程 | 產出 |
|---|---|---|---|
| Issue／需求分析 | 讀取需求、釐清範圍、畫需求架構、實作前評估 | [issue-analysis](references/zh-TW/issue-analysis.md) | 依專案工作單位維護五項分析文件 |
| 專案雛形建構 | 熟悉專案、確認框架與 DB 欄位設計，或建立已確認的骨架 | [project-scaffold](references/zh-TW/project-scaffold.md) | 專案與逐表設計說明；要求建構時再產出骨架、設定、DB 變更檔及基本驗證 |
| 操作流程與資料流確認 | 理解操作如何串起需求、module 與 DB，或確認跨層流程 | [operation-flow](references/zh-TW/operation-flow.md) | 流程／時序圖、逐步讀寫說明、狀態與失敗分支、待確認事項 |
| 介面契約確認 | 確認跨 module 輸入、輸出、錯誤及前端 Props 對應 | [interface-contract](references/zh-TW/interface-contract.md) | 介面欄位與驗證規則、結果／錯誤契約、UI 資料對應及差異 |
| 業務規則與驗收情境確認 | 確認不同資料、操作及邊界情境的預期行為 | [business-acceptance](references/zh-TW/business-acceptance.md) | 有需求依據的具體驗收案例、預期資料變化與待確認問題 |
| 實作拆解與順序確認 | 將已確認的設計與驗收案例拆成可執行工作 | [implementation-plan](references/zh-TW/implementation-plan.md) | 現況缺口、工作項目、相依順序、完成條件及第一步 |
| 實作與驗證 | 使用者要求開始開發，完成授權範圍並核對驗收行為 | [implementation-validation](references/zh-TW/implementation-validation.md) | 實際程式改動、驗證結果、限制與剩餘工作 |
| 審查與交付確認 | 整理與雙重審查程式碼，再完善本次檔案與測試架構圖 | [review-delivery](references/zh-TW/review-delivery.md) | 程式碼整理、審查與驗證紀錄，完整實作流程與測試 HTML 圖 |

其他交付流程可在使用者確定需要後加入獨立細項，不建立空白流程或假定規則。

實作架構圖（含逐檔審查進度）一律從 [範本](assets/architecture-diagram.html) 建立，依 [實作架構圖 HTML](references/zh-TW/architecture-diagram.md) 填寫。

重複盤點與文件核對優先使用 [可執行的流程核對](references/zh-TW/automation.md)：變更清單、架構檔案涵蓋比對、架構圖結構及本機連結檢查。只在需要此類工作時讀取；腳本結果不能取代需求或程式語意審查。

## 選擇與銜接

- 使用者只要求分析時，執行 issue-analysis；只要求建構時，執行 project-scaffold，先確認已有需求與架構依據。
- 使用者授權跨階段工作時，依實際需要銜接；上一階段完成不代表自動獲得下一階段的執行授權。
- 使用者正在理解專案或確認設計時，停留在說明與方案階段；不得把討論或試看流程解讀為實際建構授權。
- 會改變框架、核心資料模型、權限或寫入方式的未解需求，阻擋相依建構；不阻擋其他可獨立完成的工作。
- 既有專案沿用既有框架與升級機制，新專案才評估框架選擇。不因選擇此 skill 就重建專案、增加新表或擴大 scope。
- 需求與工作文件單位依專案脈絡；Forge 採一個 issue 一份文件，後續結果更新原文件。各細項的「issue 文件」指本專案選定的工作文件，不強迫其他專案採相同平台、編號或目錄。
- 讀取目前階段需要的段落與相依設計；已確認且未變動的內容沿用，不要求每一階段重新分析完整 issue 或建立所有前置文件。
- 在原 issue 文件維持需求 → 設計／工作項目 → 實作位置 → 驗收案例／結果的對應，可用小表或既有標題引用。每項本期需求有落點，每項改動有需求或必要技術依據；發現遺漏或超出範圍時記錄並處理，不擅自擴大需求。
- 共通檢查以細項中的原規則為準，其他階段引用而不複製；更新 skill 時核對階段責任、授權邊界與連結一致。設計確認、程式已寫、測試通過與可發布是不同狀態。

呼叫範例：使用 project-development 的 issue-analysis 分析 #92；使用 project-development 的 project-scaffold 建立已確認需求所需的模組與 DB 變更檔。

Skill 自己的檔案、腳本、範本都從實際載入的 skill 目錄定位，不假定安裝在 `.claude/skills`。發行與情境驗證方式見 [README](README.md)。
