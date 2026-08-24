# Pobby Blog - 個人履歷與作品集網站

基於 Python Flask 與現代 Glassmorphism 前端技術打造的個人履歷與作品集網站。

---

## 🏗️ 網站架構 (Architecture)

```text
┌─────────────────────────────────────────────────────────────┐
│                       使用者瀏覽器 (Client)                   │
│         [HTML5 + CSS3 Glassmorphism + JavaScript]           │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP / HTTPS (JSON)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                    後端服務 (Flask Backend)                  │
│                                                             │
│  • GET  /             -> 渲染履歷首頁 (index.html)            │
│  • POST /api/contact  -> 處理聯絡表單並發送 Email 通知        │
│  • GET  /health       -> Cloud Run 服務健康檢查端點           │
└──────────────┬──────────────────────────────┬───────────────┘
               │                              │
               ▼                              ▼
┌─────────────────────────────┐┌──────────────────────────────┐
│       Google Gmail SMTP     ││      Google Cloud Run        │
│      (Flask-Mail 寄信)      ││   (Docker + uv 容器化部署)    │
└─────────────────────────────┘└──────────────────────────────┘
```

---

## 📂 檔案目錄結構 (Project Structure)

```text
web/
├── app.py                  # Flask 後端主程式 (路由、API、郵件發送)
├── pyproject.toml          # uv 專案設定與套件依賴
├── Dockerfile              # Docker 容器化建置檔 (uv sync)
├── templates/
│   └── index.html          # 前端主頁模板
├── static/
│   ├── css/
│   │   └── style.css       # 網站樣式 (深色主題、玻璃擬態、RWD)
│   ├── js/
│   │   └── main.js         # 前端互動 (打字特效、表單 AJAX)
│   └── images/             # 圖片素材 (個人照、Favicon)
├── .env.example            # 環境變數範本檔
└── README.md               # 專案說明文件
```

---

## 🚀 快速啟動 (Quick Start)

```bash
# 1. 同步虛擬環境與依賴
uv sync

# 2. 啟動本機伺服器
uv run python app.py
```
預設伺服器運行於：`http://127.0.0.1:5000`
