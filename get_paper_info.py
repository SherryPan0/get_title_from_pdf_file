# python 3.7
# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 16:19
# @Author  : Xueli
# @File    : get_paper_info.py
# @Software: PyCharm

from scholarly import scholarly

# search a researcher's profile
print(next(scholarly.search_author('Steven A. Cholewiak')))
print('**************\n')

# search a publication and return metadata of this publication
search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
print(next(search_query))
print('**************\n')

search_query1 = scholarly.search_pubs('Public yet private: the status, durability and visibility of handover sheets')
print(next(search_query1))
print('**************\n')

'''
output:
{'affiliation': 'Vision Scientist',
 'citedby': 278,
 'email': '@berkeley.edu',
 'filled': False,
 'id': '4bahYMkAAAAJ',
 'interests': ['Depth Cues',
               '3D Shape',
               'Shape from Texture & Shading',
               'Naive Physics',
               'Haptics'],
 'name': 'Steven A. Cholewiak, PhD',
 'url_picture': 'https://scholar.google.com/citations?view_op=medium_photo&user=4bahYMkAAAAJ'}
**************

{'bib': {'abstract': 'Humans can judge from vision alone whether an object is '
                     'physically stable or not. Such judgments allow observers '
                     'to predict the physical behavior of objects, and hence '
                     'to guide their motor actions. We investigated the visual '
                     'estimation of physical stability of 3-D objects (shown '
                     'in stereoscopically viewed rendered scenes) and how it '
                     'relates to visual estimates of their center of mass '
                     '(COM). In Experiment 1, observers viewed an object near '
                     'the edge of a table and adjusted its tilt to the '
                     'perceived critical angle, ie, the tilt angle at which '
                     'the object',
         'author': ['SA Cholewiak', 'RW Fleming', 'M Singh'],
         'cites': '22',
         'eprint': 'https://jov.arvojournals.org/article.aspx?articleID=2213254',
         'gsrank': '1',
         'title': 'Perception of physical stability and center of mass of 3-D '
                  'objects',
         'url': 'https://jov.arvojournals.org/article.aspx?articleID=2213254',
         'venue': 'Journal of vision',
         'year': '2015'},
 'citations_link': '/scholar?cites=15736880631888070187&as_sdt=5,33&sciodt=0,33&hl=en',
 'filled': False,
 'source': 'scholar',
 'url_add_sclib': '/citations?hl=en&xsrf=&continue=/scholar%3Fq%3DPerception%2Bof%2Bphysical%2Bstability%2Band%2Bcenter%2Bof%2Bmass%2Bof%2B3D%2Bobjects%26hl%3Den%26as_sdt%3D0,33&citilm=1&json=&update_op=library_add&info=K8ZpoI6hZNoJ&ei=Zfr5XuSILb2I6rQP14uc0A0',
 'url_scholarbib': 'https://scholar.googleusercontent.com/scholar.bib?q=info:K8ZpoI6hZNoJ:scholar.google.com/&output=citation&scisdr=CgXQscI4GAA:AAGBfm0AAAAAXvn8waZj7X9R0UJ5cNdnvlVLWgeAd3T2&scisig=AAGBfm0AAAAAXvn8wcm2aAlNxG9d3aT-4Ypb_hxyL6SF&scisf=4&ct=citation&cd=-1&hl=en'}
**************

{'bib': {'abstract': 'Drawing on data from a multi-site case study of a range '
                     'of clinical settings, this paper explores the form of '
                     'nursing handover sheets and the processes through which '
                     'they are created and updated. We argue that these '
                     'documents function as both public and private documents, '
                     'having relevance for the whole ward while also acting as '
                     'a personal workspace. Such dual functionality needs to '
                     'be supported by any technology that seeks to provide for '
                     'the work of handover, if the handover sheet is to '
                     'continue to act as a space for work, rather',
         'author': ['R Randell', 'P Woodward', 'S Wilson'],
         'cites': '16',
         'eprint': 'https://openaccess.city.ac.uk/id/eprint/1057/1/',
         'gsrank': '1',
         'title': 'Public yet private: the status, durability and visibility '
                  'of handover sheets',
         'url': 'https://ieeexplore.ieee.org/abstract/document/4562045/',
         'venue': '2008 21st IEEE …',
         'year': '2008'},
 'citations_link': '/scholar?cites=6336224019156784111&as_sdt=5,33&sciodt=0,33&hl=en',
 'filled': False,
 'source': 'scholar',
 'url_add_sclib': '/citations?hl=en&xsrf=&continue=/scholar%3Fq%3DPublic%2Byet%2Bprivate:%2Bthe%2Bstatus,%2Bdurability%2Band%2Bvisibility%2Bof%2Bhandover%2Bsheets%26hl%3Den%26as_sdt%3D0,33&citilm=1&json=&update_op=library_add&info=71MjtyzK7lcJ&ei=bfr5Xo-UAZKSyQSLmYjgCg',
 'url_scholarbib': 'https://scholar.googleusercontent.com/scholar.bib?q=info:71MjtyzK7lcJ:scholar.google.com/&output=citation&scisdr=CgXQscI4GAA:AAGBfm0AAAAAXvn8yJkaD0ZGehToQvMNXcyByV6MZ_zo&scisig=AAGBfm0AAAAAXvn8yDOAbYvW5EK8F5-A-LiH9rOs4soa&scisf=4&ct=citation&cd=-1&hl=en'}
**************
'''