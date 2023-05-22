from models.dbgetter import getDb
from models.contentMaint import addLike, deleteLike
# from dbgetter import getDb
# from contentMaint import addLike

def userlike(user_id, content_id):
    if user_id is None or content_id is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "select * from userlike where userid = %s and contentid = %s"%(user_id, content_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is not None and len(results) > 0:
            return {"code": 4011, "msg": "数据插入错误，数据冲突"}
        sql = "insert into userlike(userid, contentid) values(%s, %s)"%(user_id, content_id)
        print('userlike',sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        db.commit()
        db.close()
        addLike(content_id)
        # print(3,results)
        # try:
        #     cursor.execute(sql)
        #     results = cursor.fetchall()
        #     db.commit()
        #     db.close()
        #     print(2,results)
        #     addLike(content_id)
        # except:
        #     return {"code": 400, "msg": "请求参数错误"}
        return {"code": 200, "msg": "成功"}
    
def userdislike(user_id,content_id):
    if user_id is None or content_id is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "select * from userlike where userid = %s and contentid = %s"%(user_id, content_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(1,results)
        if results is None or len(results) == 0:
            return {"code": 401, "msg": "数据错误"}
        sql = "delete from userlike where userid = %s and contentid = %s"%(user_id, content_id)
        cursor.execute(sql)
        db.commit()
        db.close()
        deleteLike(content_id)
        return {"code": 200, "msg": "成功"}
    
def checklike(user_id, content_id):
    if user_id is None or content_id is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "select * from userlike where userid = %s and contentid = %s"%(user_id, content_id)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results is None or len(results) == 0:
            return {"code": 200, "msg": "成功", "data": {"like": False}}
        else:
            return {"code": 200, "msg": "成功", "data": {"like": True}}
    

# if __name__ == '__main__':
#     db = getDb()
#     user_id = 1
#     article_id = 101
#     # sql = "insert into userlike(userid, contentid) values(%s, %s)"%(user_id, article_id)
#     sql = "delete from userlike where userid = %s and contentid = %s"%(user_id, article_id)
#     cursor = db.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     db.commit()
#     db.close()

