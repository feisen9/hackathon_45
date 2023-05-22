from models.dbgetter import getDb

def getArticle(articleId):
    if articleId is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "select articlename, author, articleinfo,articlecontent,photosetid\
             from article where id = %s"%(articleId,)
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        if results is None or len(results) != 1:
            return {"code": 401, "msg": "数据错误"}
             #Error
        else:
            out = {}
            out['articlename'] = results[0][0]
            out['author'] = results[0][1]
            out['articleinfo'] = results[0][2]
            out['articlecontent'] = results[0][3]
            out['photosetid'] = results[0][4]
            # print(out)
            return {"code": 200, "msg": "成功", "data": out}