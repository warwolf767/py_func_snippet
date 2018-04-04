
#-*-coding:utf-8-*-

__author__ = 'ice wolf'

import os
import re

def existNum(fileList, wordList):
    """
    :type filesList: list
    :type wordList: list
    :rtype: list
    """ 
    numList = []
    wordNumList = []
    for i in range(0, len(wordList)):
        existSum = 0
        numList.append([])
        for filePath in filesList:
            target = open(filePath, 'r+')
            desList = re.findall(wordList[i], target.read())
            numList[i].append(len(desList))
            existSum += len(desList)
        wordNumList.append(existSum)
    return [numList, wordNumList]
