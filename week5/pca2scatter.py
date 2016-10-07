#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

a = pd.read_table(open(sys.argv[1]), sep='\t')

pca1 = a["PC1"]
pca2 = a["PC2"]

plt.figure()
plt.scatter(pca1, pca2)
plt.title("Principal Component Analysis")
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.savefig("pcaplot.png")
plt.close()