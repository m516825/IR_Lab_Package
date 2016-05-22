#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import vocab
import os
import sys, getopt
import time 
from scipy.sparse import lil_matrix
import cooccur


def count_em(valid_path):
	x = 0
	for root, dirs, files in os.walk(valid_path):
		for f in files:
			x = x+1
	return x


if __name__ == '__main__':

	#########################
	inputdir = ''
	vocabfile = ''
	outputfile = ''
	data_type = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"ht:d:v:o:",["idir=","vfile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -t <datatype> -d <inputdir> -v <vocab> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -t <datatype> -d <inputdir> -v <vocab> -o <outputfile>'
			sys.exit()
		elif opt in ("-d", "--idir"):
			inputdir = arg
		elif opt in ("-v", "--vfile"):
			vocabfile = arg
		elif opt in ("-t"):
			data_type = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if inputdir == '' or vocabfile=='':
		print 'test.py -t <datatype> -d <inputdir> -v <vocab> -o <outputfile>'
		sys.exit(2)

	if outputfile == '':
		outputfile = 'cooccur.mtx.count'
	#########################

	sTime = time.time()

	vocabSet = vocab.loadVocab(vocabfile)
	print >> sys.stderr, 'done loading vocabulary set'
	v2i, i2v = vocab.vocabIndexing(vocabSet=vocabSet)
	print >> sys.stderr, 'done building index'

	vocab_size = len(vocabSet)
	cooccur_matrix = lil_matrix((vocab_size, vocab_size))

	built_file = 0
	total_file = count_em(inputdir)

	for dirPath, dirNames, fileNames in os.walk(inputdir):
		if len(fileNames) > 0 :
			sumContain = ''
			for f in fileNames:
				contain = ''
				try:
					if data_type == 'CIRB010':
						root = ET.parse(dirPath+'/'+f).getroot()
						date = root[0][1].text.strip()
						title = root[0][2].text.strip()
						text = ''
						for p in root[0][3]:
							text += p.text.strip()
						contain = date + title + text
						sumContain += contain
					else:
						fin = open(dirPath+'/'+f, 'r')
						for line in fin.readlines():
							sumContain += line.strip()
				except:
					contain = ''
					
				built_file += 1

			tokens = vocab.articleTokenize(inputData=sumContain, parallel=4)

			cooccur_matrix = cooccur.cooccur_build(tokens=tokens, cooccur_matrix=cooccur_matrix, vocab2indexing=v2i, window_size=8, symmetric=False)

			
			print >> sys.stderr, '\rdone building '+str(built_file)+' files, '+str(float("{:.4f}".format(built_file/float(total_file)*100)))+'% of corpus file', 
	print '\n'
	
	eTime = time.time()
	print >> sys.stderr, 'takes '+str(eTime-sTime)+' s to build cooccur_matrix'


	# sTime = time.time()
	# cooccur.save_sparse_matrix('cooccur.mtx', cooccur_matrix)
	# eTime = time.time()
	# print >> sys.stderr, 'takes '+str(eTime-sTime)+' s to dump cooccur_matrix'

	# sTime = time.time()
	# cooccur_matrix2 = cooccur.load_sparse_matrix('cooccur.mtx.npz')
	# eTime = time.time()
	# print >> sys.stderr, 'takes '+str(eTime-sTime)+' s to load cooccur_matrix'

	sTime = time.time()
	data_index = cooccur_matrix.nonzero()
	fp = open(outputfile, 'w')
	for index in range(len(data_index[0])):
		index_i = data_index[0][index]
		index_j = data_index[1][index]
		out = str(index_i)+' '+str(index_j)+' '+str(cooccur_matrix[index_i, index_j])+'\n'
		fp.write(out)
	eTime = time.time()
	print >> sys.stderr, 'takes '+str(eTime-sTime)+' s to dump cooccur_matrix count'


