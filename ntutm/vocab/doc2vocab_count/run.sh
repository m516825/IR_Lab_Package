#!/bin/bash

if [ ${1} == "jieba" ]; then
	shift
	str=""
	while [[ ${1} != "" ]]; do
	 	str=$str" "${1}
	 	shift	
	done
	python jieba_vocab.py $str 
fi
if [ ${1} == "stanford" ]; then
	shift
	str=""
	while [[ ${1} != "" ]]; do
	 	str=$str" "${1}
	 	shift	
	done
	python standford_vocab.py $str 
fi