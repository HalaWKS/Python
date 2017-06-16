# encoding=utf-8

import cPickle as pickle

from get_divide_result import get_result_of_evidence
from get_divide_result import get_result_of_fact
from util import divide_to_words

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 将数据保存成.pkl
def save_as_pkl(my_list, path):
    output = open(path, 'w')
    pickle.dump(my_list, output)
    output.close()


# 读取.pkl文件
def restructure_pkl(path):
    pkl_file = open(path, 'r')
    data = pickle.load(pkl_file)
    return data

if __name__ == '__main__':

    begin = datetime.datetime.now()

    feature_path = 'F:\\bsfile\\features.pkl'
    label_path = 'F:\\bsfile\\labels.pkl'

    features = restructure_pkl(feature_path)
    print "features length", len(features)

    # for feature in features:
    #     print feature

    labels = restructure_pkl(label_path)
    print "labels length", len(labels)

    for label in labels:
        print label

    # =============================
    # my_list = [1, 2, 3, 4]
    # path = 'F:\\bsfile\\test_data.pkl'
    # save_as_pkl(my_list, path)
    # load_list = restructure_pkl(path)

    # fact_words_list = divide_to_words(get_result_of_fact())
    # evidence_words_list = divide_to_words(get_result_of_evidence())
    #
    # words_list = fact_words_list + evidence_words_list
    #
    # print "length of fact_words_list", len(fact_words_list)
    # print "length of evidence_words_list", len(evidence_words_list)
    # print "length of all", len(words_list)
    #
    # path = 'F:\\bsfile\\corpus_data.pkl'
    # save_as_pkl(words_list, path)
    #
    # load_list = restructure_pkl(path)
    # print "length of load_list", len(load_list)

    # =============================

    end = datetime.datetime.now()
    runtime = end - begin

    print "运行时间：", runtime
