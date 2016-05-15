#!/usr/bin/env python
#-*- coding: utf-8 -*-
from scipy.sparse import lil_matrix
import scipy.sparse
import numpy as np

def save_sparse_matrix(filename, sparse_matrix):
    x_coo = sparse_matrix.tocoo()
    row = x_coo.row
    col = x_coo.col
    data = x_coo.data
    shape = x_coo.shape
    np.savez(filename,row=row,col=col,data=data,shape=shape)

def load_sparse_matrix(filename):
    y = np.load(filename)
    sparse_matrix = scipy.sparse.coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
    return sparse_matrix.tolil()

def cooccur_build(tokens, cooccur_matrix, vocab2indexing, window_size, symmetric=False):
	history = [-1]*window_size

	t_index = 0

	for token in tokens:

		if token == '\n':
			t_index = 0
			continue

		c_index = t_index - 1
		end_index = ((t_index - window_size) - 1) if t_index > window_size else (0 - 1)

		w2 = vocab2indexing.get(token, -1) # if token is not found in set, return -1
		if w2 == -1:
			# print token
			continue

		for index in range(c_index, end_index, -1):
			w1 = history[index%window_size]

			cooccur_matrix[w1, w2] += 1./(t_index - index)
			if symmetric:
				cooccur_matrix[w2, w1] += 1./(t_index - index)


		history[t_index%window_size] = w2
		t_index += 1

	return cooccur_matrix