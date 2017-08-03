#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/7/14

#端口扫描升级版一，将端口漏洞特征存储在存储
#usage:python portVulnScan.py ip

import socket
import os
import sys
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return

def checkVilns(banner,filename):
    f=open(filename,'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+]Server is vulnerable:'+banner.strip('\n')

def main():
    if len(sys.argv)==3:
        filename=sys.argv[2]
        if not os.path.isfile(filename):
            print '[-]'+filename+'does not exist.'
            exit(0)
        if not os.access(filename,os.R_OK):
            print '[-]'+filename+'access denied.'
            exit(0)
    else:
        print '[-]Usage:'+str(sys.argv[0])+'<vuln filename>'
        exit(0)
    portList=[21,22,25,80,110,443]
    # for x in range(1,150):
    # ip='192.168.95.'+str(x)
    ip=sys.argv[1]
    for port in portList:
        banner=retBanner(ip,port)
        if banner:
            print '[+]'+ip+':'+banner
            checkVilns(banner,filename)

if __name__ == '__main__':
    main()