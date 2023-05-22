from flask import render_template, request, redirect, url_for
from flask import Blueprint

from models.homaMaint import checkInHomePage

homePage_blueprint = Blueprint('homePage_blueprint', __name__)

@homePage_blueprint.route('/homePage', methods=['GET', 'POST'])
def homePage_handler():
    if request.method == 'GET':
        username = request.headers.get('username')
        return render_template('homePage3.html', title='homePage', username=username)
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 4001, "msg": "请求参数错误"}
        else:
            username = data.get('username')
            if username is None:
                #you ke fang wen
                return {"code": 4002, "msg": "请求参数错误"}
            else:
                return checkInHomePage(username)
    return {"code": 403, "msg": "方法参数错误"}

        


