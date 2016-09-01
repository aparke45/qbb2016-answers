#!/usr/bin/env python
"""
Create an MA plot of two datasets to compare their similarity.

Usage: ./part-three.py <file1> <file2
For this code: ./part-three.py <~/data/results/stringtie/SRR072893> 
<~/data/results/stringtie/SRR072915>

"""



import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table( sys.argv[1] )
df2 = pd.read_table(sys.argv[2])

fpkm_x = df["FPKM"] > 0
fpkm_x = df[ fpkm_x ][ "FPKM" ]

fpkm_y = df2["FPKM"] > 0
fpkm_y = df2[ fpkm_y ][ "FPKM" ]


m = (np.log(fpkm_x) - np.log(fpkm_y)) 

a = (np.log(fpkm_x) + np.log(fpkm_y))*0.5

plt.figure()
plt.scatter(a,m, alpha = 0.1)
plt.title("MA Plot of SRR072893 & SRR072915")
plt.ylabel("M")
plt.xlabel("A")
plt.savefig("ma_plot.png")
plt.close