# -*- coding: UTF-8 -*-

import MySQLdb


#   连接数据库
def connect_db():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='bs',
        charset="utf8"
    )
    return conn

conn = connect_db()


#   关闭数据库连接
def connect_close():
    conn.close()
