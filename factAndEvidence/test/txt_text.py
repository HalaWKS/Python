# -*- coding: UTF-8 -*-

import MySQLdb
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':

    content = []
    content.append('1')
    content.append('2')
    content.append('3')

    file_object = open('F:\\bsfile\\fact_evidence_data.txt', 'w')
    for con in content:
        file_object.write(con+'\n')
    file_object.close()
