#!/usr/bin/python2.7
#coding:gbk

import re

rule='gzdeflate|gzcompress|gzencode'


#�˲���������б� (['�ļ�·��'],['��������'])
whitefilter=[]


def Check(filestr,filepath):

    result = re.search(rule,filestr)

    try:
        if result.group():
            if '���' in filestr and 'unix2DosTime' in filestr:
                isok = 1
                for white in whitefilter:
                    if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:
                        isok=0
                if isok:
                    return (('�ݲ��ṩ',),),'PHP �ļ�������ų���'
    except:
        pass
    return None
