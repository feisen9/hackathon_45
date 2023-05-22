import pymysql

def getDb():
    db = pymysql.connect(host = "127.0.0.1", user = "hackathon_45",
                      password="12345678",database = "hackathon_45",
                      charset = 'utf8mb4')
    return db