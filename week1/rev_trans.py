#!/usr/bin/env python
import sys
import itertools
import fasta


nucleotide = fasta.FASTAReader(open(sys.argv[1]))
protein = fasta.FASTAReader(open(sys.argv[2]))


nucleotides = []
aminos = []

for i in nucleotide:
    nucleotides.append(i)
    
for g in protein:
    aminos.append(g)


for item in itertools.izip(nucleotides, aminos):
    seq = []
    n = 0
    nuc_s = item[0][1]
    pro_s = item[1][1]
    for aminoacid in pro_s:
        if aminoacid == "-":
            seq.append("---")
        else:
            codon = nuc_s[n:n+3]
            n += 3
            seq.append(codon)
    print ">" + item[0][0]
    print "".join(seq)


