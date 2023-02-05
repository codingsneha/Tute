import pymysql

def getDatabaseConnection(ipaddress, usr, passwd, charset, curtype):
    sqlCon  = pymysql.connect(host=ipaddress, user=usr, password=passwd, charset=charset, cursorclass=curtype)
    return sqlCon

def createUser(cursor, userName, password,
               querynum=0, 
               updatenum=0, 
               connection_num=0):
    try:
        sqlCreateUser = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';"%(userName, password)
        cursor.execute(sqlCreateUser)
    except Exception as Ex:
        print("Error creating MySQL User: %s"%(Ex))

ipa = "127.0.0.1"
usr         = "host"       
passwd      = ""            
charset     = "utf8mb4"     
curtype    = pymysql.cursors.DictCursor    

mySQLConnection = getDatabaseConnection(ipa, usr, passwd, charset, curtype)
mySQLCursor     = mySQLConnection.cursor()

createUser(mySQLCursor, "tute","pwd")

mySqlListUsers = "select host, user from mysql.user;"
mySQLCursor.execute(mySqlListUsers)

userList = mySQLCursor.fetchall()

print("List of users:")
for user in userList:
    print(user)