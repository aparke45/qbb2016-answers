#!/usr/bin/env python
"""
This script both 1. removes gaps from sequences and 2. removes sequences that are shorter than the query.
"""
import sys

d = open(sys.argv[1])
#I want to remove the gaps from the sequences with them and I want to remove all sequences shorter than the query.

# for sequences shorter than the query [see line 13] and for lines with dashes [see line 14]
for line in d:
    f = line.split()
    if f[1] == "1" and f[2] == "10293":
        print line.strip().replace("-","")
    else:
        continue

