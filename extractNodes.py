#!/home/jmcmanus/anaconda3/envs/surge/bin/python
# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port='5432' password='adcirc'")
cur = conn.cursor()
cur.execute("SELECT node, bathymetry, lon, lat FROM r3sim_fort_geom WHERE ST_Intersects(ST_MakeEnvelope(-76.0,39.0,-75.0,38.0, 4326),geom) ORDER BY node;")
geometry = cur.fetchall()
cur.close()
conn.close()

f = open('/home/jmcmanus/Work/Surge/MeshSoft/d3/simpleApp/static/subset_geom.csv','w')
f.write('node,bathymetry,longitude,latitude\n')

for geom in geometry:
    f.write(str(geom[0])+','+str(geom[1])+','+str(geom[2])+','+str(geom[3])+'\n')

f.close()
