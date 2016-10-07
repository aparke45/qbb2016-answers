#!/usr/bin/env python

import sys


for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        l = "FID" + "\t" + "IID" + line[0:].rstrip("\r\n")
        print l
    else:
        s = line[0:3] + "\t" + line[4:].rstrip("\r\n")
        print s


