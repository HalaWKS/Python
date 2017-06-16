# -*- coding: UTF-8 -*-
#  获取特征

from save_xml_db import get_xml_data
from connect_mysql import connect_db
from connect_mysql import connect_close
# from util import load_w2v_model
from util import sort_list
# from connect_mysql import conn
from gensim.models import word2vec
from pickle_operate import save_as_pkl

import re
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

path = 'F:\\bsfile\\w2v.model'
model = word2vec.Word2Vec.load(path)
word_list = []
for k, v in model.wv.vocab.items():
    word_list.append(k)


# 判断分词结果是否应该被筛掉
# word: '词语-词性'
def should_be_eliminate_divide(word):

    judge = False

    word_info = word.split('-')
    content = word_info[0]  # 词语
    flag = word_info[1]    # 词性

    # c-连词; d-副词; f-方位词; p-介词; r-代词; u-助词; x-标点;
    if ('c' in flag) or ('d' in flag) or ('f' in flag) \
            or ('p' in flag) or ('r' in flag) or ('u' in flag):
        judge = True

    if ('原告' in content) or ('被告' in content) or ('称' in content):
        judge = True

    # TODO 其他的分词筛选条件

    return judge


# 判断关键词是否应该被筛选掉
# word: '关键词-权重'
def should_be_eliminate_keyword(word):

    judge = False

    word_info = word.split('-')
    # print word_info
    content = word_info[0]  # 词语
    weight = word_info[1]    # 权重

    if ('原告' in content) or ('被告' in content) or ('证明' in content) or ('证据' in content):
        judge = True

    # TODO 其他的关键词筛选条件

    return judge


# 判断词语在不在词库里
def is_not_in_word_list(word):
    return word not in word_list


# 特征1：事实分词在证据整段内的重复率
# fact_divide:事实分词结果
# evidence:证据段
def f1_cal_fact_repeat_rate(fact_divide, evidence):
    fact_info_list = fact_divide.split('/')

    # 匹配数
    i = 0.0
    # 总数
    n = len(fact_info_list)

    for fact_info in fact_info_list:
        fact_flag = fact_info.split('-')
        word = fact_flag[0]     # 词语
        pattern = re.compile(word)
        if pattern.search(evidence):
            i += 1

    if n == 0.0:
        return 0.0

    rate = i / n

    return rate


# 特征2：事实分词和证据分词的关联度计算
# fact_divide_list:事实分词结果
# evidence_divide_list:证据分词结果
def f2_cal_divide_relevance(fact_divide, evidence_divide):

    fact_divide_list = fact_divide.split('/')
    evidence_divide_list = evidence_divide.split('/')

    # 加载模型
    # model = load_w2v_model()

    # 匹配总词数
    n = len(fact_divide_list)
    # 最大总关联度
    total_relv = 0.0

    for fact_info in fact_divide_list:
        if should_be_eliminate_divide(fact_info):   # 根据既定规则筛选词语
            continue
        fact_flag = fact_info.split('-')
        fact_word = fact_flag[0]     # 事实词语
        max_relv = 0.0  # 最大关联度
        if is_not_in_word_list(fact_word):  # 不在词库里的词语，不匹配
            n -= 1
            continue
        for evidence_info in evidence_divide_list:
            if should_be_eliminate_divide(evidence_info):  # 根据既定规则筛选词语
                continue
            evi_flag = evidence_info.split('-')
            evi_word = evi_flag[0]  # 证据词语
            if is_not_in_word_list(evi_word):   # 不在词库里的词语，不匹配
                continue
            relv = model.similarity(unicode(fact_word), unicode(evi_word))    # 计算事实词和证据词的关联度
            # print relv
            if relv > max_relv:
                max_relv = relv
        total_relv += max_relv

    if n == 0.0:
        return 0.0

    ave_relv = total_relv / n

    return ave_relv


