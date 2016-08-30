#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    elif "AS:i:0" in line:
        count = count + 1
print count
    