# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


global num_of_has_judge
num_of_has_judge = 0

def read_xml(file_path, filename):

    root = ET.parse(file_path + filename)
    # 案由
    cause_of_faction = ""
    # 是否被证实
    is_identified = "-1"
    # 事实
    facts = ""
    # 查明事实
    fact_identify = ""
    # 证据
    evidence = ""

    # 是否有“判定”
    has_judge = False

    # 案由
    ays = root.getiterator('AY')
    for ay in ays:
        if ay.attrib.has_key('value'):
            cause_of_faction = ay.attrib['value']
            # print "案由：", cause_of_faction

    # 查明事实段
    cmssds = root.getiterator('CMSSD')
    for cmssd in cmssds:
        if cmssd.attrib.has_key('value'):
            fact_identify = cmssd.attrib['value']
            # print "查明事实段：", fact_identify

    # 证据段
    zjds = root.getiterator('ZJD')
    for zjd in zjds:
        if zjd.attrib.has_key('value'):
            # 整合原告+被告的证据
            evidence += zjd.attrib['value']
    # print "证据段：", evidence

    # 原告诉称段
    ygscds = root.getiterator('YGSCD')
    # 如果没有原告诉称段，就直接返回
    if len(ygscds) == 0:
        return

    for ygscd in ygscds:
        if ygscd.attrib.has_key('value'):
            all_fact = ygscd.attrib['value'].strip()
            facts = all_fact.split('。')
            # print "原告诉称段：", all_fact
            # fact_all = ygscd.attrib['value']
            # facts = fact_all.split('。')

    all_fact = all_fact.replace(" ", "")

    # for fact in facts:
    #     print fact

    # # 检查是否有原告诉称段，没有就return
    # if all_fact == None:
    #     return

    # 检查诉称段是否有“判定”
    # if ("判令" in all_fact) or ("判决" in all_fact) or ("请求" in all_fact):
    #     has_judge = True
    #     global num_of_has_judge
    #     num_of_has_judge += 1

    # 有“请求”的部分
    # if "请求" in all_fact:
    #     print filename

    # print filename, "是否有诉求：", has_judge

    return [all_fact, fact_identify]
