#!/usr/bin/env python

import sys
import numpy as np

import h5py
file = h5py.File(sys.argv[1])
file.keys()
counts = file['0.counts'][...]
expected = file['0.expected'][...]


for i in range(0, 459):
    for j in range(0, 459):
        if counts[i,j] == 0:
            continue
        else:
            position = []
            logratiolist = []
            logratio = np.log(counts[i,j]) - np.log(expected[i,j])
            logratiolist = logratiolist.append(logratio)
            position.append()
print [i,j], logratiolist



"""
for i in counts:
    for j in expected:
        if j = 0:
            continue
        else:
            np.log(counts) - np.log(expected)

You can use ___.shape to get the dimensions of an array.
"""
