"""
    Mainfunc: File extract
    Mode0: Experiment
    Mode1: Homework
"""

import zipfile
import shutil
import re
import os

mode = 0
main_file_path = input('File source path: ')
save_file_path = input('File save path: ')
save_file_path_f = os.path.join(save_file_path , 'Formatted')
save_file_path_u = os.path.join(save_file_path , 'Unformatted')

patt = r'\d{12}_.*_作业\d{2}\.cpp'
patt_re = r'(\d{12})-(.*).zip'

if os.path.isdir(save_file_path_f) or os.path.isdir(save_file_path_u) :
    shutil.rmtree(save_file_path_f)
    shutil.rmtree(save_file_path_u)
else:
    os.mkdir(save_file_path_f)
    os.mkdir(save_file_path_u)

for file in os.listdir(main_file_path):
    file_path = os.path.join(main_file_path, file)
    with zipfile.ZipFile(file_path , 'r') as f:
        for x in f.namelist():
            if x[len(x)-4:] == '.cpp':
                x_rename = x.encode('cp437').decode('utf-8')
                tag = re.search( patt , x_rename )
                if tag != None:
                    f.extract( x , save_file_path_f + os.sep )
                    temp_path_1 = os.path.join( save_file_path_f , x )
                    temp_path_2 = os.path.join( save_file_path_f , x_rename )
                else:
                    info_elements = re.findall(patt_re, file)[0]
                    x_rename = info_elements[0] + '_' + info_elements[1] + '_' + '作业' + save_file_path[len(save_file_path)-2:] + '.cpp'
                    f.extract( x , save_file_path_u + os.sep )
                    temp_path_1 = os.path.join( save_file_path_u , x )
                    temp_path_2 = os.path.join( save_file_path_u , x_rename )
                os.rename( temp_path_1 , temp_path_2 )
                print(x_rename + ' Extract Done!')
