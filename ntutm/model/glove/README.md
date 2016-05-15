# glove
---
### usage of this folder

This folder implement the golve model to do word embedding from input cooccur matrix and vocab file

- glove 	

output formate :

- A binary format vocab vector
- A folder (vectors_[iteration]/) exists number of vocab size files, each file has its vector with plain text. The files are named by thier vocab_id

jieba vocab parser
---

useage:

		./run.sh glove -i [inputfile(cooccur matrix)] -o [outputfile(binary format output)] -v [vocab file(without count)] -iter [number of iterations(default 30)] -vsize [vector size of vocab(default 50)]
