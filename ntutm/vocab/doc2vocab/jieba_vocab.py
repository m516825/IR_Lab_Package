#!/usr/bin/env python
#-*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import vocab
import os
import sys, getopt

def count_em(valid_path):
	x = 0
	for root, dirs, files in os.walk(valid_path):
		for f in files:
			x = x+1
	return x

if __name__ == "__main__":

	#########################
	inputdir = ''
	outputfile = ''
	data_type = ''
	try:
		opts, args = getopt.getopt(sys.argv[1:],"ht:d:o:",["idir=","ofile="])
	except getopt.GetoptError:
		print 'test.py -t <datatype> -d <inputdir> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -t <datatype> -d <inputdir> -o <outputfile>'
			sys.exit()
		elif opt in ("-d", "--idir"):
			inputdir = arg
		elif opt in ("-t"):
			data_type = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	if inputdir == '':
		print 'test.py -t <datatype> -d <inputdir> -o <outputfile>'
		sys.exit(2)

	if outputfile == '':
		outputfile = 'vocab.out'
	#########################
	
	vocabSet = set([])
	build_time = 0.
	total = count_em(inputdir)
	for dirPath, dirNames, fileNames in os.walk(inputdir):
		if len(fileNames) > 0 :
			sumContain = ''
			for f in fileNames:
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
					a = ''
				build_time += 1.

			vocabSet = vocab.buildVocab(vocabSet=vocabSet, inputData=sumContain, parallel=4)
			print >> sys.stderr, '\rdone building '+str(float("{0:.2f}".format(build_time/total*100.)))+'% vocabulary set ', 

	print >> sys.stderr, '\nstart dumping vocabulary set'			
	vocab.dumpVocab(outputfile, vocabSet)
	print >> sys.stderr, 'done dumping vocabulary set'			

