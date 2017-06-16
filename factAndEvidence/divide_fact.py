# -*- coding: UTF-8 -*-

import jieba.posseg as jbps


def divide_sentence(str0):
    result_set = jbps.cut(str0)
    return result_set


def get_divide_list(str0):
    result_set = divide_sentence(str0)
    divide_list = []
    for word in result_set:
        # 去掉标点
        if 'x' in word.flag:
            continue
        divide_list.append(word.word + '-' + word.flag)
    return divide_list


if __name__ == '__main__':
    str1 = "原告诉称，原、被告于2011年9月5日在岳池县双鄢乡人民政府协议离婚，离婚协议对夫妻财产约定：“1、武装部旁边一套面积300.54平方米的住房属于男方所有（因房屋有贷款三年后所有权归男方），其它所有财产属女方所有；2、凡由夫妻双方签字认可的所有欠债由女方承担，所有房屋贷款由女方承担，其于借款谁借谁还"
    divide_list = get_divide_list(str1)

    for element in divide_list:
        print element
