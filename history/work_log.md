# Work Log / Commit History

## [v2.1.9] - 2026-08-19 (Avatar Fits Full Square Frame & Timeline Typo Fix)
- `static/css/style.css`: 將 `.avatar-wrapper` 與照片完全調整為 100% 填滿外部 320x380px 的毛玻璃方框卡片，取消 160px 圓形限制。
- `templates/index.html`: 修正經歷時間軸第三項 `timeline-item lef` 之拼寫為 `timeline-item left`。

## [v2.1.8] - 2026-08-19 (Uniform Skill Category Card Heights)
- `static/css/style.css`: 為 `.skill-category` 設定 `min-height: 340px;` 與 `align-items: stretch;`，使所有技能卡片（包含只有 2 個選項的 Database Management 與 AI 區塊）的外框高度與 4 個選項的卡片完全對齊一致。

## [v2.1.7] - 2026-08-19 (Skill Tags Vertical List Layout)
- `static/css/style.css`: 將專業技能 (Skills) 區塊中的 `.skill-tags` 改為垂直單列排列 (`flex-direction: column; gap: 10px;`)，每個技能選項各自換行並呈現 100% 條列式卡片。
- `templates/index.html`: 優化技能項目內圖示與文字間的間距。

## [v2.1.6] - 2026-08-19 (Personal Details Vertical Layout)
- `static/css/style.css`: 將「關於我」底部的個人資訊條目（所在地、主要領域、電子信箱）恢復為原先的逐行單列垂直排列 (`flex-direction: column; gap: 12px;`)。

## [v2.1.5] - 2026-08-19 (About Me Glass-Card Full Width Expansion)
- `static/css/style.css`: 將「關於我 (About Me)」的 `.about-grid` 與 `.about-text.glass-card` 改為單欄置中並放大擴展至容器適當寬度 (`max-width: 1000px`)，個人資訊條目改為自適應雙欄網格排版，下方的技能與經歷等區塊保持原樣不受影響。

## [v2.1.4] - 2026-08-19 (Fix CSS Linter Warnings for background-clip)
- `static/css/style.css`: 於 `.text-gradient` 與 `.stat-number` 加入標準屬性 `background-clip: text;` 與 `color: transparent;`，消除編輯器黃色波浪警告線 (Linter Warning)。

## [v2.1.3] - 2026-08-19 (Allow Floating Badges to Overflow Card Frame)
- `static/css/style.css`: 將 `.avatar-card` 設為 `overflow: visible;`，並將照片裁剪隔離至 `.avatar-wrapper` 內部，讓左右兩側的浮動徽章 (`.badge-1` 和 `.badge-2`) 可以完整凸出超出卡片邊界 (`left: -35px`, `right: -35px`) 呈現立體層次感，並加上 `white-space: nowrap` 防止折行。

## [v2.1.2] - 2026-08-19 (Avatar Image Full Frame)
- `static/css/style.css`: 將 `.avatar-card`、`.avatar-wrapper` 與 `.avatar-img` 設為滿版 100% 填滿整個外框（不再使用 160px 圓形剪裁），並設定 `z-index: 5` 保持浮動徽章層級正常。

## [v2.1.0] - 2026-08-19 (Update Avatar Image & Styles)
- `templates/index.html`: 將 Hero 區塊圖示替換為 `static/images/images (1).jpg` 照片。

## [v2.0.0] - 2026-08-19 (Backend Refactored to Python 3.12 Flask & Gunicorn)
- 重構為 Flask 後端架構與 Cloud Run Python 3.12 容器化環境。

---

## [v1.0.0] - 2026-08-18 (Complete Initial Portfolio & Nginx Architecture)
- Initial release with static Nginx architecture.
