#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/8/1

import optparse
import activeipscan

def target_ip(startIP,endIP):
    startIPs=startIP.split('.')
    endIPs=endIP.split('.')
    print startIPs,endIPs
    for a_ip in range(int(endIPs[0])-int(startIPs[0])+1):
            for b_ip in range(int(endIPs[1])-int(startIPs[1])+1):
                for c_ip in range(int(endIPs[2])-int(startIPs[2])+1):
                    targetIP=str(int(startIPs[0])+a_ip)+'.'+str(int(startIPs[1])+b_ip)+'.'+str(int(startIPs[2])+c_ip)+'.'+'0'
                    print targetIP
                    activeipscan.main(targetIP)

def main():
    parser=optparse.OptionParser('usage%prog -H <target host> -u <user> -F <password list>')
    parser.add_option('-s',dest='startIP',type='string',help='specify startIP')
    parser.add_option('-e',dest='endIP',type='string',help='specify endIP')
    parser.add_option('-U',dest='passwordFile',type='string',help='specify password file')
    parser.add_option('-P',dest='passwordFile',type='string',help='specify password file')
    (options,args)=parser.parse_args()
    startIP = options.startIP
    endIP=options.endIP
    print 'test.py running'
    # startIP="127.0.0.0"
    # endIP="130.0.0.0"
    target_ip(startIP,endIP)
    print 'test.py running'


# main()
if __name__ == '__main__':
    main()