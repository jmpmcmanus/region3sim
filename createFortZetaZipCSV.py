#!/home/data/anaconda3/bin/python
# -*- coding: utf-8 -*-

import os, glob
import xarray as xr
import pandas as pd
import numpy as np
from datetime import datetime
from zipfile import ZipFile
import warnings
warnings.filterwarnings("error")

def createZipFile(dirpath, infile):
    if len([f for f in glob.glob(dirpath+"zip/"+"csvfort")]) == 0:
        os.mkdir(dirpath+"zip/"+"csvfort")

    with xr.open_dataset(infile) as nc:
        startdate = datetime(2000,9,1,0,0,0)
        startsecond = datetime.timestamp(startdate)

        time = nc.variables['time'][:].data
        tindex = np.where(time > 1.5995402557e-314)[0]
        time = nc.variables['time'][tindex].data.astype(int)
        lon =nc.variables['x'][:].data

        ntime = len(time)
        ncells = len(lon)
        node = np.arange(ncells)

        for i in range(ntime):
            outzipfile = ZipFile(dirpath+"zip/"+".".join(infile.split('/')[len(infile.split('/'))-1].split('.')[0:2])+'.zip','a')

            try:
                zeta = nc.variables['zeta'][i,:]
            except RuntimeWarning:
                outzipfile.close()
                sys.exit('*** DeprecationWarning: elementwise comparison failed; this will raise an error in the future.')

            zeta_mask = zeta.mask
            zeta_data = zeta.data
            zeta_fill = zeta.fill_value
            findex = np.where(zeta_data==zeta_fill)
            zeta_data[findex] = np.nan

            timestamp = np.array([datetime.fromtimestamp(startsecond+time[i]).strftime("%Y-%m-%dT%H:%M:%S")] * ncells)

            df = pd.DataFrame({'node': node, 'zeta': zeta_data, 'mask': zeta_mask, 'timestamp': timestamp}, columns=['node', 'zeta', 'mask', 'timestamp'])

            outcsvfile = "_".join(infile.split('/')[len(infile.split('/'))-1].split('_')[0:2]) + '_' + \
                  datetime.fromtimestamp(startsecond+time[i]).strftime("%Y-%m-%dT%H-%M-%S") + \
                  '.fort.63_mod.csv'
            df.to_csv(dirpath+"zip/"+'csvfort/'+outcsvfile, encoding='utf-8', header=True, index=False)
            outzipfile.write(dirpath+"zip/"+'csvfort/'+outcsvfile)
            os.remove(dirpath+"zip/"+'csvfort/'+outcsvfile)

            outzipfile.close()

dirpath = '/home/data/'
infiles = [f for f in glob.glob(dirpath+"nc/"+"*.nc")]
infiles.sort()
infile = infiles[0]
#for infile in infiles:
createZipFile(dirpath, infile.strip())

