"""
    Mainfunc: File extract
"""

import zipfile, shutil, re, os

main_file_path = input('File source path: ')
save_file_path = input('File save path: ')

save_file_path_cpp = os.path.join(save_file_path,'CPP')
save_file_path_txt = os.path.join(save_file_path,'TXT')

extension_info = input('Extention Info: ')

patt_zip = r'(\d{12})-(.*).zip'
patt_doc = r'(\d{12})-(.*).doc'

def CppCollect(folder, name, path):

    for x in folder.namelist():
        if x[len(x)-4:] == '.cpp':
            folder.extract(x, path + os.sep)
            x_path = os.path.join(path, x)
            x_rename_path = os.path.join(path, name)
            os.rename( x_path , x_rename_path )
        print(name + 'Extract done!')


if os.path.isdir(save_file_path_cpp):
    shutil.rmtree(save_file_path_cpp)
else:
    os.mkdir(save_file_path_cpp)

if os.path.isdir(save_file_path_txt):
    shutil.rmtree(save_file_path_txt)
else:
    os.mkdir(save_file_path_txt)

for file in os.listdir(main_file_path):

    file_path = os.path.join(main_file_path, file)

    if file[len(file)-3:] == 'zip':

        info_elements_zip = re.findall(patt_zip, file)[0]
        stu_id_zip = info_elements_zip[0]
        stu_name_zip = info_elements_zip[1]

        with zipfile.ZipFile(file_path , 'r') as f:
            file_conter = len(f.namelist())-1
            if file_conter == 1:
                file_name = stu_id_zip + '_' + stu_name_zip + '_' + extension_info + '.cpp'
                CppCollect(f, file_name, save_file_path_cpp)
            else:
                pass
                # TODO
    
    if file[len(file)-3:] == 'doc':

        info_elements_doc = re.findall(patt_doc, file)[0]
        stu_id_doc = info_elements_doc[0]
        stu_name_doc = info_elements_doc[1]
        file_name = stu_id_doc + '_' + stu_name_doc + '_' + extension_info +'.cpp'
        shutil.copy(file_path, save_file_path_txt)
        df_file_name = os.path.join(save_file_path_txt, file)
        re_file_name = os.path.join(save_file_path_txt, file_name)
        os.rename(df_file_name, re_file_name)


    # with zipfile.ZipFile(file_path , 'r') as f:
    #     file_conter = len(f.namelist())-1
    #     if file_conter == 1:
    #         file_name = stu_id_zip + '_' + stu_name_zip + '_' + extension_info + '.cpp'
    #         CppCollect(f, file_name, save_file_path_cpp)
    #     else:
    #         pass
    #         # TODO
            

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
        #         -    f.extract( x , save_file_path_u + os.sep )
        #             temp_path_1 = os.path.join( save_file_path_u , x )
        #             temp_path_2 = os.path.join( save_file_path_u , x_rename )
        #         os.rename( temp_path_1 , temp_path_2 )
        #         print(x_rename + ' Extract Done!')
