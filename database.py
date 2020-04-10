import pymysql


class mysql():
    @staticmethod
    def creatDatabase():
        mydb = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='zaoshuizaoqi',
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE movieslist")
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)

    @staticmethod
    def linkDatabase():
        mydb = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='zaoshuizaoqi',
            database="movieslist",
        )
        return mydb


def creatTable():
    mycursor = mysql.linkDatabase().cursor()
    tablesql = "CREATE TABLE movies (name VARCHAR(255) PRIMARY KEY, other VARCHAR(255), score VARCHAR(255)," \
               "quote VARCHAR(255),cover_url VARCHAR(255))"
    mycursor.execute(tablesql)
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

# mysql.creatDatabase()
# creatTable()