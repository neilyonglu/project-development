# project-development

沿用作者的開發邏輯：先整合當前專案特點、流程與可用依賴，再按需求進行分析、設計、拆解、實作、驗證與雙重審查。提供需求到實作／驗收的追溯，以及可編輯的 HTML 架構與測試視圖。

[English](README.md) | 繁體中文

## 語言模式

代理使用英文 `SKILL.md` 與英文階段指引；[中文版流程](SKILL.zh-TW.md) 與 `references/zh-TW/` 供閱讀維護。兩種輸出模式共用同一份 skill，不需要重複安裝。

預設 `output_language: zh-TW`，明確指定英文則用 `en`。本次使用者選擇優先於專案偏好，專案偏好優先於預設；已選模式沿用到後續工作，直到使用者更改。中英文都由英文工作指令引導，不能保證模型內部思考的語言，也不要求輸出內部思考。

- 中文：「使用 project-development，先整合此專案脈絡，輸出用繁體中文。」
- 英文：「Use project-development. Integrate this project's context first and produce all deliverables in English.」
- 切換：「接下來改用英文輸出，沿用目前工作文件。」

語言涵蓋回覆、工作文件、審查與圖表說明。程式名稱、API／DB 欄位、命令、路徑與原文引用保持原樣；既有專案文件不因切換而全部翻譯。

## 安裝與使用

將整個 `project-development/` 目錄放入目標代理支援的 skills 目錄，保留 SKILL.md、references、scripts、assets。Claude Code 的專案安裝位置可用 `.claude/skills/project-development/`；其他代理使用各自支援的目錄與呼叫語法。移除時只移除已安裝的 skill 目錄，保留專案工作文件與脈絡。

例如：「使用 project-development，先整合此專案的特點與流程，再分析這份需求」；「使用 project-development，依已確認的計畫完成實作與驗證」。只要求某階段就只做該階段；脈絡已建立時沿用並核對相關變動。

專案脈絡與工作文件留在各自 repository，公開發行包不包含真實專案資料、私人 issue 或憑證。發布只打包此目錄，排除 `__pycache__`、`*.pyc` 與本機暫存。此修改不代表已發布、安裝至其他代理或完成跨代理驗證。

## 相依與替代

- 指引本身需要能讀取專案檔案的開發代理；產品 runtime、資料庫與建置依賴由專案脈絡決定。
- 核對腳本使用 Python 3.9+ 標準庫與 Git。腳本路徑從實際 skill 目錄取得；詳細操作見 [automation](references/zh-TW/automation.md)。
- `/code-review`、`/ponytail-review` 適用且可用時優先使用，否則執行內建兩輪審查，不自行安裝。
- HTML 範本從 CDN 載入 Mermaid／ELK，需要網路與瀏覽器；沒有渲染能力時明示未驗證，不影響可獨立完成的分析與結構核對。

## 驗證方式

先執行腳本的 links 檢查及 `scripts/test_workflow_check.py`；前者只核對本機檔案連結，後者在臨時 repository 測試盤點／圖結構，不操作產品 DB。

實際代理情境另按下表評估，記錄代理／版本、輸入、專案 fixture、產物、實際異動與判定；下列是評估案例，不代表已實跑。使用臨時專案與假 issue，不連正式系統。

| 情境 | 應觀察的結果 |
|---|---|
| Forge 類型、只要求分析 | 整合 Domo／GitLab／文件慣例，產出五項分析，不修改產品或操作 DB |
| 不同技術、沒有 issue | 由實際專案建立脈絡，不套入 Domo／GitLab、不虛構 issue |
| 已有脈絡與部分設計、授權實作 | 只核對相關變動與必要缺口，延續原工作文件，不重建全套前置文件 |
| 缺少兩個審查 skills | 完成正確性與簡化兩輪本機審查，記錄實際方式 |
| 規範與 manifest 矛盾、需求缺漏 | 保留來源與未解問題，只阻擋相依工作，不猜業務政策 |
| 中文／英文模式及中途切換 | 回覆、文件與圖表使用所選語言，沿用同一份工作文件，技術識別字保持原樣 |
| 已有使用者異動、缺少 DB 或瀏覽器 | 保留無關修改，明示未驗證範圍，不把 mock／結構檢查當成實際驗證 |

## 參考與授權

設計參考（未複製其程式或完整指令）：[Superpowers](https://github.com/obra/superpowers) 的驗證證據與流程分級、[Spec Kit](https://github.com/github/spec-kit) 的技術脈絡與複雜度理由、[create-feature](https://github.com/garethrhughes/skills/blob/main/create-feature/SKILL.md) 的共通／專案規則分層與審查交接。

本 skill 使用 [MIT License](LICENSE)。首次發行可用 Git tag `v0.1.0`；公開 repository 位址尚未設定，不提供虛構安裝 URL。
