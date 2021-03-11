# -*- coding: utf-8 -*-
import re
import subprocess
import shlex

doc_path=r"信息工程学院-电子信息类-2020电子信息类02-202005110201-蔡昊楠.doc"
cmd=shlex.split(f"grep -n 教师批语 {doc_path}")
result = subprocess.check_output(cmd)
line_num_tmp = int(result.decode("utf-8")[0:3])
bias = 3
line_num_comment = line_num_tmp + bias
print(line_num_comment)
doc_file=open(doc_path)
lines=doc_file.readlines()
line_str_comment = lines[line_num_comment]
comment = re.search( r'<w:t>(.*)</w:t>', line_str_comment, re.M|re.I).group(1)
print(comment)
