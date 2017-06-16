# -*- coding: UTF-8 -*-

import os


#   获取文件列表
def get_files(file_path):

    path_dir = os.listdir(file_path)

    return path_dir


if __name__ == '__main__':

    filepath = "F:\\南京大学\\毕设\\共享文书\\Test"
    filepath_utf8 = unicode(filepath, 'utf-8')

    print(filepath_utf8)

    i = 0;
    files = get_files(filepath_utf8);
    for file in files:
        i += 1;
        print(file);

    print "There are", i, "files";
#     python的print会给每个元素之间自动添加空格
