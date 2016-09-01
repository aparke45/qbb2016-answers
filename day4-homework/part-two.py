#!/usr/bin/env python
"""
The code below creates a histogram for the FPKM values of SRR072893.

"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1] )


fpkm = df["FPKM"] > 0
fpkm = df[ fpkm ][ "FPKM" ]
a = np.log(fpkm)

plt.figure()
plt.hist(a)
plt.title("Frequency of Log FPKM for SRR072893")
plt.ylabel("Frequency")
plt.xlabel("Log(FPKM)")
plt.savefig("histogram.png")
plt.close