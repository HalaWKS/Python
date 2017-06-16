# -*- coding: UTF-8 -*-

from divide_fact_test import divide_sentence
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 去掉重复的词
def delete_duplicate_word(result_set):

    new_result_set = []
    exist = False

    for result in result_set:
        for new_result in new_result_set:
            if result.word == new_result.word:
                exist = True
                break
        if exist:
            exist = False
            continue
        new_result_set.append(result)

    return new_result_set


def should_be_delete(flag):
    # c-连词; d-副词; f-方位词; p-介词; r-代词; u-助词; x-标点;
    if ('c' in flag) or ('d' in flag) or ('f' in flag) \
            or ('p' in flag) or ('r' in flag) or ('u' in flag) or ('x' in flag):
        return True
    return False


def get_match_rate(fact, fact_identify):

    # “认定事实段”的长度过短，认为描述为“经审理查明，确认原告所述事实属实。”此类，直接予以认定
    if len(fact_identify) <= 60:
        return 1

    i = 0.0
    n = 0.0

    result_set = divide_sentence(fact)

    # 去重复词
    result_set = delete_duplicate_word(result_set)

    for result in result_set:

        # 不匹配一些无意义的词
        if should_be_delete(result.flag):
            continue

        # 正则匹配
        pattern = re.compile(result.word)
        is_match = pattern.search(fact_identify)
        n += 1
        if is_match:
            i += 1
            print result.word, result.flag, is_match.group()
        else:
            print result.word, result.flag, is_match

    rate = i / n

    print "匹配词数：", i
    print "总词数：", n
    print "匹配率：", rate

    return rate

    # if rate > 0.5:
    #     return True
    # else:
    #     return False

    # return False

if __name__ == '__main__':
    str1 = "原告诉称，他和被告于2011年9月5日在岳池县双鄢乡人民政府协议离婚，离婚协议对夫妻财产约定：“1、武装部旁边一套面积200平方米的住房属于男方所有（因房屋有贷款三年后所有权归男方），其它所有财产属女方所有；2、凡由夫妻双方签字认可的所有欠债由女方承担，所有房屋贷款由女方承担，其于借款谁借谁还"
    # str1 = str1.decode('utf8')
    str2 = "经审理查明：原、被告2009年12月24日在岳池县双鄢乡人民政府办理结婚登记（结婚证字号川［2009］广岳双结字3000073）。2011年9月5日签订离婚协议并办理离婚登记（离婚证字号川［2001］广岳双离字010），订立离婚协议的主要内容“一、子女抚养问题……；二、双方财产分割：武装部旁有一套面积200平方米住房属男方所有（因房屋有贷款三年后所有权归男方），其它所有财产（房子、车子、投资股权）属女方所有；三、债权债务：凡由夫妻双方签字认可的所有欠债由女方承担，所有房屋的贷款由女方承担，其于借款谁借谁还；四、离婚后双方互不干扰对方的生活，要尊重对方的隐私”。2011年12月29日原、被告在岳池县民政局办理结婚登记（结婚证字号J511621-2011-004154）。2012年1月9日双方签订离婚协议并在岳池县民政局办理离婚登记（L511621-2012-000014），订立离婚协议如下：“一、男、女双方自愿离婚；二、子女抚养：共同生育一女成某乙和一子李某乙由女方抚养，男方不支付任何费用；三、共同财产的处理：婚后男女双方的共同房产、车产、股权、投资都归女方所有；四、共同债权的处理：婚后男女双方共同债权由女方分享；五、共同债务的处理：男女双方共同债务由女方承担；六、夫妻共同存款处理：婚后双方共同存款归女方享有”。原、被告在婚姻关系存续期间，于2011年2月28日共同承诺自愿用自有门市座落岳池县九龙镇白塔路及新风路交叉2层（产权号为00080195，面积304．3平方米）及自有住房座落于岳池县九龙镇文兴街1号5-1号住宅一套（产权号为00080150，面积201．5平方米）作抵押，以被告成某甲为借款人、原告李某甲为借款担保人，向贷款人岳池县农村信用合作联社同兴信用社申请个人贷款。2011年4月8日成某甲与岳池县农村信用合作联社同兴信用社就以上门市及房产为抵押物签订了抵押合同（合同编号：2011年岳信同个借［2011］77字001号），并进行了抵押登记。2011年4月10日，贷款人岳池县农村信用合作联社向借款人及本案被告成某甲放贷柒拾万元整。位于岳池县九龙镇文兴街1号5-1号（岳池县房权证岳字第00080150号），登记时间是2011年1月5日，建筑面积201．5平方米，房屋所有权人成某甲。"
    str2 = str2.decode('utf8')
    # result_set = divide_sentence(str1)

    print get_match_rate(str1, str2)

