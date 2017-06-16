# -*- coding: UTF-8 -*-
# 获取特征

from gensim.models import word2vec
import re
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    # l = [[1, 2], [3, 4], [5, 6]]
    # print len(l)
    # print unicode('\xe5\x8d\x97\xe9\x80\x9a')
    path = 'F:\\bsfile\\w2v.model'
    model = word2vec.Word2Vec.load(path)
    word_list = []
    for k, v in model.wv.vocab.items():
        word_list.append(k)
    for word in word_list:
        if word == '南通':
            print 'have', word
    # 定义pattern
    # pattern = re.compile(u'《([^》]*)》')
    #
    # str = u"原告文登市农村《信用合作联社》高村信用社诉称，原告与五被告于2009年3月31日签订《文高农信高保借字2009第045号》及文高农信借字2009第045借款合同，借款金额200，000元，贷款月利率6．75‰"
    #
    # results = pattern.findall(str)
    #
    # for result in results:
    #     print result

