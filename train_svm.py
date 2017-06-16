# encoding=utf-8
import cPickle as pickle
import numpy as np

from datetime import datetime
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

feature_list = pickle.load(open('features_small.pkl', 'r'))
label_list = pickle.load(open('labels_small.pkl', 'r'))

# 可使用k折交叉验证
features_train, features_test, labels_train, labels_test = \
    cross_validation.train_test_split(np.array(feature_list), np.array(label_list), test_size=0.1, random_state=42)

# 自动调整至最佳参数
# parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
# clf = grid_search.GridSearchCV(SVC(), parameters)

clf = SVC(kernel="rbf", C=1000)
print 'start fitting ' + str(datetime.now())
clf.fit(features_train, labels_train)
print 'start predicting ' + str(datetime.now())
pred = clf.predict(features_test)
print accuracy_score(pred, labels_test)
pickle.dump(clf, open('svm_model.pkl', 'w'))

# lda
# 10000条, kernel="rbf"   , C=1000, 0.617
# word2vec
# 10000条, kernel="rbf"   , C=1000, 0.561
# 10000条, kernel="rbf"   , C=100 , 0.558
# 10000条, kernel="linear", C=1000, 0.534
# 10000条, kernel="linear", C=100 , 0.535
# word2vec + lda
# 10000条, kernel="rbf"   , C=1000, 0.689
# 10000条, kernel="rbf"   , C=100 , 0.655
# 10000条, kernel="rbf"   , C=10  , 0.598
# 10000条, kernel="rbf"   , C=1   , 0.59
# 10000条, kernel="linear", C=1000, 0.59
# 10000条, kernel="linear", C=100 , 0.589
# 10000条, kernel="linear", C=10  , 0.588
# 10000条, kernel="linear", C=1   , 0.582
# word2vec + lda + 重复词
# 10000条, kernel="rbf"   , C=1000, 0.63
# 10000条, kernel="rbf"   , C=100 , 0.632
# 10000条, kernel="linear", C=1000, 0.593