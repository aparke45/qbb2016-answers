#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt


a = pd.read_table(open(sys.argv[1]), delim_whitespace= True)

histvals = a["MAF"]

plt.hist(histvals)
plt.title("Allele Frequency Spectrum")
plt.savefig("allelefreqhist.png")

# Call read MAF column and call plt.hist
