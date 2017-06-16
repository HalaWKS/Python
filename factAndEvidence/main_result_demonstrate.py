# -*- coding: UTF-8 -*-

from save_xml_db import get_xml_data
from get_features import get_features_list_for_demo
from pickle_operate import restructure_pkl

import datetime
import sys
import get_features
reload(sys)
sys.setdefaultencoding('utf8')


def print_line():
    print '='*100


if __name__ == '__main__':
    begin = datetime.datetime.now()

    # 按照四个模块顺序对xml进行处理
    # ===============1.数据收集+2.数据预处理===============
    file_path = unicode("F:\\MSYSTestFile\\", 'utf-8')
    filename = "1133184.xml"
    all_data = get_xml_data(file_path, filename)
    labels = []
    for data in all_data:
        labels.append(data[6])
    # 一个data内的构成方式：
    # [fact, fact_divide, fact_keyword, evidence, evidence_divide, evidence_keyword, is_identified]
    # print "数据量：", len(all_data)
    # for data in all_data:
    #     print '='*30
    #     for ele in data:
    #         print ele
    # =====================3.特征提取=====================
    k = 5
    features_list = get_features_list_for_demo(all_data, k)
    # for features in features_list:
    #     print features
    # ====================4.分类器预测====================
    # TODO
    clf_svm_path_all_feature = 'F:\\bsfile\\clf_svm_all_feature.pkl'
    clf = restructure_pkl(clf_svm_path_all_feature)
    pred = clf.predict(features_list)
    # =====================5.结果输出=====================
    print filename
    print_line()
    print "证据："
    print all_data[0][3]
    for i in range(0, len(all_data)):
        print_line()
        print all_data[i][0]
        print "是否能被证实：", all_data[i][6]
        print "预测证实情况：", pred[i]
    print_line()
    # ===================================================
    end = datetime.datetime.now()
    runtime = end - begin
    print "运行时间：", runtime
