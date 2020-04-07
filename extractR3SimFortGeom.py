#!/home/jmcmanus/anaconda3/envs/surge/bin/python
# -*- coding: utf-8 -*-

import psycopg2, json

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' port='5432' password='adcirc'")
cur = conn.cursor()

cur.execute("SELECT node, bathymetry, lon, lat FROM r3sim_fort_geom ORDER BY node;")
nodes = cur.fetchall()
cur.close()
conn.close()

f = open('region3sim_fort_geom.csv','w')
f.write('node,bathymetry,lon,lat\n')

for node in nodes:
    f.write(str(node[0])+','+str(node[1])+','+str(node[2])+','+str(node[3])+'\n')

f.close()
