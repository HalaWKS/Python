# -*- coding: UTF-8 -*-

# from connect_mysql import connect_db
# from connect_mysql import connect_close
from connect_mysql import conn
from divide_evidence import get_divide_result
from divide_evidence import get_evidence_keyword

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 存入evidence_info表
def save_evidence_info(result_set):

    cur = conn.cursor()

    sql_insert_evidence_info = "insert into evidence_info (filename, evidence, divide_result, key_words)" \
                        " values(%s, %s, %s, %s)"

    # 遍历结果集，每一个result代表一个证据明细：
    # result[0]:filename 文书编号
    # result[1]:factidentity 查明事实
    # result[2]:causeoffaction 案由
    # result[3]:evidence 证据
    i = 1
    for result in result_set:
        divide_result = get_divide_result(result[3])
        key_words = get_evidence_keyword(result[3])
        print "第", i, "篇：", result[0]
        i += 1
        try:
            cur.execute(sql_insert_evidence_info, (result[0], result[3], divide_result, key_words))
        except:
            conn.rollback()
    conn.commit()


