# Pobby Blog - 個人履歷與作品集網站

基於 Python Flask 與現代 Glassmorphism 前端技術打造的個人履歷與作品集網站。


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
└── README.md               # 專案說明文件
```

