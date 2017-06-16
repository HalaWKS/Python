# -*- coding: UTF-8 -*-

# from connect_mysql_test import connect_db
# from connect_mysql_test import conn
# from connect_mysql_test import connect_close
from get_file_test import get_files
from read_xml_test import read_xml
from divide_fact_test import divide_sentence

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET



if __name__ == '__main__':

    file_path = unicode("F:\\南京大学\\毕设\\共享文书\\Test\\", 'utf-8')
    filename = unicode("1014730.xml", 'utf-8')

    fact_and_idedfact = read_xml(file_path, filename)

    facts = fact_and_idedfact[0]
    fact_identified = fact_and_idedfact[1]

    print facts
    print fact_identified

    facts_divided = facts.split("。")

    for fact in facts_divided:
        
        print fact


    # files = get_files(file_path)

    # print "共有", len(files), "篇文书"

    # for filename in files:
    #     read_xml(file_path, filename)

    # print "有", num_of_has_judge, "篇文书有诉求"


    # str1 = "请求"
    # str2 = "请求判定：1.诉讼费由被告承担"
    # print str1 in str2
