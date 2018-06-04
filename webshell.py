# -*- coding:utf-8 -*-
import re
import os


'''
def get_file():
    list_files_name = []
    list_files_data = []
    filepath = 'F:\office day\code\python\webshell\data'
    filename_list = listdir(filepath)
    print(filename_list)
'''



def get_file1(filepath):
    rule_data,rule_id = read_list()
    list_files_name = []
    list_files_data = []
    for root, dirs, files in os.walk(filepath, topdown=False):
        for name in files:
            if name.endswith('php'):                                           #筛选php文件
                #print(os.path.join(root,name))
                filename = (os.path.join(root,name))                           #获取所有文件名称跟路径
                #print(name)
                list_files_name.append(filename)
    for list_data_s in list_files_name:
        with open(list_data_s, 'r',encoding='UTF-8') as f:                  #读取所有php
            try:
                while True:
                    lines = next(f, None)
                    if lines is None:
                        break
                    #print(list_data_s)
                    list_files_data.append(lines+"@_@"+list_data_s)
            except:
                pass
    for i,c in zip(rule_data,rule_id):
        for q in i:
            if q ==None:
                break
            file_data = str(q)
            for bbs in (list_files_data):
                arr = bbs.split('@_@')                                      #切割------分类文件路径跟匹配内容
                line = arr[0]                                                #匹配内容
                file_name = arr[1]                                           #匹配文件路径
                search_data = re.search(file_data,line)                      #正则匹配文件内容
                if search_data is not None:
                    list_a_data = search_data,c,file_name
                    print(list_a_data)



def read_list():
    rule_data = []
    rule_id   = []
    re_rule_data = 'allchar="1">(.*)</rule>'
    re_rule_id = 'rule_id="(.*)"\sscore'
    with open('webshell_rule.xml',"r") as f:
        while True:
            line = next(f, None)
            if line is None:
                break
            aa = re.findall(re_rule_data,line)
            bb = re.findall(re_rule_id, line)
            rule_data.append(aa)
            rule_id.append(bb)
    return rule_data,rule_id





if __name__=='__main__':
    rootdir = 'F:\office day\code\python\webshell\data'
    get_file1(rootdir)