# 特征3：事实和证据关键词的关联度计算
# fact_divide_list:事实关键词提取结果
# evidence_divide_list:证据关键词提取结果
# k：返回关联度前k大的
# 返回值里第一个是平均关联度
def f3_cal_keyword_relevance(fact_keyword, evidence_keyword, k):

    if "" == fact_keyword or "" == evidence_keyword:
        null_list = []
        for i in range(k + 1):
            null_list.append(0.0)
        return null_list
        # print "keyword is Null"

    fact_keyword_list = fact_keyword.split('/')
    evidence_keyword_list = evidence_keyword.split('/')

    #   加载模型
    # model = load_w2v_model()

    # 匹配总词数
    n = len(fact_keyword_list)
    # 最大总关联度
    total_relv = 0.0
    # 关联度列表
    relv_list = []
    # 返回列表：长度n+1，第一个元素是平均关联度，之后是从大到小的n个关联度
    return_list = []

    for fact_info in fact_keyword_list:
        if should_be_eliminate_keyword(fact_info):   # 根据既定规则筛选关键词
            continue
        fact_flag = fact_info.split('-')
        fact_word = fact_flag[0]     # 事实词语
        max_relv = 0.0  # 最大关联度
        if is_not_in_word_list(fact_word):  # 不在词库里的词语，不匹配
            n -= 1
            continue
        for evidence_info in evidence_keyword_list:
            if should_be_eliminate_keyword(evidence_info):  # 根据既定规则筛选词语
                continue
            evi_flag = evidence_info.split('-')
            evi_word = evi_flag[0]  # 证据词语
            if is_not_in_word_list(evi_word):   # 不在词库里的词语，不匹配
                continue
            relv = model.similarity(unicode(fact_word), unicode(evi_word))    # 计算事实词和证据词的关联度
            if relv > max_relv:
                max_relv = relv
        relv_list.append(max_relv)
        total_relv += max_relv

    if n == 0.0:
        ave_relv = 0.0
    else:
        ave_relv = total_relv / n

    relv_list = sort_list(relv_list)

    # 组装返回list
    return_list.append(ave_relv)
    for i in range(k):
        # print i
        if i < (len(relv_list) - 1):
            return_list.append(relv_list[i])
        else:
            return_list.append(0.0)

    return return_list


# 特征4：判断事实中的一些特定词语在证据中的出现度
# 特定词语的定义：具体的金额、具体的合同名字、具体的日期
# fact：事实段
# fact_divide：分词结果
# evidence：证据段
# 返回值：匹配总次数
def f4_num_of_special_word(fact, fact_divide, evidence):
    # 匹配次数
    match_num = 0
    # 拆分事实分词
    fact_divide_info = fact_divide.split('/')

    # print fact
    # print evidence

    # 定义pattern, 匹配书名号内的内容
    pattern = re.compile(u'《([^》]*)》')
    pattern_result_set = pattern.findall(fact)
    # 检查特定文件名在证据段中的重复度
    for result in pattern_result_set:
        ptn = re.compile(result)
        if ptn.search(evidence):
            match_num += 1
            # print result

    # 匹配日期、金钱
    i = 0
    temp_word = ""
    for fact_info in fact_divide_info:
        # print i, fact_info
        fact_and_flag = fact_info.split('-')
        fact_word = fact_and_flag[0]  # 事实词语
        fact_flag = fact_and_flag[1]  # 事实词性
        if i == 0 and ('m' in fact_flag):
            i += 1
            temp_word = fact_word
            continue
            # print i, temp_word
        if i > 0 and ('m' in fact_flag):
            i += 1
            temp_word += fact_word
        if i > 0 and ('m' not in fact_flag):
            i = 0
            # print temp_word
            ptn_num = re.compile(temp_word)
            if ptn_num.search(evidence):
                match_num += 1
    return match_num


# 从数据库中获取结果集
# result[0]:ID
# result[1]:文书编号
# result[2]:案由
# result[3]:事实原文
# result[4]:事实分词结果
# result[5]:事实关键词
# result[6]:证据
# result[7]:证据分词结果
# result[8]:证据关键词
# result[9]:事实是否被认定
def get_features_data():
    result_set = []

    conn = connect_db()
    cur = conn.cursor()

    sql_select_f_e_info = "SELECT * FROM bs.fact_evidence_info_sup"

    cur.execute(sql_select_f_e_info)
    result_set = cur.fetchall()

    cur.close()
    connect_close()

    return result_set


# 获得特征列表（二维）
# 一条特征格式：
# [f1, f2, f3_ave, f3_1, ..., f3_k, f4]
# 一条数据的特征数组长度为：k+4
def get_features_list(result_set, k):

    feature_list = []
    # result[0]:ID
    # result[1]:文书编号
    # result[2]:案由
    # result[3]:fact-事实原文
    # result[4]:fact_divide-事实分词结果
    # result[5]:fact_keyword-事实关键词
    # result[6]:evidence-证据
    # result[7]:evidence_divide证据分词结果
    # result[8]:evidence_keyword证据关键词
    # result[9]:事实是否被认定
    i = 0
    for result in result_set:
        i += 1
        print "data of feature", i
        single_data_feature = []
        # 提取特征
        f1 = f1_cal_fact_repeat_rate(result[4], result[6])
        f2 = f2_cal_divide_relevance(result[4], result[7])
        f3 = f3_cal_keyword_relevance(result[5], result[8], k)
        f4 = f4_num_of_special_word(result[3], result[4], result[6])
        # 组装特征
        single_data_feature.append(f1)
        single_data_feature.append(f2)
        for feature in f3:
            single_data_feature.append(feature)
        single_data_feature.append(f4)
        # 添加到特征列表里
        feature_list.append(single_data_feature)

    # print "data num:", len(feature_list)
    # for feature in feature_list:
    #     print feature

    return feature_list


