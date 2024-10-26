from flask import Flask

app = Flask(__name__)

from app import routes  # Import routes

# Hàm khởi tạo ứng dụng Flask
def create_app():
    app.config.from_object('config.config.DevelopmentConfig')
    return app