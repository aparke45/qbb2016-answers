#!/usr/bin/env python

import sys

for line in sys.stdin:
    if "DROME" in line:
        if len(line.split()) > 3:
            var = line.split()[2]
            var2 = line.split()[3]
            print str(var)+"\t\t"+str(var2)



    
