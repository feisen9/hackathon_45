from models.dbgetter import getDb
from models.contentMaint import getContent
from utils.imgutils import imagefile_to_base64

from __init__ import imgConf

def checkInHomePage(username):
    if username is None:
        return {"code": 400, "msg": "请求参数错误"}
    else:
        db = getDb()
        cursor = db.cursor()
        cursor.execute("select username, icon from user where username = %s", (username,))
        results = cursor.fetchall()
        db.close()
        if results is None or len(results) != 1:
            return {"code": 401, "msg": "数据错误"}
             #Error
        else:
            out = {}
            out['username'] = results[0][0]
            out['icon'] = results[0][1]
            content = getContent(None)
            if content['code'] != 200:
                return {"code": 401, "msg": "数据错误"}
                #Error
            else:
                for row in content['data']:
                    out[row['contenttype']] = row
                
                icon_path = (imgConf.config['ICON'] + out['icon']).strip()
                print(icon_path)
                out['iconimg'] = imagefile_to_base64(icon_path)
                return {"code": 200, "msg": "成功", "data": out}




