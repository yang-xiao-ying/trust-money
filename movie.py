from flask import Flask
from flask import (
    render_template,
    request,
)
from database import mysql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("server.html")


def getMovieInfo(sql):
    info = []
    mydb = mysql.linkDatabase()
    print(mydb)
    mycursor = mydb.cursor()
    try:

        mycursor.execute(sql)
        myresult = mycursor.fetchall()  # fetchall() 获取所有记录
        for s in myresult:
            movieinfo = {}
            movieinfo['name'] = s[0]
            movieinfo['other'] = s[1]
            movieinfo['score'] = s[2]
            movieinfo['quote'] = s[3]
            movieinfo['cover_url'] = s[4]
            info.append(movieinfo)
        # print(info)
    except Exception as e:
        print('查找不存在')
    finally:
        mycursor.close()

    return info


@app.route("/seek", methods=['POST'])
def register():
    form = request.form.to_dict()
    print(form)
    name = form['name']
    score = form['score']
    ms = []
    if name:
        sql = "select * from movies where name like '{}%'".format(name)
        ms = getMovieInfo(sql)
        print(ms)
    elif score:
        sql = "select * from movies where score={}".format(score)
        ms = getMovieInfo(sql)
        print(ms)
    return render_template("server.html", ms=ms)


if __name__ == '__main__':
    app.run()
