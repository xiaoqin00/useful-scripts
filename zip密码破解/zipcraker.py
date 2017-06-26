#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import zipfile
from threading import Thread
import time
import optparse

def pojie_zip(path, password):
    if path[-4:] == '.zip':
        zip = zipfile.ZipFile(path, "r", zipfile.zlib.DEFLATED)
        try:
            zip.extractall(path='e:', members=zip.namelist(), pwd=password)
            print ' ----success!,The password is %s' % password
            zip.close()
            return True
        except:
            pass
        print'error'

def get_pass(passPath,zipPath):
    passFile = open(passPath, 'r')
    for line in passFile.readlines():
        password = line.strip('\n')
        print 'Try the password %s' % password
        if pojie_zip(zipPath, password):
            break
    passFile.close()

if __name__ == '__main__':
    parser=optparse.OptionParser('usage%prog --pP <passPath> --zP <zipPath>')
    parser.add_option('--pP',dest='passPath',type='string',help='specify passPath')
    parser.add_option('--zP',dest='zipPath',type='string',help='specify zipPath')
    (options,args)=parser.parse_args()
    passPath=options.passPath
    zipPath=options.zipPath
    if (passPath==None)|(zipPath==None):
        print (parser.usage)
        exit(0)
    start = time.clock()
    get_pass(passPath,zipPath)
    print "done (%.2f seconds)" % (time.clock() - start)