# -*- coding: UTF-8 -*-


from connect_mysql import conn
from delete_appeal import delete_appeal
from util import delete_space
from util import list_to_string
from judge_fact import judge_relevance
from judge_fact import get_match_rate
from find_key_word import get_key_word_list
from divide_fact import get_divide_list
from divide_evidence import get_evidence_keyword
from divide_evidence import get_divide_result

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# 返回提取的数据
# result[0]:事实原文
# result[1]:事实分词结果
# result[2]:事实关键词
# result[3]:证据
# result[4]:证据分词结果
# result[5]:证据关键词
# return[] = [fact, fact_divide, fact_keyword, evidence, evidence_divide, evidence_keyword]
def get_xml_data(file_path, filename):

    root = ET.parse(file_path + filename)
    # 文书情况
    condition = "正常"
    # 事实
    facts = ""
    # 证据
    evidence = ""
    # 是否被证实
    is_identified = "-1"
    # 证据关键词
    evidence_keyword = ""
    # 证据分词
    evidence_divide = ""
    # 事实分词列表
    divide_fact_list = []
    # 关键词列表
    key_words_list = []
    # 返回数组
    return_list = []

    # 证据段
    zjds = root.getiterator('ZJD')
    for zjd in zjds:
        if zjd.attrib.has_key('value'):
            # 整合原告+被告的证据
            evidence += zjd.attrib['value']
    # print "证据段：", evidence

    if len(zjds) == 0:
        condition = "无证据"
        print filename, "无证据"
        return

    evidence = delete_space(evidence)
    evidence_divide = get_divide_result(evidence)
    evidence_keyword = get_evidence_keyword(evidence)

    # 原告诉称段
    ygscds = root.getiterator('YGSCD')
    for ygscd in ygscds:
        if ygscd.attrib.has_key('value'):
            all_fact = ygscd.attrib['value'].strip()
            # print "原告诉称段：", all_fact
            # fact_all = ygscd.attrib['value']
            # facts = fact_all.split('。')

    if len(ygscds) == 0:
        condition = "无原告诉称"
        print filename, "无原告诉称"
        return

    # 查明事实段
    cmssds = root.getiterator('CMSSD')
    for cmssd in cmssds:
        if cmssd.attrib.has_key('value'):
            fact_identify = cmssd.attrib['value']
            # print "查明事实段：", fact_identify

    if len(cmssds) == 0:
        condition = "无查明事实"
        print filename, "无查明事实"
        return

    fact_identify = delete_space(fact_identify)

    # 删除空格
    all_fact = delete_space(all_fact)

    # 根据句号划分
    facts = all_fact.split('。')

    # 删除诉求部分
    facts = delete_appeal(facts)

    for fact in facts:

        # 删去事实中的脏数据。中间有空白项，就跳过
        if (fact == "") or (fact == "……") or (len(fact) < 10):
            continue

        # 获得分词结果
        fact_divide = list_to_string(get_divide_list(fact))

        #获得关键词
        fact_keyword = list_to_string(get_key_word_list(fact))

        # 判断是否被认定
        match_rate = get_match_rate(fact, fact_identify)
        identify = judge_relevance(match_rate)
        if identify:
            is_identified = 1
        else:
            is_identified = 0

        # [fact, fact_divide, fact_keyword, evidence, evidence_divide, evidence_keyword, is_identified]
        a_set_of_data = [fact, fact_divide, fact_keyword, evidence, evidence_divide, evidence_keyword, is_identified]
        return_list.append(a_set_of_data)

    return return_list


# 将提取的数据写入数据库
def save_xml_data(file_path, filename):

    root = ET.parse(file_path + filename)
    # 文书情况
    condition = "正常"
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
    # 事实分词列表
    divide_fact_list = []
    # 关键词列表
    key_words_list = []
    # SQL语句和游标声明
    sql_fact_evidence = "insert into fact_evidence (filename, fact, factidentify, isidentified, causeoffaction, evidence)" \
                        " values(%s, %s, %s, %s, %s, %s)"
    sql_fact_info = "insert into fact_info (filename, divideresult, keyword, fact, match_rate)" \
                    " values(%s, %s, %s, %s, %s)"
    sql_doc_condition = "insert into doc_condition (filename, con)" \
                        " values(%s, %s)"
    cur = conn.cursor()

    # 案由
    ays = root.getiterator('AY')
    for ay in ays:
        if ay.attrib.has_key('value'):
            cause_of_faction = ay.attrib['value']
            # print "案由：", cause_of_faction

    if len(ays) == 0:
        condition = "无案由"
        cur.execute(sql_doc_condition, (filename, condition))
        cur.close()
        conn.commit()
        print filename, "无案由"
        return

    cause_of_faction = delete_space(cause_of_faction)

    # 查明事实段
    cmssds = root.getiterator('CMSSD')
    for cmssd in cmssds:
        if cmssd.attrib.has_key('value'):
            fact_identify = cmssd.attrib['value']
            # print "查明事实段：", fact_identify

    if len(cmssds) == 0:
        condition = "无查明事实"
        cur.execute(sql_doc_condition, (filename, condition))
        cur.close()
        conn.commit()
        print filename, "无查明事实"
        return

    fact_identify = delete_space(fact_identify)

    # 证据段
    zjds = root.getiterator('ZJD')
    for zjd in zjds:
        if zjd.attrib.has_key('value'):
            # 整合原告+被告的证据
            evidence += zjd.attrib['value']
    # print "证据段：", evidence

    if len(zjds) == 0:
        condition = "无证据"
        cur.execute(sql_doc_condition, (filename, condition))
        cur.close()
        conn.commit()
        print filename, "无证据"
        return

    evidence = delete_space(evidence)

    # 原告诉称段
    ygscds = root.getiterator('YGSCD')
    for ygscd in ygscds:
        if ygscd.attrib.has_key('value'):
            all_fact = ygscd.attrib['value'].strip()
            # print "原告诉称段：", all_fact
            # fact_all = ygscd.attrib['value']
            # facts = fact_all.split('。')

    if len(ygscds) == 0:
        condition = "无原告诉称"
        cur.execute(sql_doc_condition, (filename, condition))
        cur.close()
        conn.commit()
        print filename, "无原告诉称"
        return

    # 删除空格
    all_fact = delete_space(all_fact)

    # 根据句号划分
    facts = all_fact.split('。')

    # 删除诉求部分
    facts = delete_appeal(facts)

    # 写入数据库

    facts_len = len(facts)
    # i = 0

    for fact in facts:

        # i += 1
        # 删去事实中的脏数据。中间有空白项，就跳过
        if (fact == "") or (fact == "……") or (len(fact) < 10):
            continue

        # 不写入最后的一个空白项
        # if i == facts_len:
        #     break

        # 获得分词结果
        divide_fact_result = list_to_string(get_divide_list(fact))

        #获得关键词
        key_word = list_to_string(get_key_word_list(fact))

        # 判断是否被认定
        match_rate = get_match_rate(fact, fact_identify)
        identify = judge_relevance(match_rate)
        if identify:
            is_identified = 1
        else:
            is_identified = 0

        cur.execute(sql_fact_evidence, (filename, fact, fact_identify, is_identified, cause_of_faction, evidence))
        cur.execute(sql_fact_info, (filename, divide_fact_result, key_word, fact, match_rate))

    cur.execute(sql_doc_condition, (filename, condition))

    cur.close()
    conn.commit()
