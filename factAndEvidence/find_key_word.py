# -*- coding: UTF-8 -*-

import jieba.analyse as jban

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 关键字提取(带权重)
def get_key_word_list(fact):

    key_words_list = []

    key_words = get_key_word_generator(fact)

    for x, w in key_words:
        key_words_list.append(x + '-' + str(w))
        # print('%s %s' % (x, w))

    return key_words_list


# 关键字提取(不带权重)
def get_key_word_without_weight(sentence):
    key_words_list = []
    key_words = get_key_word_generator(sentence)

    for x, w in key_words:
        key_words_list.append(x)

    return key_words_list


def get_key_word_generator(fact):
    key_words = jban.textrank(fact, withWeight=True)
    return key_words


if __name__ == '__main__':
    str0 = "C罗在禁区内接到本泽马直传后背身分球到中路禁区线附近，本泽马跟上一脚推射被奥布拉克神勇挡出。"
    key_words = get_key_word_list(str0)

    for key_word in key_words:
        print key_word
