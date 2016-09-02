#!/usr/bin/env python

"""
Usage: ./00-prom-approx.py <~/data/results/stringtie/SRR072893/t_data.ctab>

"""
import sys

import pandas as pd

df_ctab = pd.read_csv( sys.argv[1], sep="\t")

df_roi = df_ctab["chr"].str.contains("211000")
#The line above gives back Boolean responses. For all of the lines that contain "211000", they will be stored in df_roi as True; for the others, they will be stored in df_roi as False.
df_ctab = df_ctab[~df_roi]

#The ~ in the argument of the line above, says that I don't want the values for which - in reference to the code line above it - the line contains the string "211000" and gives back True.  The tilda actually switches true for false and false for true, so, for all of the lines in the first code line that ring back True, they will be turned into falses, and will not go through the next line to become part of df_ctab.

for row in df_ctab.itertuples():
    chr = row[2]
    t_name = row[6]
    if row[3] == "+":
        tss_strt = row[4] - 500 
        tss_end = row[4] + 500
        print  chr + "\t" + str(tss_strt) + "\t" + str(tss_end) + "\t" + t_name
    elif row[3] == "-":
        tss_strt = row[5] - 500 
        tss_end = row[5] + 500
        print  chr + "\t" + str(tss_strt) + "\t" + str(tss_end) + "\t" + t_name
 
        
    



#Create a .bed with columns of start sit, end site, chrom, and t-name.
