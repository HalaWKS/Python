# -*- coding: UTF-8 -*-

import jieba.posseg as jbps
from util import list_to_string
from find_key_word import get_key_word_list

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


# 拆分一条证据
def divide_a_evidence(str0):
    result_set = jbps.cut(str0)
    return result_set


# 获得拆分的List
def get_divide_list(str0):
    result_set = divide_a_evidence(str0)
    divide_list = []
    for word in result_set:
        # 去掉标点
        if 'x' in word.flag:
            continue
        divide_list.append(word.word + '-' + word.flag)
    return divide_list


# 获得拆分的结果(字符串形式)
def get_divide_result(evidence):
    divide_result = list_to_string(get_divide_list(evidence))
    return divide_result


# 获得证据的关键字(字符串形式)
def get_evidence_keyword(evidence):
    key_word_result = list_to_string(get_key_word_list(evidence))
    return key_word_result

if __name__ == '__main__':
    evidence = "原告孟庆营对其陈述事实在举证期限内提供的证据有：1、2013年11月9日欠条一份。原告孟庆营认为该份证据能够证实被告甘元元当天到其家购猪，欠其购猪价款12850元。2、2014年4月9日欠条一份。原告孟庆营认为该份证据能够证实被告于记华和甘元元共同合伙到其家购猪，欠其购猪款11200元。以上事实有欠条、当事人陈述等在卷为证，足以证实。"

    print get_divide_result(evidence)
    print get_evidence_keyword(evidence)
