#!/usr/bin/python2.7
#coding:gbk

import re

keywords=[
            '�����Զ�����',
            'xxddos',
            'phpddos',
            'fsockopen("udp:',
            'fsockopen("tcp:',
            '$_get["moshi"]=="udp"'
        ]


#�˲���������б� (['�ļ�·��'],['��������'])
whitefilter=[
                (['install/svinfo.php'],['fsockopen("tcp:']),
]


def Check(filestr,filepath):

    filestr = filestr.lower()

    #���ؼ��ʲ���-�ݲ�ȷ������
    for key in keywords:
        if key in filestr:
            isok=1
            for white in whitefilter:
                if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:
                    isok=0
            if isok:
                return ((key,),),'PHP ddos_cc�����ű�'
    return None
