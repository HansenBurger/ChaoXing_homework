"""
    take zipfile all out
"""
import os
from shutil import copy

main_file_path = input('PATH: ')
target_file_path = os.path.join(main_file_path , 'Extract')
os.rmdir(target_file_path)
os.mkdir(target_file_path)

count_num = 0

for item in os.listdir(main_file_path):
    folder_path = os.path.join(main_file_path , item)
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path , file)
        # print(file)
        if os.path.isfile(file_path):
            print('Get it')
            copy(file_path, target_file_path)

