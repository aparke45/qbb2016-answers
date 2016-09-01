#!/usr/bin/env python

"""

"""

import sys, fasta

# Command line arguments
a_name = sys.argv[1] #TARGET
b_name = sys.argv[2] #QUERY
k = int( sys.argv[3])


target_sequence = {}
for ident, sequence in fasta.FASTAReader( open(a_name) ):
    target_sequence[ident]=sequence


# Make a loop to go through each sequence in target, report out the first dictionary's values, to find the sequence name. Then print out the name, start sites, and kmer.

extended_sequences = []

for ident, sequence in fasta.FASTAReader( open(a_name) ):

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
        for j in range(0, len(sequence2) - k):
            kmer = sequence2[ j: j+k ]
            query_start = j
            if kmer not in target_positions:
                continue
            match_positions = target_positions[kmer]
            
            #print ident, match_positions, query_start, kmer
            
            i = match_positions[0]
            j = query_start
            s = kmer
            
            while True:
                i -= 1
                j -= 1
                if target_sequence[ident][i] is not sequence2[j]:
                    break
                elif i == 0 or j == 0:
                    break
                s = target_sequence[ident][i] + s

            while True:
                i += 1
                j += 1
                if target_sequence[ident][i] is not sequence2[j]:
                    break
                elif i + 1 == len(target_sequence[ident]) or j + 1 == len(sequence2):
                    break
                s = s + target_sequence[ident][i]
            extended_sequences.append(s)

a = sorted(extended_sequences, key=len, reverse=True)
            

print a
