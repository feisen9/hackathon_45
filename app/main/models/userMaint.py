from models.dbgetter import getDb

def checkUser(username, password):
    """
    Checks if a user with the given username and password exists in the database.

    :param username: The username of the user to check.
    :type username: str
    :param password: The password of the user to check.
    :type password: str
    :return: True if the user exists, False otherwise.
    :rtype: bool
    """
    db = getDb()
    cursor = db.cursor()
    cursor.execute("select * from user where username = %s and pass = %s", (username, password))
    results = cursor.fetchall()
    db.close()
    if results is None or len(results) == 0:
        return False
    else:
        return True

def addUser(username, password):
    db = getDb()
    cursor = db.cursor()
    cursor.execute("insert into user (username, pass) values (%s, %s)", (username, password))
    db.commit()
    db.close()

def deleteUser(username):
    db = getDb()
    cursor = db.cursor()
    cursor.execute("delete from user where username = %s", (username,))
    db.commit()
    db.close()

def updateUser(username, password):
    db = getDb()
    cursor = db.cursor()
    cursor.execute("update user set pass = %s where username = %s", (password, username))
    db.commit()
    db.close()

def getUserId(username):
    db = getDb()
    cursor = db.cursor()
    cursor.execute("select id from user where username = %s", (username,))
    results = cursor.fetchall()
    db.close()
    if results is None or len(results) != 1:
        return None
    else:
        return results[0][0]

if __name__ == '__main__':
    r = checkUser('admin', '123456')
    print(r)
    # print(len(r))