from flask import render_template, request, redirect, url_for
from flask import Blueprint

from models.articleMaint import getArticle
from models.userLike import checklike, userlike, userdislike
from models.contentMaint import addView

articlePage_blueprint = Blueprint('articlePage_blueprint', __name__)

@articlePage_blueprint.route('/articlePage', methods=['GET', 'POST'])
def articlePage_handler():
    if request.method == 'GET':
        return render_template('articlepage.html')
    elif request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 4001, "msg": "请求参数错误"}
        else:
            articleid = data.get('articleId')
            if articleid is None:
                return {"code": 4002, "msg": "请求参数错误"}
            else:
                print(addView(articleid))
                result = getArticle(articleid)
                return result
    return {"code": 403, "msg": "方法参数错误"}


@articlePage_blueprint.route('/addview', methods=['POST'])
def addview_handler():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 4001, "msg": "请求参数错误"}
        else:
            contentid = data.get('contentId')
            if contentid is None:
                return {"code": 4002, "msg": "请求参数错误"}
            else:
                return addView(contentid)
    return {"code": 403, "msg": "方法参数错误"}

@articlePage_blueprint.route('/checkLike', methods=['POST'])
def checkLike_handler():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 4001, "msg": "请求参数错误"}
        else:
            contentid = data.get('contentId')
            userid = data.get('userId')
            if contentid is None or userid is None:
                return {"code": 4002, "msg": "请求参数错误"}
            else:
                return checklike(userid, contentid)
    return {"code": 403, "msg": "方法参数错误"}

@articlePage_blueprint.route('/like', methods=['POST'])
def like_handler():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return {"code": 4001, "msg": "请求参数错误"}
        else:
            contentid = data.get('contentId')
            userid = data.get('userId')
            tolike = data.get('toLike')
            print(contentid,userid,tolike)
            if contentid is None or userid is None or tolike is None:
                print(4,data)
                return {"code": 4002, "msg": "请求参数错误"}
            else:
                if tolike:
                    return userlike(userid, contentid)
                else:
                    return userdislike(userid, contentid)
    return {"code": 403, "msg": "方法参数错误"}