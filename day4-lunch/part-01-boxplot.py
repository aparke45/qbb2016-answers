#!/usr/bin/env python

"""
To create a boxplot of the log(FPKM) of both SRR072893 and SRR072915.

"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_ctab = pd.read_csv( sys.argv[1], sep="\t")
df2_ctab = pd.read_csv( sys.argv[2], sep="\t")


df_roi = df_ctab["gene_name"] == "Sxl" 
df_sxl = df_ctab[df_roi]
df_sxl_fpkm = df_sxl ["FPKM"] > 0
g = df_sxl[df_sxl_fpkm]
a = np.log(g["FPKM"])


df2_roi = df2_ctab["gene_name"] == "Sxl"
df2_sxl = df2_ctab[df2_roi]
df2_sxl_fpkm = df2_sxl["FPKM"] > 0
n = df2_sxl[df2_sxl_fpkm]
b = np.log(n["FPKM"])

x = ['SRR072893', 'SRR072915']
plt.figure()
plt.boxplot([a,b], labels=x)
plt.semilogy
plt.xlabel("Set")
plt.ylabel("Log of FPKM")
plt.title("FPKM of Sxl transcripts in SRR072893 and SRR072915")
plt.savefig("FPKM_logs.png")
plt.close()



