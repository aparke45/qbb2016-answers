#!/usr/bin/env python

"""
Usage: /.01-part3.py <ctab file> <tab file>

Example: /.01-part3.py <~/data/results/stringtie/SRR072893/t_data.ctab> <~/qbb-2016-answers/day5-lunch/H3K4me3_out.tab>
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


df_ctab = pd.read_csv( sys.argv[1], sep="\t")
df2_ctab = pd.read_csv( sys.argv[2], sep="\t")

fpkm = {}
for row in df_ctab.itertuples():
    fpkm_col = row[12]
    t_name = row[6]
    fpkm[t_name] = fpkm_col
# Create a dictionary, where gene names are the keys and FPKMs are the values.

avg_mean = {}
for row in df2_ctab.itertuples():
    avg_mean_col = row[6]
    t_name = row[1]
    avg_mean[t_name] = avg_mean_col
    
# Create a dictionary, where gene names are the keys and average means are the values.

fpkm_ =[]
mean=[]

for key in fpkm.keys():
    if key in avg_mean:
        fpkm_.append(fpkm[key])
        mean.append(avg_mean[key])

model = sm.OLS(fpkm_,mean)
results = model.fit()
print results.summary()



"""
Information from bioweb.pasteur.fr:

bigWigAverageOverBed - Compute average score of big wig over each bed, which may have introns.
usage:
   bigWigAverageOverBed in.bw in.bed out.tab
The output columns are:
   name - name field from bed, which should be unique
   size - size of bed (sum of exon sizes
   covered - # bases within exons covered by bigWig
   sum - sum of values over all bases covered
   mean0 - average over bases with non-covered bases counting as zeroes
   mean - average over just covered bases
Options:
   -bedOut=out.bed - Make output bed that is echo of input bed but with mean column appended
   -sampleAroundCenter=N - Take sample at region N bases wide centered around bed item, rather
                     than the usual sample in the bed item.
"""