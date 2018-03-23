
#-*-coding:utf-8-*-

__anthor__ = 'ice wolf'

def getFilesColSum(filesList):
	"""
	:type filesList: list
	:rtype: int
	"""	
	colSum = 0
	for filename in filesList:
		print filename
		target = open(filename,'r+') 
		lines = len(target.readlines()) 
		target.close()
		colSum += lines
		print "There are %d lines in %s" % (lines, filename)
	return colSum
