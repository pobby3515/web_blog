import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """渲染履歷網站首頁"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact_api():
    """處理聯絡表單 API 請求"""
    try:
        data = request.get_json() if request.is_json else request.form
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        if not name or not email or not message:
            return jsonify({
                "status": "error",
                "message": "請填寫所有必填欄位 (姓名、Email 與訊息內容)。"
            }), 400
            
        # 在此可擴充發送 Email 或儲存資料庫邏輯
        print(f"[Contact Received] Name: {name}, Email: {email}, Message: {message}")
        
        return jsonify({
            "status": "success",
            "message": f"感謝您的來信，{name}！我們已收到您的訊息，會盡快與您聯繫。"
        }), 200
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {e}")
        return jsonify({
            "status": "error",
            "message": "伺服器處理失敗，請稍後再試。"
        }), 500

@app.route('/health')
def health_check():
    """Cloud Run 健康檢查端點"""
    return jsonify({"status": "healthy", "service": "flask-portfolio"}), 200

if __name__ == '__main__':
    # 本地測試預設運行於 5000 埠
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
