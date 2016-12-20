#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy
from sklearn.cluster import KMeans
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import linkage
import pandas as pd
import pydendroheatmap as pdh
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import leaves_list as leaves

data_by_cell_type = pd.read_csv(open(sys.argv[1]), sep="\t", index_col=0, header=0)
data_by_cell_type_array = np.array(data_by_cell_type)
data_by_cell_type = data_by_cell_type_array.astype(np.float)

data_by_cell_type_linkage = linkage(data_by_cell_type[1:])
data_by_gene_linkage = linkage(data_by_gene[1:])

y = leaves(data_by_cell_type_linkage)

z = leaves(data_by_gene_linkage)

data_by_cell_type = data_by_cell_type[y, : ]
data_by_cell_type = data_by_cell_type[ : , z]

plt.figure()
a = KMeans(n_clusters=8, random_state=0).fit(data_by_cell_type)
labels = a.labels_

colors = ['green', 'red', 'blue', 'yellow', 'purple', 'orange', 'black', 'cyan']

for i in range(len(data_by_cell_type)):
    plt.plot(data_by_cell_type[i,0], data_by_cell_type[i,1], c = colors[labels[i]])
    
plt.savefig('CFU_vs_Poly_Expression.png')