# 获得特征列表（二维）
# 一条特征格式：
# [f1, f2, f3_ave, f3_1, ..., f3_k, f4]
# 一条数据的特征数组长度为：k+4
def get_features_list_for_demo(result_set, k=5):

    feature_list = []
    # result[0]:fact-事实原文
    # result[1]:fact_divide-事实分词结果
    # result[2]:fact_keyword-事实关键词
    # result[3]:evidence-证据
    # result[4]:evidence_divide-证据分词结果
    # result[5]:evidence_keyword-证据关键词
    i = 0
    for result in result_set:
        i += 1
        print "feature of fact&evidence", i
        single_data_feature = []
        # 提取特征
        f1 = f1_cal_fact_repeat_rate(result[1], result[3])
        f2 = f2_cal_divide_relevance(result[1], result[4])
        f3 = f3_cal_keyword_relevance(result[2], result[5], k)
        f4 = f4_num_of_special_word(result[0], result[1], result[3])
        # 组装特征
        single_data_feature.append(f1)
        single_data_feature.append(f2)
        for feature in f3:
            single_data_feature.append(feature)
        single_data_feature.append(f4)
        # 添加到特征列表里
        feature_list.append(single_data_feature)

    # print "data num:", len(feature_list)
    # for feature in feature_list:
    #     print feature

    return feature_list


# 获得标签列表
def get_labels_list(result_set):
    label_list = []
    # result[0]:ID
    # result[1]:文书编号
    # result[2]:案由
    # result[3]:fact-事实原文
    # result[4]:fact_divide-事实分词结果
    # result[5]:fact_keyword-事实关键词
    # result[6]:evidence-证据
    # result[7]:evidence_divide证据分词结果
    # result[8]:evidence_keyword证据关键词
    # result[9]:事实是否被认定
    i = 0
    for result in result_set:
        i += 1
        print "data of label", i
        label = float(result[9])
        label_list.append(label)

    # print "label num:", len(label_list)
    # for l in label_list:
    #     print l

    return label_list


if __name__ == '__main__':

    begin = datetime.datetime.now()

    # 按照四个模块顺序对xml进行处理
    # ===============1.数据收集+2.数据预处理===============
    file_path = unicode("F:\\MSYSTestFile\\", 'utf-8')
    filename = "1000015.xml"
    all_data = get_xml_data(file_path, filename)
    # 一个data内的构成方式：
    # [fact, fact_divide, fact_keyword, evidence, evidence_divide, evidence_keyword]
    # print "数据量：", len(all_data)
    # for data in all_data:
    #     print '='*30
    #     for ele in data:
    #         print ele
    # =====================3.特征提取=====================
    k = 5
    features_list = get_features_list_for_demo(all_data, k)
    for features in features_list:
        print features

    # result_set = get_features_data()
    # # for result in result_set:
    # #     print result[0], result[1], result[2], result[3], result[4], result[5], result[6]
    # print "len of result", len(result_set)
    #
    # k = 5

    # feature_list = get_features_list(result_set, k)
    # feature_path = 'F:\\bsfile\\features.pkl'
    # save_as_pkl(feature_list, feature_path)
    # for f in feature_list:
    #     print f

    # label_list = get_labels_list(result_set)
    # label_path = 'F:\\bsfile\\labels.pkl'
    # save_as_pkl(label_list, label_path)

    # feature_list_supplement = get_features_list(result_set, k)
    # feature_path_supplement = 'F:\\bsfile\\features_supplement.pkl'
    # save_as_pkl(feature_list_supplement, feature_path_supplement)
    #
    # label_list_supplement = get_labels_list(result_set)
    # label_path_supplement = 'F:\\bsfile\\labels_supplement.pkl'
    # save_as_pkl(label_list_supplement, label_path_supplement)

    # result[0]:ID
    # result[1]:文书编号
    # result[2]:案由
    # result[3]:事实原文
    # result[4]:事实分词结果
    # result[5]:事实关键词
    # result[6]:证据
    # result[7]:证据分词结果
    # result[8]:证据关键词
    # result[9]:事实是否被认定
    # for result in result_set:
    #     f1 = f1_cal_fact_repeat_rate(result[4], result[6])
    #     print f1
    #     f2 = f2_cal_divide_relevance(result[4], result[7])
    #     # print f4_num_of_special_word(result[3], result[4], result[6])
    #     f3 = f3_cal_keyword_relevance(result[5], result[8], 5)
    #
    # print "f2 =", f2
    # print "f3 =", f3

    end = datetime.datetime.now()
    runtime = end - begin
    print "运行时间：", runtime
