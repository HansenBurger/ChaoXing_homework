# -*- coding: utf-8 -*-
import re
import subprocess
import shlex

def FindComment(doc_path):
    '''
        doc_path: xml file which need to be read lines

    '''
    bias = 3
    cmd = shlex.split(f"grep -n 教师批语 {doc_path}")
    result = subprocess.check_output(cmd)
    line_num_tmp = int(result.decode("utf-8")[0:3])
    line_num_comment = line_num_tmp + bias
    doc_file = open(doc_path)
    lines = doc_file.readlines()
    line_str_comment = lines[line_num_comment]
    comment = re.search( r'<w:t>(.*)</w:t>', line_str_comment, re.M|re.I).group(1)
    
    return comment
