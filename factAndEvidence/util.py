# -*- coding: UTF-8 -*-

from gensim.models import word2vec

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def load_w2v_model():
    path = 'F:\\bsfile\\w2v.model'
    model = word2vec.Word2Vec.load(path)
    return model


def delete_space(string0):
    string0 = string0.replace(" ", "")
    return string0


def list_to_string(list0):
    string0 = ""
    lenth0 = len(list0)
    i = 0
    for element in list0:
        string0 += str(element)
        if i != (lenth0-1):
            string0 += '/'
        i += 1
    return string0


# 把一串分词结果拆分成words_list
def divide_to_words(result_list):
    words_list = []
    a_sentence_word = []
    for divide_result in result_list:
        # 拆分一句话的分词结果，word_info是“词语-词性”对
        word_info_list = divide_result[0].split('/')
        for word_info in word_info_list:
            # word_and_chara[0]是词语
            word_and_chara = word_info.split('-')
            # 一句话是一个list
            a_sentence_word.append(word_and_chara[0])
        # 把一句话的分词结果作为一个元素，放入words_list里
        words_list.append(a_sentence_word)
        a_sentence_word = []

    return words_list


# 对列表进行排序
def sort_list(my_list):
    for i in range(len(my_list) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(my_list) - i - 1):  # ｊ为列表下标
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


if __name__ == '__main__':
    model = load_w2v_model()
    word_list = []
    for k, v in model.wv.vocab.items():
        word_list.append(k)
    print len(word_list)
    print "sssss" not in word_list
    # print len(model.wv.vocab.items())
    # print u"原告" in model.wv.vocab.items()[0]
    # for i in range(10):
    #     print model.wv.vocab.items()[i][0]
    # print len(model[u'原告'])
    # word_list = model.vocab.items()
    # print len(word_list)
    # list0 = [3, 6, 7, 3, 1, 2, 9, 8, 5]
    # list0 = sort_list(list0)
    # print list0
    # string0 = list_to_string(list0)
    # print string0
    # list0 = ["原告", "被告", "我"]
    # print "原告" in list0
