#!/usr/bin/env python
"""
This code below creates a Gaussian kernel density estimation plot.

"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

df = pd.read_table( sys.argv[1] )

fpkm = df["FPKM"] > 0
fpkm = df[ fpkm ][ "FPKM" ]
fpkm = np.log(fpkm).values

x = np.linspace(0, 100, 1000)

j = stats.gaussian_kde(fpkm)


plt.figure()
plt.plot(x, j(x))
plt.title("Gaussian Kernel Density Estimation of FPKM for SRR072893")
plt.ylabel("Probability Density")
plt.xlabel("FPKM")
plt.savefig("gaussian_kde_fpkm.png")
plt.close