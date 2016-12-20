#!/usr/bin/env python

import sys
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import scipy
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import linkage
import pandas as pd
import pydendroheatmap as pdh
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import leaves_list as leaves

# For cell type and gene names from hema_data.txt file:

cell_type = []
genes = []
for i, line in enumerate(open(sys.argv[1])):
	fields = line.split('\t')
	if i == 0:
		cell_type = fields[1:]
	else:
		genes.append(fields[0])

# For linkages:
data_by_cell_type = pd.read_csv(open(sys.argv[1]), sep="\t", index_col=0, header=0)
data_by_cell_type_array = np.array(data_by_cell_type)
data_by_gene = np.transpose(data_by_cell_type_array)

data_by_cell_type = data_by_cell_type_array.astype(np.float)
data_by_gene = data_by_gene.astype(np.float)

data_by_cell_type_linkage = linkage(data_by_cell_type[1:])
data_by_gene_linkage = linkage(data_by_gene[1:])

y = leaves(data_by_cell_type_linkage)

z = leaves(data_by_gene_linkage)

data_by_cell_type = data_by_cell_type[y, : ]
data_by_cell_type = data_by_cell_type[ : , z]

# For dendrograms:
plt.figure()
dendrogram(data_by_gene_linkage, labels= cell_type)
plt.title('Dendrogram')
plt.xlabel('Cell Type')
plt.ylabel('Distance')
plt.savefig("Dendrogram_by_cell_type.png")
plt.close()


plt.figure()
dendrogram(data_by_cell_type_linkage, labels = genes)
plt.title('Dendrogram')
plt.xlabel('Genes')
plt.ylabel('Distance')
plt.savefig('Dendrogram_by_gene.png')
plt.close()


# For heatmap:
heatmap = pdh.DendroHeatMap(heat_map_data=data_by_cell_type, left_dendrogram = data_by_cell_type_linkage, top_dendrogram = data_by_gene_linkage)
heatmap.title = 'Heatmap'
heatmap.colormap = heatmap.yellowBlackBlue
heatmap.column_labels = ['CFU', 'poly', 'unk', 'mys', 'int', 'mid']
heatmap.export('Heatmap_with_dendrograms.png')


"""
make dendrograms
leaves list converts linkage values back to expression data
use leaves to sort numpy arrays
"""