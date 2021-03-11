import re

a = '202005110224_徐可_作业16.cpp'
c = '202005110224-徐可.zip'
patt = r'\d{12}_.*_作业\d{2}\.cpp'
patt_plust = r'(\d{12})-(.*).zip'

b = re.search(patt, a)

c_correct = c[:12] + '_' + c[13:len(c)] + '_' + '作业16'
c_recorrect = re.findall(patt_plust, c)[0]

if b != None:
    print(c_recorrect)
