#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/6/22

import sys
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
#main
def main(argv) :
    #����ļ���������ֻ�����ĵ�������ֻ����argv��1��
    outfile = argv[1] + '.txt'
    args = [argv[1]]

    debug = 0
    pagenos = set()
    password = ''
    maxpages = 0
    rotation = 0
    codec = 'utf-8'   #�������
    caching = True
    imagewriter = None
    laparams = LAParams()
    #
    PDFResourceManager.debug = debug
    PDFPageInterpreter.debug = debug

    rsrcmgr = PDFResourceManager(caching=caching)
    outfp = file(outfile,'w')
#pdfת��
    device = TextConverter(rsrcmgr, outfp, codec=codec, laparams=laparams,
                imagewriter=imagewriter)

    for fname in args:
        fp = file(fname,'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
#�����ĵ�������ÿһҳ������
        for page in PDFPage.get_pages(fp, pagenos,
                          maxpages=maxpages, password=password,
                          caching=caching, check_extractable=True) :
            page.rotate = (page.rotate+rotation) % 360
            interpreter.process_page(page)
        fp.close()
    device.close()
    outfp.close()
    return

if __name__ == '__main__' :
    main(sys.argv)