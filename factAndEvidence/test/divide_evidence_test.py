# -*- coding: UTF-8 -*-

import jieba
import jieba.posseg as jbps
import jieba.analyse as jban

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def divide_evidence(str):
    result_set = jbps.cut(str, HMM=False)
    return result_set


def delete_useless_words(result_set):
    return result_set

if __name__ == '__main__':
    print None
