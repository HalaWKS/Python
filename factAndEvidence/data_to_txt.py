# -*- coding: UTF-8 -*-

import MySQLdb
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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


if __name__ == '__main__':
    cur = conn.cursor()

    result_set = []

    sql_select_fact_info = "SELECT * FROM bs.fact_evidence_information"

    try:
        cur.execute(sql_select_fact_info)
        result_set = cur.fetchall()
    except:
        print "Error: unable to fecth data"

    print "Num of fact_info:", len(result_set)

    # result[0]:ID
    # result[1]:文书编号
    # result[2]:案由
    # result[3]:fact-事实原文
    # result[4]:fact_divide-事实分词结果
    # result[5]:fact_keyword-事实关键词
    # result[6]:evidence-证据
    # result[7]:evidence_divide证据分词结果
    # result[8]:evidence_keyword证据关键词
    # result[9]:事实是否被认定
    data_list = []
    file_object = open('F:\\bsfile\\fact_evidence_data.txt', 'w')
    for result in result_set:
        fact = result[3] + '\n'
        evidence = result[6] + '\n'
        is_identified = result[9] + '\n'
        data_list.append(fact)
        data_list.append(evidence)
        data_list.append(is_identified)
        data_list.append('\n')
    file_object.writelines(data_list)
    file_object.close()




