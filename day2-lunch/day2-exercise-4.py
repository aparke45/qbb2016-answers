#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    elif count < 10: 
        print line.split ("\t")[2]
        count = count + 1
    else: 
        break

 



    