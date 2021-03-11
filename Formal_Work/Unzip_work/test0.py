import pandas as pd
import os

form_path = input('Form_Path: ')
save_path = input('Save_Path: ')

df = pd.read_excel(form_path, 0, 1 ,usecols=['学号', '学生姓名', '分数', '提交时间', '作业批语'])

for i in range(len(df.index)):
    df.loc[i, '学号'].astype(str) 
    if df.loc[i, '学生姓名'] == '马悦' or df.loc[i, '学生姓名'] == '江元豪':
        df.drop(i, inplace = True)

df.sort_values('学号', inplace = True)
df = df[['学号', '提交时间', '学生姓名', '分数', '作业批语']]
#index_label = '学号',
df.to_excel(save_path, index = False,  encoding = 'UTF-8')
