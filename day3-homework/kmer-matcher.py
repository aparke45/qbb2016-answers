#!/usr/bin/env python

"""
Read sequences from a fasta file, count the number of times each k-mer occurs 
across all sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta.file

"""

import sys, fasta

# Command line arguments
a = open(sys.argv[1]) #TARGET
b_name = sys.argv[2] #QUERY
k = int( sys.argv[3])



# Make a loop to go through each sequence in target, report out the first dictionary's values, to find the sequence name. Then print out the name, start sites, and kmer.


for ident, sequence in fasta.FASTAReader( a ):

    target_positions = {}
    sequence = sequence.upper()
    for i in range(0, len(sequence) - k):
        kmer = sequence[ i: i+k ]
        if kmer in target_positions.keys():
            target_positions[kmer].append(i)
        else:
            target_positions[ kmer ] = [ i ]

    #print target_positions
    
    for ident2, sequence2 in fasta.FASTAReader( open(b_name) ):
    # By replacing the variable in FASTAReader with a function of open, the system reopens the query file (that is called at every comparison) - which is the loop I wanted!
        sequence2 = sequence2.upper()
        for i in range(0, len(sequence2) - k):
            kmer = sequence2[ i: i+k ]
            query_start = i
            if kmer not in target_positions:
                continue
            match_positions = target_positions[kmer]
            
            print ident, match_positions, query_start, kmer

""""
## The above identifies kmers in the query sequence and looks for them in the target_positions dictionary.

target_sequence name =
target_start = match_positions


print target_sequence_name + target_start + query_start + k
'''
"""