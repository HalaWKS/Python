# -*- coding: UTF-8 -*-

import jieba
import jieba.posseg as jbps
import jieba.analyse as jban

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def add_freq_word():
    jieba.suggest_freq('原告', True)
    jieba.suggest_freq('诉称', True)


def divide_sentence(str):
    result_set = jbps.cut(str, HMM=False)
    return result_set


if __name__ == '__main__':

    str0 = "我们中出了一个叛徒"
    str1 = "原告诉称，原、被告于2011年9月5日在岳池县双鄢乡人民政府协议离婚，离婚协议对夫妻财产约定：“1、武装部旁边一套面积200平方米的住房属于男方所有（因房屋有贷款三年后所有权归男方），其它所有财产属女方所有；2、凡由夫妻双方签字认可的所有欠债由女方承担，所有房屋贷款由女方承担，其于借款谁借谁还"
    str2 = "……"

    # jieba.suggest_freq('原告', True)

    print('='*40)

    words = divide_sentence(str2)

    result = []

    for word in words:
        result.append(word.word + '-' + word.flag)
        print word.word, word.flag
        # print word

    [r.encode('utf8') for r in result]
    print result

    # for r in result:
    #     print r

    print('='*40)

    key_word = []

    key_words = jban.textrank(str1, withWeight=True)
    for x, w in key_words:
        key_word.append(x + '-' + str(w))
        print('%s %s' % (x, w))

    print key_word

    for word in key_word:
        print word
