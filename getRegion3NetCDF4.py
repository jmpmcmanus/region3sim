#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, wget, sys

ftype = sys.argv[1]

f = open('files-thredds-'+ftype.strip(),'r')
files = f.readlines()
f.close()

dirpath = '/var/lib/postgresql/data/nc/'
os.chdir(dirpath)

for file in files:
    url = file.strip()
    filename = wget.download(url)
    prefix = "_".join(url.split('/')[7].split('_')[:2]).lower()

    os.rename(dirpath+filename,dirpath+prefix+'_'+filename)
