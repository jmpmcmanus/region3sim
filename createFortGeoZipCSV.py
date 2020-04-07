#!/home/jmcmanus/anaconda3/envs/surge/bin/python
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

    outcsvfile = 'data/Region3Geo.csv'
    df.to_csv(outcsvfile, encoding='utf-8', header=True, index=False)


dirpath = 'data/ncfort/'
infile = 'BP1_dp1r1b1c1h1l1_fort.63_mod.nc'
createZipFile(dirpath+infile)

