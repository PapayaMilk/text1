from flask import Blueprint

acc = Blueprint("acc", __name__)


@acc.route('/acc')
def acc_func():
    return "这是acc蓝图页面"
