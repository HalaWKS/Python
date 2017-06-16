# -*- coding: UTF-8 -*-

import xlwt
from connect_mysql import connect_db
from connect_mysql import connect_close


import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 数据表写入Excel
def sql_to_excel(tablename, outputpath):
    conn = connect_db()
    cur = conn.cursor()

    result_set = []

    sql_select = "SELECT * FROM bs." + tablename

    # print sql_select

    cur.execute(sql_select)

    result_set = cur.fetchall()

    # 获取表中的数据字段名称
    fields = cur.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('table_' + tablename, cell_overwrite_ok=True)

    # print fields

    cur.close()
    connect_close()

    # 写上字段信息
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1, len(result_set)+1):
        for col in range(0, len(fields)):
            sheet.write(row, col, result_set[row-1][col])

    workbook.save(outputpath)


if __name__ == '__main__':

    begin = datetime.datetime.now()

    tablename = "fact_evidence_info"
    outputpath = "F:\\bsfile\\fact_evidence_info.xls"
    sql_to_excel(tablename, outputpath)

    end = datetime.datetime.now()
    runtime = end - begin
    print "运行时间：", runtime
