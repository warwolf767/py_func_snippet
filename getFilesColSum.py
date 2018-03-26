
#-*-coding:utf-8-*-

__author__ = 'ice wolf'

def getFilesColSum(filesList):
	"""
	:type filesList: list
	:rtype: int
	"""	
	colSum = 0
	for filename in filesList:
		print filename
		target = open(filename,'r+') 
		content = target.readlines()
        L = content[0].find('\r') == -1 and content or content[0].split('\r')
        lines = len(L)  
		target.close()
		colSum += lines
		print "There are %d lines in %s" % (lines, filename)
	return colSum
