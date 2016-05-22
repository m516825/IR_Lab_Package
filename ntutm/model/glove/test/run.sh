#!/bin/bash

if [ ${1} == "glove" ]; then
	gcc ../cooccur_formated.c -o main
	./main -i ./data/cooccur.out -o reformate.bin
	gcc ../glove.c -o main
	./main -save-file vocab -threads 8 -input-file reformate.bin -x-max 100 -iter 30 -vector-size 50 -binary 3 -vocab-file ./data/vocab.out -verbose 2
fi
