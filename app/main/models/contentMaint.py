from datetime import datetime

from models.dbgetter import getDb

def getContent(date):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    db = getDb()
    cursor = db.cursor()
    sql="select id, title, summary, contenttype, numlike, numview from content\
          where date(created_at) = \'%s\' "%(date)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(date)
    print(sql)
    print(results)
    if results is None or len(results) ==0 or len(results) > 3:
        return {"code": 401, "msg": "数据错误"}
    else:
        out = []
        for result in results:
            out.append({"id": result[0], "title": result[1],
                         "summary": result[2], "contenttype": result[3],
                           "numlike": result[4], "numview": result[5]})
        return {"code": 200, "msg": "成功", "data": out}
    
def addView(contentId):
    if contentId is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "update content set numview = numview + 1 where id = %s"%(contentId,)
        cursor.execute(sql)
        db.commit()
        db.close()
        return {"code": 200, "msg": "成功"}
    
    
def addLike(contentId):
    if contentId is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "update content set numlike = numlike + 1 where id = %s"%(contentId,)
        cursor.execute(sql)
        db.commit()
        db.close()
        return {"code": 200, "msg": "成功"}
    
def deleteLike(contentId):
    if contentId is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        sql = "update content set numlike = numlike - 1 where id = %s"%(contentId,)
        cursor.execute(sql)
        db.commit()
        db.close()
        return {"code": 200, "msg": "成功"}
