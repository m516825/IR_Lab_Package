#!/bin/bash

if [ ${1} == "jieba" ]; then
	python ../jieba_vocab.py -t CIRB010 -d ./data/ -o ./vocab_count.out
fi

if [ ${1} == "stanford" ]; then
	python ../standford_vocab.py -t CIRB010 -d ./data/ -o ./vocab_count.out
fi