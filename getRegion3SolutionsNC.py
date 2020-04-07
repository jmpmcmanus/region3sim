#!/home/jmcmanus/anaconda3/envs/surge/bin/python
# -*- coding: utf-8 -*-

import os, wget, sys

ftype = sys.argv[1]

f = open('files-thredds-'+ftype.strip(),'r')
files = f.readlines()
f.close()

for file in files:
    url = file.strip()
    filename = wget.download(url)
    prefix = "_".join(url.split('/')[7].split('_')[:2])

    os.rename(filename,'data/nc'+ftype+'/'+prefix+'_'+filename)
