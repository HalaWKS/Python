# encoding=utf-8
# 语料库测试

from gensim.models import word2vec

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def test(path):
    model = word2vec.Word2Vec.load(path)

    xsd = model.similarity(u"欠款", u"欠条")
    print xsd

    # for item in model.most_similar(u'借款', topn=10):
    #     print item[0], item[1]

if __name__ == '__main__':
    path = 'F:\\bsfile\\w2v.model'
    test(path)
