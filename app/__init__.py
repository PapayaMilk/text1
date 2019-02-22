from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from app.views.acc import acc
from app.views.user import user


def create_app():
    my_app = Flask(__name__)
    my_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@127.0.0.1:3306/day127?charset=utf8"
    my_app.config["SQLALCHEMY_POOL_SIZE"] = 5
    my_app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
    my_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(my_app)
    my_app.register_blueprint(acc)
    my_app.register_blueprint(user)

    return my_app
