#!/usr/bin/env python

import sys
import itertools
import fasta
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
import scipy.stats as stats


query = fasta.FASTAReader(open(sys.argv[1]))
nucleoseqs = fasta.FASTAReader(open(sys.argv[2]))

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
 
    
# The above codon table is from http://stackoverflow.com/questions/19521905/translation-dna-to-protein.   

query = []
for identifier, sequence in query:
    query = [sequence[i:i+3] for i in range(0, len(sequence), 3)]

nucleoseqs = []  
for identifier2, sequence2 in nucleoseqs:
    nucleoseqs = [sequence2[i:i+3] for i in range(0, len(sequence2), 3)]


syn = {}
nonsyn = {}

for index, i in enumerate(query):
    syn[index] = 0
    nonsyn[index] = 0
index = 0
    

for (n,q) in zip(nucleoseqs, cycle(query)):
    if n not in codontable:
        continue
    elif codontable[n] == codontable[q]:
        if n == q:
            continue
        else:
            syn[index] += 1
    else:
        nonsyn[index] += 1
    if index <= 3427:
        index += 3
    else:
        index = 0

print index, syn[index]

dNdSrat = []


for index in syn and nonsyn:
    dNdSrat.append((syn[index], nonsyn[index]))

d_list = []

for item in dNdSrat:
    d_list.append(item[1]-item[0])

keys = []
for index in syn:
    keys.append(index)


array = np.array(d_list)

z_score = stats.zscore(array)


plt.figure()
plt.scatter(keys, z_score)
plt.title("Z Scores vs Codon Position in Sequence")
plt.xlabel("Codon Position in Sequence")
plt.ylabel("Z-Score")
plt.savefig("Z-ScorePlot.png")
plt.close()






"""



import sys
import itertools
import fasta
import matplotlib.pyplot as plt
import numpy as np


query = fasta.FASTAReader(open(sys.argv[1]))
nucleoseqs = fasta.FASTAReader(open(sys.argv[2]))

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
 
    
# The above codon table is from http://stackoverflow.com/questions/19521905/translation-dna-to-protein.   

# querylist = []
# for identifier, sequence in query:
#     for i in range(0, len(sequence), 3):
#         querylist.append(sequence[i:i+3])
# print querylist

querycodons = []
for identifier, sequence in query:
    querycodons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
print querycodons



# nucleoseqslist = []
# for identifier2, sequence2 in nucleoseqs:
#     nucleoseqslist.append(sequence2)
#
# d = {}
#
# t = 0
#
#
for alignment in nucleoseqslist:
    location = 1
    alignment = nucleoseqslist[t]
    t += 1
    for position in range(0, len(querylist)-3, 3):
        seq_codon = alignment[position:position+3]
        query_codon = querylist[position:position+3]
        if codontable[query_codon] == codontable[seq_codon]:
            if query_codon == seq_codon:
                if location not in d:
                    d[location] = [("-")]
                else:
                    d[location].append(("-"))
                location += 1
            else:
                if location not in d:
                    d[location] = [("dS")]
                else:
                    d[location].append(("dS"))
                location += 1
        else:
            if location not in d:
                d[location] = [("dN")]
            else:
                d[location].append(("dN"))
            location += 1



dS = []
dN = []

for k in d.keys():
    for mutation in d[k]:
        none = d[k].count("-")
        syn = d[k].count("dS")
        nonsyn = d[k].count("dN")
    print syn

"""



