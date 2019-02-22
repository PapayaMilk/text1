from flask import Blueprint, jsonify
from app.models import User
from app import db

user = Blueprint("user", __name__)


@user.route('/user')
def user_func():
    user_obj = User(name="DragonFire")
    db.session.add(user_obj)
    db.session.commit()
    return "这是user蓝图页面"


@user.route('/user_list')
def user_func1():
    res = User.query.first()
    ret = {"username": res.name}
    return jsonify(ret)
