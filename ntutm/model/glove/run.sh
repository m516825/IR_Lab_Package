#!/bin/bash

if [ ${1} == "glove" ]; then
	shift
	Iter=30
	Vsize=50
	while [[ ${1} != "" ]]; do
	 	key=${1}
	 	case $key in
	 		-i|--inputfile)
			Inputfile="${2}"
			shift	
	 		;;
	 		-o|--outputfile)
			Outputfile="${2}"
			shift	
	 		;;
	 		-v|--vocabfile)
			Vocabfile="${2}"
			shift	
	 		;;
	 		-iter)
			Iter="${2}"
			shift	
	 		;;
	 		-vsize)
			Vsize="${2}"
			shift	
	 		;;
			*)
            
    		;;
	 	esac
	 	shift	
	done
	gcc cooccur_formated.c -o main
	./main -i ${Inputfile} -o reformate.bin
	gcc glove.c -o main
	./main -save-file ${Outputfile} -threads 8 -input-file reformate.bin -x-max 100 -iter ${Iter} -vector-size ${Vsize} -binary 3 -vocab-file ${Vocabfile} -verbose 2
fi