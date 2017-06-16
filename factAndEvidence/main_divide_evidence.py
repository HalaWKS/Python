# -*- coding: UTF-8 -*-

from connect_mysql import connect_db
from connect_mysql import connect_close
from save_evidence_info import save_evidence_info
from get_evidence import get_evidence

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':

    begin = datetime.datetime.now()

    # TODO
    connect_db()

    result_set = get_evidence()
    save_evidence_info(result_set)

    connect_close()

    end = datetime.datetime.now()
    runtime = end - begin
    print "运行时间：", runtime
