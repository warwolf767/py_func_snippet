
#-*-coding:utf-8-*-

__author__ = 'ice wolf'

import os
import re

def getFileList(dir, fileList, patternStr='^$'):
    """
    :type dir: string
    :type filesList: list
    :type patternStr: string
    :rtype: list
    """ 
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for name in os.listdir(dir):
            #Ignore files with '.jpg'
            if not (re.findall(patternStr, name)) == []:
                continue
            newDir=os.path.join(dir,name)
            getFileList(newDir, fileList)  
    return fileList
