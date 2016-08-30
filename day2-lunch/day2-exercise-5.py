#!/usr/bin/env python

import sys

count = 0
sum1 = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
        
    elif line.split()[4] != "*":
        cut_mapq_line=line.split()[4]
        count = count + 1
        sum1 = sum1 + int(cut_mapq_line) 
    else: 
        break

print float (sum1/count)