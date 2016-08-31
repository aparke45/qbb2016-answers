#!/usr/bin/env python

# This is a python script for identifier mapping.  There are two options for this script.  If the argument -h is included while running the script, a "." will print in places when there is no match of the FlyBase IDs between the mapping file and the .ctab file.  If the argument -a is included while running the script, nothing will print when there is no match of the FlyBase IDs between the mapping file and the .ctab file.

import sys

dic = {}

opt = sys.argv[1]
file = open("/Users/cmdb/qbb2016-answers/day2-homework/flybase_uniprot_ids.out")

for line in file.readlines():
    c = line.split()
    fly = c[1]
    uniprot = c[0]
    dic[fly] = uniprot
 
    
#To search the dictionary for matches to the keys. This will print the value for the keys, if matches are found.
if opt == "-h":
    for line in open("/Users/cmdb/data/fastq/t_data.ctab"):
        f = line.split()
        d = f[8]
        if d in dic:
            print dic[d] and line
    else:
        print "."

if opt == "-a":
    for line in open("/Users/cmdb/data/fastq/t_data.ctab"):
        f = line.split()
        d = f[8]
        if d in dic:
            print dic[d] and line
        else:
            continue
    