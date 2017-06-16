# -*- coding: UTF-8 -*-

# from connect_mysql import connect_db
# from connect_mysql import connect_close
from connect_mysql import conn

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def get_evidence():

    # conn = connect_db()
    cur = conn.cursor()

    result_set = []

    sql_select_evidence = "SELECT * FROM bs.evidence"

    try:
        cur.execute(sql_select_evidence)
        result_set = cur.fetchall()
    except:
        print "Error: unable to fecth data"

    print "Num of evidence:", len(result_set)

    cur.close()
    # connect_close()

    return result_set


if __name__ == '__main__':
    get_evidence()
