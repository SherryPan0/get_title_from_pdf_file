# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 14:07
# @Author  : Xueli
# @File    : extract_title.py
# @Software: PyCharm

import pandas as pd
import os
from PyPDF2 import PdfFileReader
import datetime
import multiprocessing as mp

# using two modules to extract titles from pdf files
# method 1: using pdftitle module
def get_title_pdftitle(path):
    """
    get metadata info from a pdf file, here we only return titles
    :param path(str): pdf file path,
            path = "/Users/sherry/Google_Drive/transfer/SchRecSubset1/DaMon/DaMon2008/p41jouini.pdf"
    :return: title(str)
    """
    cmd = 'pdftitle -p {}'.format(path)
    res = os.popen(cmd)
    title = res.read()
    return title

# method 2: using pypdf2 module
def get_info_pypdf2(path):
    """
    get metadata info from a pdf file, here we only return titles
    :param path(str): pdf file path,
            path = "/Users/sherry/Google_Drive/transfer/SchRecSubset1/DaMon/DaMon2008/p41jouini.pdf"
    :return: title(str)
    """
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        # number_of_pages = pdf.getNumPages()
    # author = info.author
    # creator = info.creator
    # producer = info.producer
    # subject = info.subject
    title = info.title
    return title


def iter_files(rootDir):
    """
    :param rootDir(str): root directory that contains all pdf files
    :return:
    """
    file_name_list = []
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root,file)
            if file_name.endswith('/Icon'):
                pass
            else:
                file_name_list.append(file_name)
    df = pd.DataFrame(file_name_list, columns=['paperID'])
    df.to_csv('pdf_ls.csv', index=False)
    return file_name_list

def partition(ls, size):
    """
    Returns a new list with elements
    of which is a list of certain size.

        >>> partition([1, 2, 3, 4], 3)
        [[1, 2, 3], [4]]
    """
    print('the total number of pdf files in this root directory is: ', len(ls))
    return [ls[i:i+size] for i in range(0, len(ls), size)]

def job(path_list):
    # print('the number of pdf files in this list is: ', len(path_ls))
    path_ls = path_list[0]
    group_name = path_list[1]
    start = datetime.datetime.now()
    title_ls = []
    fail_ls = []
    for path in path_ls:
        try:
            title1 = get_title_pdftitle(path)
            title2 = get_info_pypdf2(path)
            title_ls.append([path, title1, title2])
        except:
            fail_ls.append(path)
            # print('fail to extract title from this file: ', path)
    df = pd.DataFrame(title_ls, columns=['paperID', 'title_pdftitle', 'title_pypdf2'])
    fail_df = pd.DataFrame(fail_ls, columns=['fail_path'])
    df.to_csv('result/titles_{}.csv'.format(group_name), index=False)
    print('running time of this job: ', datetime.datetime.now() - start)
    return  df, fail_df



# speed up by using multiprocess
if __name__ == '__main__':
    start = datetime.datetime.now()
    rootDir = '/Users/sherry/Google_Drive/transfer/subset2_4'
    # rootDir = input('the root directory of all pdf files: ')
    pdf_ls = iter_files(rootDir)
    # print('the root directory of all pdf files: ', len(pdf_ls))
    sub_ls = partition(pdf_ls,10)
    first_param = sub_ls
    second_param = list(range(len(sub_ls)))
    print('second param: ', second_param)
    pool = mp.Pool(processes=4)
    result = pool.map(job, zip(first_param, second_param))


