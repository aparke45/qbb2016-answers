#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <metadata.csv> <replicatesdata.csv> <ctab_dir>

The purpose of this code is to create a timecourse plot of the presence of
 Sxl across developmental stages in females and males.

In addition, replicates can be added.

"""



import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_meta = pd.read_csv(sys.argv[1])
df_replicates = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]

# We need a list 

fem_Sxl = []

df_roi = df_meta["sex"] == "female"
for sample in df_meta[df_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df_roi2 = df["t_name"] == "FBtr0331261"
    fem_Sxl.append( df[ df_roi2 ]["FPKM"].values)

male_Sxl = []
df2_roi = df_meta["sex"] == "male"
for sample in df_meta[df2_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df2_roi2 = df["t_name"] == "FBtr0331261"
    male_Sxl.append( df[ df2_roi2 ]["FPKM"].values)



fem_rep = []
df3_roi = df_replicates["sex"] == "female"
for sample in df_replicates[df3_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df3_roi2 = df["t_name"] == "FBtr0331261"
    fem_rep.append( df[ df3_roi2 ]["FPKM"].values)
    
male_rep = []
df4_roi = df_replicates["sex"] == "male"
for sample in df_replicates[df4_roi]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table(filename)
    
    df4_roi2 = df["t_name"] == "FBtr0331261"
    male_rep.append( df[ df4_roi2 ]["FPKM"].values)


my_xticks = np.array([0,1,2,3,4,5,6,7,8])
dog = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

plt.figure()
plt.plot(fem_Sxl, 'r-', label ="fem_Sxl")
plt.plot(male_Sxl, 'b-', label="male_Sxl")
plt.plot([4,5,6,7], fem_rep, 'r.')
plt.plot([4,5,6,7], male_rep, 'b.')
plt.xticks( my_xticks, dog)
plt.ylim(1,300)
plt.legend()
plt.xlabel("Developmental Stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.title("Development Timecourse of Sxl in Male & Female Fly")
plt.savefig("timecourse_fem_male.png")
plt.close()