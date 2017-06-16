# -*- coding: UTF-8 -*-

from get_file_test import get_files

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# 检查出现多个“查明事实段”的文书
def read_xml(file_path, filename):

    root = ET.parse(file_path + filename)

    # 查明事实
    fact_identify = ""
    len_of_fact = 0

    # print filename

    # 查明事实段
    cmssds = root.getiterator('CMSSD')

    if len(cmssds) == 0:
        return

    for cmssd in cmssds:
        if cmssd.attrib.has_key('value'):
            fact_identify = cmssd.attrib['value']
            len_of_fact = len(fact_identify)

    if len_of_fact < 60:
        print filename
        print "查明事实段：", fact_identify
        print "长度：", len_of_fact

    # print len(cmssds)

    # if len(cmssds) == 0:
    #     print "无查明事实段"

if __name__ == '__main__':

    file_path = unicode("F:\\南京大学\\毕设\\共享文书\\民事一审\\", 'utf-8')
    # filename = unicode("1020024.xml", 'utf-8')

    # read_xml(file_path, filename)

    files = get_files(file_path)

    print "共有", len(files), "篇文书"

    for filename in files:
        read_xml(file_path, filename)
