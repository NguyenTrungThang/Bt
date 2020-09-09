from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "b'ZZ~\xa6T\xf7\xe9\x9e\xd6oo\x8e\xaaq!O'"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:666666@localhost/mydb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

admin = Admin(app=app, name="Quản lý thư viện", template_mode="bootstrap3")

login = LoginManager(app=app)