#!/usr/bin/env python

import sys

f = open(sys.argv[1])

for line in f:
    f = line.split()
    print ">"+f[0] + "\n" + f[3] 