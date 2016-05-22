#!/bin/bash

if [ ${1} == "jieba" ]; then
	python ../jieba_cooccur.py -t CIRB010 -d ./data/raw_data/ -v ./data/vocab.out -o ./cooccur.out
fi
