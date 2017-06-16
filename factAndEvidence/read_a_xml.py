# -*- coding: UTF-8 -*-
# 解析文书.xml，在其中提取关键数据

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def read_xml(filename):

    root = ET.parse(filename)

    evidence = ""

    # 案由
    ays = root.getiterator('AY')
    for ay in ays:
        if ay.attrib.has_key('value'):
            print "案由：", ay.attrib['value']

    # 查明事实段
    cmssds = root.getiterator('CMSSD')
    for cmssd in cmssds:
        if cmssd.attrib.has_key('value'):
            print "查明事实段：", cmssd.attrib['value']

    if len(cmssds) == 0:
        print "无查明事实段"
        return

    # 证据段
    zjds = root.getiterator('ZJD')
    # print "证据段长度：", len(zjds)
    for zjd in zjds:
        if zjd.attrib.has_key('value'):
            evidence += zjd.attrib['value']
    print "证据段：", evidence

    # 原告诉称段
    ygscds = root.getiterator('YGSCD')
    # print "原告诉称段长度：", len(ygscds)
    if len(ygscds) == 0:
        return

    for ygscd in ygscds:
        if ygscd.attrib.has_key('value'):
            print "原告诉称段：", ygscd.attrib['value']
            fact_all = ygscd.attrib['value']
            facts = fact_all.split('。')

    for fact in facts:
        print fact


if __name__ == '__main__':

    filename = "F:\\南京大学\\毕设\\共享文书\\Test\\1241966.xml"
    filename_utf8 = unicode(filename, 'utf-8')

    read_xml(filename_utf8)

