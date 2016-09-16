#!/usr/bin/env python

import sys
import fasta
import numpy as np

contigs = fasta.FASTAReader(open(sys.argv[1]))


# Number of contigs, min, max, avg contig length

count = 0
contigs_list = []
for identifier, sequence in contigs:
    count += 1
    sequence = len(sequence)
    contigs_list.append(sequence)
    
contigs_list.sort()
g = np.sum(contigs_list)
g_50 = g/2.


sum = 0
for i in contigs_list:
    sum += i
    if sum > g_50:
        n50 = i
        break

    
print count
print min(contigs_list)
print max(contigs_list)
print np.mean(contigs_list)
print n50


