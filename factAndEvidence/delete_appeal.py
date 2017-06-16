# -*- coding: UTF-8 -*-


def delete_appeal(facts, filename="testfile"):

    i = 0
    facts_after_delete = []

    # print "This is", filename

    for fact in facts:
        if ("判令" in fact) or ("判决" in fact) or ("请求" in fact) or ("故诉至法院" in fact):
            break
        facts_after_delete.append(fact)
        i += 1

    return facts_after_delete;


if __name__ == '__main__':
    fact_all = "原告广德公司诉称：原、被告分别于2012年12月17日、2013年1月9日签订两份《机械设备租赁合同》，合同约定由被告向原告租赁SD16湿地推土机两台、SD16干地推土机两台，用于被告在安徽宣城洪林的工地施工，合同对租赁期限、租金、违约金等均做了约定。合同签订后，原告按合同约定向被告提供了机械设备，而被告未能按合同约定支付租金，故诉至法院。请示判令被支付租金62692元、违约金27857元，共计90549元。诉讼费用由被告承担。"
    facts = fact_all.split("。")

    print "================================="
    i = 0
    for fact in facts:
        i += 1
        print i, ".", fact
    print "================================="
    facts = delete_appeal(facts)
    i = 0
    for fact in facts:
        i += 1
        print i, ".", fact
