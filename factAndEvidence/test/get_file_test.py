# -*- coding: UTF-8 -*-

import os


#   获取文件列表
def get_files(file_path):

    path_dir = os.listdir(file_path)

    return path_dir
