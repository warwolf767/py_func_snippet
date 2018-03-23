
#-*-coding:utf-8-*-

__anthor__ = 'ice wolf'

import os

def getFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            if s == "xxx":
                continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList

def getFilesColSum(filesList):
	colSum = 0
	for filename in filesList:
		print filename
		target = open(filename,'r+') 
		lines = len(target.readlines()) 
		target.close()
		colSum += lines
		print "There are %d lines in %s" % (lines, filename)
	return colSum

filesList = getFileList('F:\\MPD\\wamp\www\\BMS2-3.0\\0', [])
print len(filesList)
colSum = getFilesColSum(filesList)
