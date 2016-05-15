#!/bin/bash

if [ ${1} == "jieba" ]; then
	shift
	str=""
	while [[ ${1} != "" ]]; do
	 	str=$str" "${1}
	 	shift	
	done
	python jieba_cooccur.py $str 
fi