# encoding=utf-8

import cPickle as pickle
from gensim.models import word2vec
from pickle_operate import restructure_pkl

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 训练语料库
def train_model(words_list, save_path):
    # 参数：
    # 单词集合;
    # 少于min_count次数的单词会被丢弃掉;
    # 神经网络的隐藏层的单元数;
    model = word2vec.Word2Vec(words_list, min_count=10, size=300, iter=15)

    model.save(save_path)

if __name__ == '__main__':

    begin = datetime.datetime.now()

    words_list_path = 'F:\\bsfile\\corpus_data.pkl'
    save_path = 'F:\\bsfile\\w2v.model'

    words_list = restructure_pkl(words_list_path)
    print len(words_list)
    # for i in range(0, 10):
    #     print words_list[i]
    train_model(words_list, save_path)

    end = datetime.datetime.now()

    runtime = end - begin

    print "运行时间：", runtime
