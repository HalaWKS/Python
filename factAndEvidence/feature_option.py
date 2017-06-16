# -*- coding: UTF-8 -*-
#  获取特征

from pickle_operate import save_as_pkl
from pickle_operate import restructure_pkl

import re
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 获取特征
def get_feature(feature_path):
    features = restructure_pkl(feature_path)
    return features


# 被认定数量
def num_of_true(features, labels):
    i = 0
    for label in labels:
        if label == 1:
            i += 1
    print "认定数：", i
    return i


# 不认定数量
def num_of_false(features, labels):
    i = 0
    for label in labels:
        if label == 0:
            i += 1
    print "不认定数：", i
    return i


# 获取标签
def get_label(label_path):
    labels = restructure_pkl(label_path)
    return labels


# 获取label=0, label=1数量一样的feature和label列表
def get_same_feature_label(features, labels):
    new_features = []
    new_labels = []

    # 事实不可被认定数量
    # label_0_num = 0
    # for label in labels:
    #     if label == 0:
    #         label_0_num += 1
    # print "事实不可被认定数量：", label_0_num

    for i in range(len(features)):
        # 先添加所有label = 0的
        if labels[i] == 0:
            new_features.append(features[i])
            new_labels.append(labels[i])

    print "事实不可被认定数量：", len(new_features)

    judge_false = len(new_features)
    flag = 0

    for j in range(len(features)):
        if flag < judge_false and labels[j] == 1:
            new_features.append(features[j])
            new_labels.append(labels[j])
            flag += 1

    return new_features, new_labels


# 获取正则类特征
# feature[0], feature[8]
def get_regular_feature(features):
    regular_features = []
    for feature in features:
        regular_feature = [feature[0], feature[8]]
        regular_features.append(regular_feature)
    return regular_features


# 获取w2v类特征
# feature[1], feature[2], feature[3], feature[4], feature[5], feature[6], feature[7]
def get_w2v_feature(features):
    w2v_features = []
    for feature in features:
        w2v_feature = [feature[1], feature[2], feature[3], feature[4],
                       feature[5], feature[6], feature[7]]
        w2v_features.append(w2v_feature)
    return w2v_features

if __name__ == '__main__':
    begin = datetime.datetime.now()

    print "开始时间：", begin

    # ================================================

    old_feature_path = 'F:\\bsfile\\features.pkl'
    old_label_path = 'F:\\bsfile\\labels.pkl'
    new_feature_path = 'F:\\bsfile\\features_3482.pkl'
    new_label_path = 'F:\\bsfile\\labels_3482.pkl'
    sup_feature_path = 'F:\\bsfile\\features_supplement.pkl'
    sup_label_path = 'F:\\bsfile\\labels_supplement.pkl'
    all_feature_path = 'F:\\bsfile\\features_all.pkl'
    all_label_path = 'F:\\bsfile\\labels_all.pkl'
    regular_feature_path = 'F:\\bsfile\\features_regular.pkl'
    w2v_feature_path = 'F:\\bsfile\\features_w2v.pkl'

    w2v_features = restructure_pkl(w2v_feature_path)
    regular_features = restructure_pkl(regular_feature_path)

    print "w2v:", len(w2v_features)
    print "正则:", len(regular_features)

    for i in range(10):
        print w2v_features[i]
    print '=' * 50
    for j in range(10):
        print regular_features[i]

    # all_features = restructure_pkl(all_feature_path)
    # print "全部特征数：", len(all_features)
    #
    # w2v_features = get_w2v_feature(all_features)
    # print "w2v特征数：", len(w2v_features)
    # save_as_pkl(w2v_features, w2v_feature_path)

    # for i in range(10):
    #     print w2v_features[i]

    # regular_features = get_regular_feature(all_features)
    # print "正则特征数：", len(regular_features)
    # save_as_pkl(regular_features, regular_feature_path)

    # features_old = get_feature(old_feature_path)
    # labels_old = get_label(old_label_path)
    #
    # print "旧特征数：", len(features_old)
    # print "旧标签数：", len(labels_old)
    # num_of_true(features_old, labels_old)
    # num_of_false(features_old, labels_old)
    #
    # features_sup = get_feature(sup_feature_path)
    # labels_sup = get_label(sup_label_path)
    #
    # print "补充特征数：", len(features_sup)
    # print "补充标签数：", len(labels_sup)
    # num_of_true(features_sup, labels_sup)
    # num_of_false(features_sup, labels_sup)
    #
    # features_all = features_old + features_sup
    # labels_all = labels_old + labels_sup
    #
    # print "全部特征数：", len(features_all)
    # print "全部标签数：", len(labels_all)
    # num_of_true(features_all, labels_all)
    # num_of_false(features_all, labels_all)
    #
    # save_as_pkl(features_all, all_feature_path)
    # save_as_pkl(labels_all, all_label_path)

    # features = get_feature(feature_path)
    # labels = get_label(label_path)
    #
    # a = get_same_feature_label(features, labels)
    # new_features = a[0]
    # new_labels = a[1]

    # print len(new_features), len(new_labels)
    # print "认定：", num_of_true(new_features, new_labels)
    # print "不认定：", num_of_false(new_features, new_labels)

    # for i in range(10):
    #     print new_features[i]
    #     print new_labels[i]

    # save_as_pkl(new_features, new_feature_path)
    # save_as_pkl(new_labels, new_label_path)

    # ================================================

    end = datetime.datetime.now()
    runtime = end - begin

    print "运行时间：", runtime

