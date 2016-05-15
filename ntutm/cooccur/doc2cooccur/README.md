# doc2cooccur
---
### usage of this folder

There are several methods in this folder to generate the cooccur matrix from input data :

- jieba 	(chinese parser)

output formate :
-The vocab_id is auto-generate from vocab file

		vocab_id vocab_id cooccur_count
		vocab_id vocab_id cooccur_count
		vocab_id vocab_id cooccur_count
		vocab_id vocab_id cooccur_count
		.
		.
		.

data type :

- none		(for text only data)
- CIRB010	(for CIRB010 data format)

jieba vocab parser
---

useage:

		./run.sh jieba -t [data type] -d [directory of data(recursively wolk through)] -v [vocab file(without count)]-o [output file name]
