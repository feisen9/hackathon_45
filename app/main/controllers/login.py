from flask import render_template, request, redirect, url_for
from flask import Blueprint

from models.userMaint import checkUser,addUser,getUserId

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login_handler():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 400, "msg": "请求参数错误"}
        username = data.get('username')
        password = data.get('password')
        if username and password:
            if checkUser(username, password):
                nextUrl = url_for('homePage_blueprint.homePage_handler')
                return {"code": 200, "msg": "登录成功", "nextUrl":nextUrl,"userId":getUserId(username)}
            else:
                return {"code": 400, "msg": "用户名或密码错误"}
        elif username:
            return {"code": 400, "msg": "密码缺失"}
        elif password:
            return {"code": 400, "msg": "用户名缺失"}
    return {"code": 403, "msg": "方法参数错误"}


@login_blueprint.route('/register', methods=['GET', 'POST'])
def register_handler():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 400, "msg": "请求参数错误"}
        username = data.get('username')
        password = data.get('password')
        if username and password:
            if checkUser(username, password):
                return {"code": 400, "msg": "用户名已存在"}
            else:
                addUser(username, password)
                return {"code": 200, "msg": "注册成功"}
        elif username:
            return {"code": 400, "msg": "密码缺失"}
        elif password:
            return {"code": 400, "msg": "用户名缺失"}