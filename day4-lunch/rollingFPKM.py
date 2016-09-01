#!/usr/bin/env python

"""
To calculate and put on one graph, the rolling means of FPKM from two files - SRR072893 and SRR072915 - for each chromosome.

"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# To open things from the command line:
a = open(sys.argv[1])
b = open(sys.argv[2])
c = int(sys.argv[3])

x = ["2R", "2L", "3R", "3L", "4", "X"]
# List of chromosomes for the creation of a loop that goes through each chromosome - 2L, 2R, etc.

df_ctab = pd.read_csv( sys.argv[1], sep="\t")
df2_ctab = pd.read_csv( sys.argv[2], sep="\t")

for i in x:
    df_roi = df_ctab[ "chr" ] == i
    df_chrom = df_ctab[ df_roi ]
    df = df_chrom[ "FPKM" ].rolling( 200 ).mean()

    df2_roi = df2_ctab[ "chr" ] == i
    df2_chrom = df2_ctab[ df2_roi ]
    df2 = df2_chrom[ "FPKM" ].rolling( 200 ).mean()
    
    dog = ['SRR072893', 'SRR072915']
    plt.figure()
    plt.plot(df, label=dog[0])
    plt.plot(df2, label=dog[1])
    plt.legend()
    plt.xlabel("Position")
    plt.ylabel("Rolling FPKM Mean")
    plt.title("Rolling mean (size = 200) for " + i)
    plt.savefig( "rollingFPKMplots" + i + ".png" )
    plt.close()
