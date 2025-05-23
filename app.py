# app.py
from flask import Flask

app = Flask(__name__)

# Добавляем security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route('/')
def home():
    return "Hello, Practice202!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
