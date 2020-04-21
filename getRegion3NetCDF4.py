#!/home/data/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, wget, sys

ftype = sys.argv[1]

f = open('files-thredds-'+ftype.strip(),'r')
files = f.readlines()
f.close()

for file in files:
    url = file.strip()
    filename = wget.download(url)
    prefix = "_".join(url.split('/')[7].split('_')[:2]).lower()

    os.rename(filename,'/home/jmpmcmanus/data/nc/'+prefix+'_'+filename)
