# doc2vocab
---
### usage of this folder

There are several methods in this folder to generate the vocab file with count from input data :

- jieba 	(chinese parser)
- stanford	(chinese parser)

output formate :

		sorted_vocab_1 count 
		sorted_vocab_2 count
		sorted_vocab_3 count
		sorted_vocab_4 count
		.
		.
		.

data type :

- none		(for text only data)
- CIRB010	(for CIRB010 data format)

jieba vocab parser
---

useage:

		./run.sh jieba -t [data type] -d [directory of data(recursively wolk through)] -o [output file name]

stanford vocab parser
---
This method will take bunch of time, since it has to load model for each sentence.

useage:

		./run.sh stanford -t [data type] -d [directory of data(recursively wolk through)] -o [output file name]