# -*- coding: UTF-8 -*-

from get_file_list import get_files

from connect_mysql import connect_db
from connect_mysql import connect_close
from save_xml_db import save_xml_data

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':

    begin = datetime.datetime.now()

    file_path = unicode("F:\\南京大学\\毕设\\共享文书\\民事一审\\", 'utf-8')

    # 测试一篇文书
    # filename = unicode("1242875.xml", 'utf-8')
    # save_xml_data(file_path, filename)

    # 多篇文书
    files = get_files(file_path)

    print "共有", len(files), "篇文书"

    i = 0

    connect_db()
    for filename in files:
        i += 1
        save_xml_data(file_path, filename)
    connect_close()

    end = datetime.datetime.now()

    runtime = end - begin

    print "运行时间：", runtime

    # print "写入了", i, "篇文书"

