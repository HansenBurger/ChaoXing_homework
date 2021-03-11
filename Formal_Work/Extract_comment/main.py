'''
1. unzip all the zip file
2. read docx file
3. exctract 'grade' and 'comment' to list
4. outpput to csv
'''

import os, zipfile, re
from ReadXmlLines import FindComment

name_list = []
Id_list = []
grade_list = []
comment_list = []

raw_zip_path = r'C:\Users\汉森Burger\Desktop\C_class\raw_file\38402105_33396820_10728028.zip'
# raw_unzip_path = raw_zip_path[:len(raw_zip_path)-4]
raw_unzip_path = r'C:\Users\汉森Burger\Desktop\C_class\raw_file\38402105_33396820_10728028'

patt = r'(.*)\.(.*)'
output = re.findall(patt, raw_zip_path)[0][1]
print(output)

for file in os.listdir(raw_unzip_path):
    file_type = re.findall(patt, file)[0][1]
    file_path = os.path.join(raw_unzip_path, file)
    if file_type == 'zip':
        with zipfile.ZipFile(file_path, 'r') as f:
            for x in f.namelist():
                if re.findall(patt, x)[0][1] == 'doc':
                    print(x)
                    # x_rename = x.encode('cp437').decode('utf-8')

                   # comment_list.append(FindComment())

            

