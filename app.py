import os
from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
app = Flask(__name__)

# Flask-Mail 郵件伺服器設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', '個人網站聯絡系統 <pobby3515@gmail.com>')

mail = Mail(app)

@app.route('/')
def index():
    """渲染履歷網站首頁"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact_api():
    """處理聯絡表單 API 請求並發送郵件"""
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
            
        print(f"[Contact Received] Name: {name}, Email: {email}, Message: {message}")
        
        # 若已設定 Gmail 密碼，則發送 Email 通知到指定信箱
        mail_username = app.config['MAIL_USERNAME']
        mail_password = app.config['MAIL_PASSWORD']
        recipient = os.getenv('MAIL_RECIPIENT', mail_username)
        
        if mail_username and mail_password and "your_16_digit" not in mail_password:
            msg = Message(
                subject=f"【個人網站聯絡通知】來自 {name} 的新訊息",
                recipients=[recipient],
                sender=app.config['MAIL_DEFAULT_SENDER'],
                reply_to=email,
                body=f"您好，有人在個人履歷網站提交了聯絡表單：\n\n"
                     f"📌 訪客姓名：{name}\n"
                     f"📌 電子信箱：{email}\n\n"
                     f"💬 訊息內容：\n{message}\n\n"
                     f"----------------------------------------\n"
                     f"本通知由個人履歷網站後端系統自動發送，直接點擊回覆即可回信給訪客。"
            )
            mail.send(msg)
            print(f"[Email Sent] Successfully delivered to {recipient}")
        
        return jsonify({
            "status": "success",
            "message": f"感謝您的來信，{name}！訊息已順利送出，我會盡快與您聯繫。"
        }), 200
        
    except Exception as e:
        app.logger.error(f"Error processing contact form: {e}")
        return jsonify({
            "status": "error",
            "message": "伺服器發送郵件失敗，請稍後再試。"
        }), 500

@app.route('/health')
def health_check():
    """Cloud Run 健康檢查端點"""
    return jsonify({"status": "healthy", "service": "flask-portfolio"}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
