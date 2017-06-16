# encoding=utf-8
# 获取证据和事实的分词结果集

from connect_mysql import connect_db
from connect_mysql import connect_close
from util import divide_to_words

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 判断分词结果是否应该被淘汰
# def should_be_eliminate(word, part_of_speech):
#
#     return False


# 获取证据分词结果集
def get_result_of_evidence():

    conn = connect_db()
    cur = conn.cursor()
    result_set = []

    sql_select_evidence_info = "SELECT divide_result FROM bs.evidence_info"

    try:
        cur.execute(sql_select_evidence_info)
        result_set = cur.fetchall()
    except:
        print "Error: unable to fecth data"

    print "evidence_num", len(result_set)

    # for result in result_set:
    #     print result[0]

    # connect_close()

    return result_set


# 获取事实分词结果集
def get_result_of_fact():

    conn = connect_db()
    cur = conn.cursor()
    result_set = []

    sql_select_evidence_info = "SELECT divideresult FROM bs.fact_info"

    try:
        cur.execute(sql_select_evidence_info)
        result_set = cur.fetchall()
    except:
        print "Error: unable to fecth data"

    print "fact_num", len(result_set)

    # for result in result_set:
    #     print result[0]

    connect_close()

    return result_set


if __name__ == '__main__':

    begin = datetime.datetime.now()

    words = divide_to_words(get_result_of_fact())

    for word in words:
        print word

    end = datetime.datetime.now()

    runtime = end - begin

    print "运行时间：", runtime
