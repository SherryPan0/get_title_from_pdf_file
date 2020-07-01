# Extract titles from pdf files

#### 1. Using different python modules to extract title from pdf files
Two python modules were used to extract titles:

* **pdftitle**: using pdfminer.six to parse pdf files
* **pypdf2**

Code: extract_title.py

* Input: root directory that contains all candidate papers in pdf format.
* Output: csv files with three columns: [paperID, title\_pdftitle, title\_pypdf2] in direcrory "result/"



#### 2. Retrieve metadata of papers
**scholarly** is a python module to retrieve metadata from google scholar search engine, to get metadata of a given paper title

Example: get\_paper\_info.py
