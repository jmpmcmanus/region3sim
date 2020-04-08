#!/home/jmpmcmanus/anaconda3/bin/python
# -*- coding: utf-8 -*-

import netCDF4, os
import pandas as pd
import numpy as np

def createZipFile(infile):
    nc=netCDF4.Dataset(infile)

    lon =nc.variables['x'][:].data
    lat = nc.variables['y'][:].data
    bathymetry = nc.variables['depth'][:].data

    ncells = len(lon)
    node = np.arange(ncells)

    df = pd.DataFrame({'node': node, 'lon': lon, 'lat': lat, 'bathymetry': bathymetry}, columns=['node', 'lon', 'lat', 'bathymetry'])

    outcsvfile = '/home/jmpmcmanus/data/csv/Region3Geo.csv'
    df.to_csv(outcsvfile, encoding='utf-8', header=True, index=False)


dirpath = '/home/jmpmcmanus/data/nc/'
infile = 'bp1_dp1r2b1c2h1l1_fort.63_mod.nc'
createZipFile(dirpath+infile)

