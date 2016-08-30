#!/usr/bin/env python

import sys

count = 0

for line in sys.stdin:
    if line.startswith("@"):
        continue
    elif "ZS:i:" in line:
        continue
    elif "AS:i:" in line:
        count = count + 1
print count
    