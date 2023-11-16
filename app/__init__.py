from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
app=Flask(__name__)
app.secret_key='3487ywheenujbhreriu4ui$$&()&^^^9erjrtunbr'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:1234@localhost/saleapp_db?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db=SQLAlchemy(app=app)
login=LoginManager(app=app)
