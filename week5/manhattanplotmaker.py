#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

for f in sys.argv[1:]:
    t = f.split(".")[1]
    if f.startswith("FID"):
        continue
    else:
        a = pd.read_table(open(f), delim_whitespace = True)
        log = -1*np.log10(a["P"])
        a["P"] < 10**-5
        b = a[a["P"] < 10**-5]
        # Use of double a means that, within brackets is a Boolean statement.  So for all values that evaluate the statement as True, the second a will take their values.
        log2 = -1*np.log10(b)    
        #snps = a["SNP"]

        plt.figure()
        plt.plot(log, 'b.')
        plt.plot(log2, 'r.')
        
        # Pandas automatically assigns an index, so it will plot that index with the log values.
        plt.title(t + " Manhattan Plot")
        plt.xlabel("SNPs")
        plt.ylabel("-Log10")
        plt.savefig(t + "assocplot.png")
        plt.close()