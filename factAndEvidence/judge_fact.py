# -*- coding: UTF-8 -*-

from divide_fact import divide_sentence

import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def delete_duplicate_word(result_set):

    new_result_set = []
    exist = False

    for result in result_set:
        for new_result in new_result_set:
            if result.word == new_result.word:
                exist = True
                break
        if exist:
            exist = False
            continue
        new_result_set.append(result)

    return new_result_set


def should_be_delete(flag):
    # c-连词; d-副词; f-方位词; p-介词; r-代词; u-助词; x-标点;
    if ('c' in flag) or ('d' in flag) or ('f' in flag) \
            or ('p' in flag) or ('r' in flag) or ('u' in flag) or ('x' in flag):
        return True
    return False


# 判断事实是否能被认定
def get_match_rate(fact, fact_identify):

    # print "诉称", fact
    # print "认定事实", fact_identify

    # “认定事实段”的长度过短，认为描述为“经审理查明，确认原告所述事实属实。”此类，直接予以认定
    if len(fact_identify) <= 60:
        return 1.0

    i = 0.0
    n = 0.0

    result_set = divide_sentence(fact)

    # 去重复词
    result_set = delete_duplicate_word(result_set)

    for result in result_set:

        # 不匹配一些无意义的词
        if should_be_delete(result.flag):
            continue

        # 正则匹配
        pattern = re.compile(result.word)
        is_match = pattern.search(fact_identify)
        n += 1
        if is_match:
            i += 1
        #     print result.word, is_match.group(), i, n
        # else:
        #     print result.word, is_match, i, n

    # print i, n
    rate = i / n

    # print "匹配词数：", i
    # print "总词数：", n
    # print "匹配率：", rate

    return rate


def judge_relevance(match_rate):
    if match_rate > 0.4:
        return True
    else:
        return False
