# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 14:07
# @Author  : Xueli
# @File    : extract_title.py
# @Software: PyCharm

import pandas as pd
import os
from PyPDF2 import PdfFileReader

# method 1: using pdftitle module
# pdftitle uses pdfminer.six project to parse PDF document
def get_title_pdftitle(path):
    try:
        cmd = 'pdftitle -p {}'.format(path)
        res = os.popen(cmd)
        title = res.read()
        return title
    except:
        print('Fail to parse:\n', path)

# method 2: using pypdf2 module
def get_info_pypdf2(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        # number_of_pages = pdf.getNumPages()
    # author = info.author
    # creator = info.creator
    # producer = info.producer
    # subject = info.subject
    title = info.title
    return(title)

if __name__ == '__main__':
    title_ls = []
    for i in range(1,51):
        path = 'test_set/R{}-1.pdf'.format(i)
        title1 = get_title_pdftitle(path)
        title2 = get_info_pypdf2(path)
        title_ls.append([i, title1, title2])
        print(i)
        print('get title using pdftitle: ', title1)
        print('get title using pypdf2: ', title2)
        print('****************')
    df = pd.DataFrame(title_ls, columns=['paperID', 'title using pdftitle', 'title using pypdf2'])
    df.to_csv('title.csv', index=False)


