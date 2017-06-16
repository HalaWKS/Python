# -*- coding: UTF-8 -*-
#  朴素贝叶斯分类器
import cPickle as pickle
import numpy as np
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from pickle_operate import restructure_pkl
from feature_option import num_of_false
from feature_option import num_of_true

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    begin = datetime.datetime.now()

    print "开始时间：", begin

    feature_path = 'F:\\bsfile\\features.pkl'
    label_path = 'F:\\bsfile\\labels.pkl'
    clf_nb_path = 'F:\\bsfile\\clf_nb.pkl'
    clf_nb_path_equal_feature = 'F:\\bsfile\\clf_nb_equal_feature.pkl'
    clf_nb_path_all_feature = 'F:\\bsfile\\clf_nb_all_feature.pkl'
    clf_nb_path_regular_feature = 'F:\\bsfile\\clf_nb_regular_feature.pkl'
    clf_nb_path_w2v_feature = 'F:\\bsfile\\clf_nb_w2v_feature.pkl'
    new_feature_path = 'F:\\bsfile\\features_3482.pkl'
    new_label_path = 'F:\\bsfile\\labels_3482.pkl'
    all_feature_path = 'F:\\bsfile\\features_all.pkl'
    all_label_path = 'F:\\bsfile\\labels_all.pkl'
    regular_feature_path = 'F:\\bsfile\\features_regular.pkl'
    w2v_feature_path = 'F:\\bsfile\\features_w2v.pkl'

    print "朴素贝叶斯"
    print "特征：w2v+正则"

    features = restructure_pkl(all_feature_path)
    print "features length", len(features)

    labels = restructure_pkl(all_label_path)
    print "labels length", len(labels)

    # 获取等量的特征
    # features_labels = get_same_feature_label(features, labels)
    # new_features = features_labels[0]
    # new_labels = features_labels[1]

    # 可使用k折交叉验证
    features_train, features_test, labels_train, labels_test = \
        cross_validation.train_test_split(np.array(features), np.array(labels), test_size=0.1, random_state=42)

    # 显示训练集里，认定和不认定的数量
    print "训练集："
    train_true = num_of_true(features_train, labels_train)
    train_false = num_of_false(features_train, labels_train)

    # 显示测试集里，认定和不认定的数量
    print "测试集："
    test_true = num_of_true(features_test, labels_test)
    test_false = num_of_false(features_test, labels_test)

    clf = GaussianNB()
    clf.fit(features_train, labels_train)

    # 加载已保存的模型
    # clf = restructure_pkl(clf_nb_path_all_feature)

    pred = clf.predict(features_test)
    print "准确率：", accuracy_score(pred, labels_test)

    # 召回率和精确率计算
    recall = 0.0
    precision = 0.0
    true_positive = 0.0
    false_negative = 0.0
    false_positive = 0.0
    for i in range(0, len(pred)):
        # 猜测为认定，且确实为认定，成功被检索数+1
        if pred[i] == 1.0 and labels_test[i] == 1.0:
            true_positive += 1
        # 猜测为认定，实际却是不认定，检索失败数+1
        if pred[i] == 1.0 and labels_test[i] == 0.0:
            false_positive += 1
        # 猜测为不认定，但实际为认定，猜测“被认定”失败数+1
        if pred[i] == 0.0 and labels_test[i] == 1.0:
            false_negative += 1

    recall = true_positive / (true_positive + false_negative)
    precision = true_positive / (true_positive + false_positive)

    print "召回率：", recall
    print "精确率：", precision

    # 保存训练的模型
    # pickle.dump(clf, open(clf_nb_path, 'w'))
    pickle.dump(clf, open(clf_nb_path_all_feature, 'w'))

    end = datetime.datetime.now()
    runtime = end - begin

    print "运行时间：", runtime

