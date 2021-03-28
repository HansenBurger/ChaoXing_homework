"""
    Mainfunc: File extract
"""

import zipfile, shutil, re, os

main_file_path = input('File source path: ')
save_file_path = input('File save path: ')

extension_info = input('Extention Info')

patt = r'(\d{12})-(.*).zip'

def CppCollect(folder, name, path):

    for x in folder.namelist():
        if x[len(x)-4:] == '.cpp':
            folder.extract(x, path + os.sep)
            x_path = os.path.join(path, x)
            x_rename_path = os.path.join(path, name)
            os.rename( x_path , x_rename_path )
        print(name + 'Extract done!')


if os.path.isdir(save_file_path):
    shutil.rmtree(save_file_path)
else:
    os.mkdir(save_file_path)

for file in os.listdir(main_file_path):

    info_elements = re.findall(patt, file)[0]
    stu_id = info_elements[0]
    stu_name = info_elements[1]

    file_path = os.path.join(main_file_path, file)

    with zipfile.ZipFile(file_path , 'r') as f:
        file_conter = len(f.namelist())-1
        if file_conter == 1:
            file_name = stu_id + '_' + stu_name + '_' + extension_info + '.cpp'
            CppCollect(f, file_name, save_file_path)
        else:
            pass
            # TODO
            

        # for x in f.namelist():
        #     if x[len(x)-4:] == '.cpp' and counter < 2 :
        #         counter = counter + 1
        #         x_rename = x.encode('cp437').decode('utf-8')
        #         if tag != None:
        #             f.extract( x , save_file_path + os.sep )
        #             temp_path_1 = os.path.join( save_file_path , x )
        #             temp_path_2 = os.path.join( save_file_path , x_rename )
        #         else:
        #             info_elements = re.findall(patt_re, file)[0]
        #             x_rename = info_elements[0] + '_' + info_elements[1] + '_' + '作业' + save_file_path[len(save_file_path)-2:] + '.cpp'
        #             f.extract( x , save_file_path_u + os.sep )
        #             temp_path_1 = os.path.join( save_file_path_u , x )
        #             temp_path_2 = os.path.join( save_file_path_u , x_rename )
        #         os.rename( temp_path_1 , temp_path_2 )
        #         print(x_rename + ' Extract Done!')
