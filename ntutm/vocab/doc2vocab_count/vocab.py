#!/usr/bin/env python
# encoding=utf-8
import jieba
import jieba.posseg as pseg

def articleTokenize(inputData, period_break=True, parallel=0):
	"""
	This function token the imput article and return tokened article in list formate

		paramIn@ inputData 		inputData to be tokened
		paramIn@ period_break 	whether to add wrap after period mark, default value is true
		paramIn@ parallel 		default parallel is set to 0

		return@	 tokenList 		return tokened list of article
	"""
	tokenList = []

	if parallel > 0:
			jieba.enable_parallel(parallel)

	words = jieba.cut(inputData, cut_all=False)
	for word in words:
		if word == '\n':
			tokenList.append(word)
		else:
			word = word.strip()
			if word != '':
				if word == u'。' and period_break:
					tokenList.append(word)
					tokenList.append('\n')
				else:
					tokenList.append(word)

	if parallel > 0:
			jieba.disable_parallel()

	return tokenList


def buildVocabWithCount(vocabDict, inputData, parallel=0):
	"""
	This function help user to build a vocabulary dict with count by given inuput data.

		paramIn@ vocabDict		inital vocabulary dict, can be none empty dict
		paramIn@ inputData		data to be added in to vocabulary dict
		paramIn@ parallel 		default parallel is set to 0
		return@	 vocabSet 		return a added vocabulary dict
	"""
	if parallel > 0:
		jieba.enable_parallel(parallel)

	words = jieba.cut(inputData, cut_all=False)
	for word in words:
		word = word.strip()
		if word != '':
			try:
				vocabDict[word] += 1
			except:
				vocabDict[word] = 1

	words = jieba.cut(inputData, cut_all=True)
	for word in words:
		word = word.strip()
		if word != '':
			try:
				vocabDict[word] += 1
			except:
				vocabDict[word] = 1

	if parallel > 0:
		jieba.disable_parallel() 

	return vocabDict

def dumpVocabWithCount(fileName, vocabDict, key=1):
	"""
	This function dump the vocabDict to output file name

		paramIn@ fileName	output fileName
		paramIn@ vocabSet	the vocabulary set to be dump
		paramIn@ key 		sorted value, key==0 sorted by word, key==1 sorted by count, default is set to 1	
	"""
	fp = open(fileName, 'w')
	for v, c in sorted(vocabDict.iteritems(), key=lambda x: x[key]):
		try:
			fp.write(v.encode('utf8')+' '+str(c)+'\n')
		except:
			print "unable to write"

def loadVocabWithCount(fileName):
	"""
	This function can load the existing vocabulary file, and return a vocabulary dict with vocabulary count

		paramIn@ fileName	the vocabulary file name
		return@  vocabDict	the vocabulary dict load from file
	"""
	vocabDict = dict()
	fp = open(fileName, 'r')
	for line in fp.readlines():
		info = line.strip()
		vocab = info.split(' ')[0]
		count = info.split(' ')[1]
		vocabDict[vocab] = count

	return vocabDict


def buildVocab(vocabSet, inputData, parallel=0):
	"""
	This function help user to build a vocabulary set by given inuput data.

		paramIn@ vocabSet		inital vocabulary set, can be none empty set
		paramIn@ inputData		data to be added in to vocabulary set
		paramIn@ parallel 		default parallel is set to 0
		return@	 vocabSet 		return a added vocabulary set
	"""
	if parallel > 0:
		jieba.enable_parallel(parallel)

	words = jieba.cut(inputData, cut_all=False)
	for word in words:
			word = word.strip()
			if word != '':
				vocabSet.add(word)

	words = jieba.cut(inputData, cut_all=True)
	for word in words:
	    	word = word.strip()
	    	if word != '':
				vocabSet.add(word)

	if parallel > 0:
		jieba.disable_parallel() 

	return vocabSet

def dumpVocab(fileName, vocabSet):
	"""
	This function dump the vocabSet to output file name

		paramIn@ fileName	output fileName
		paramIn@ vocabSet	the vocabulary set to be dump	
	"""
	fp = open(fileName, 'w')
	for v in sorted(vocabSet):
		try:
			fp.write(v.encode('utf8')+'\n')
		except:
			print "unable to write "+v

def loadVocab(fileName):
	"""
	This function can load the existing vocabulary file, and return a vocabulary set

		paramIn@ fileName	the vocabulary file name
		return@  vocabSet	the vocabulary set load from file
	"""
	vocabSet = set()
	fp = open(fileName, 'r')
	for line in fp.readlines():
		vocab = line.strip().decode('utf-8')
		vocabSet.add(vocab)

	return vocabSet

def posTagging(inputData, plainText=False, parallel=0):
	"""
	This function takes input text and return POS tagged text or a generator(depend on param)

		paramIn@ inputData		input text data to be tagged
		paramIn@ plainText 		Boolean value, if true return plainText data, else return generator
		paramIn@ parallel 		default parallel is set to 0
 	"""
	if parallel > 0:
		jieba.enable_parallel(parallel)

	generator = pseg.cut(inputData)

	if parallel > 0:
		jieba.disable_parallel() 

	if plainText:
		contain = ''
		for word, flag in generator:
			contain += word+'('+str(flag)+')'
		return contain
	else:
		return generator

def vocabIndexing(vocabSet):
	vocab2index = {}
	index2vocab = {}
	for i, word in enumerate(sorted(vocabSet)):
		vocab2index[word] = i
		index2vocab[i] = word

	return vocab2index, index2vocab







