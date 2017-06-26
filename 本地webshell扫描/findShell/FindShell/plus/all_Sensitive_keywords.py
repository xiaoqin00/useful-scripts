#!/usr/bin/python2.7
#coding:gbk

import re

keywords=[
            'serv-u',
            'wscript.shell',
            'phpspy',
            'jspspy',
            'webshell','shell.application',
            'documents and settings/all users',
            '����',
            '����'
            'getruntime().exec',
            '$_[+""]=\'\'',
            'chr(99).chr(104).chr(114)',
            'chr($a[79]).chr($a[78])',
            '"ass"."ert"'
        ]


knownshell=[
            '%74%68%36%73%62%65%68%71%6c%61%34%63%6f%5f%73%61%64%66%70%6e%72',
            'ixcixreaixteix_ixfixuixnixctixioixn',
            'r57shell',

]

rulelist=[
    '[\'"]e[\'"]\.[\'"]v[\'"]\.[\'"]a[\'"]\.[\'"]l[\'"]',
    '[\'"]a[\'"]\.[\'"]s[\'"]\.[\'"]s[\'"]\.[\'"]e[\'"]\.[\'"]r[\'"]\.[\'"]t[\'"]'
]



#�˲���������б� (['�ļ�·��'],['��������'])
whitefilter=[
                (['spellchecker.cfm'],['Program Files']),
]

whitefilter1=['spellchecker.cfm']

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
                return ((key,),),'�������йؼ���'

    #���ؼ��ʲ���-ȷ������
    for key in knownshell:
        if key in filestr:
            isok=1
            for white in whitefilter:
                if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:
                    isok=0
            if isok:
                return ((key,),),'��֪��������'

    #���������
    for rule in rulelist:
        result = re.search(rule,filestr)
        try:

            if result.group():
                return ((result.group(),),),'��֪��������'
        except:
            pass

    #�����������
    if 'cmd.exe' in filestr and 'program files' in filestr:
        isok=1
        for white in whitefilter1:
            if white in filepath.replace('\\','/'):
                isok=0
        if isok:
            return (('cmd.exe��Program Files',),),'���к��Źؼ���'

    #���йؼ��֣���֪��������
    if 'www.phpdp.org' in filestr:
        return (('www.phpdp.org',),),'PHP��ܼ��ܺ������йؼ���'

    if 'www.phpjm.net' in filestr:
        return (('www.phpjm.net',),),'PHP���ܺ������йؼ���'

    return None
