SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "r3sim_fort_temp" (
"node" integer,
"stormid" integer,
"zeta" numeric,
"mask" character varying(10), 
"timestamp"  date, 
"bathymetry" numeric);
ALTER TABLE r3sim_fort_temp ADD COLUMN geom geometry(POINT,4326);
COMMIT;

INSERT INTO r3sim_fort_temp 
    SELECT Z.node, Z.stormid, Z.zeta, Z.mask, Z.timestamp, G.bathymetry, G.geom
    FROM bp1_dp1r1b1c1h1l1_fort_8i AS Z
    INNER JOIN r3sim_fort_geom AS G ON (Z.node=G.node)
    WHERE Z.timestamp = '2000-09-05 02:00:00' AND Z.stormid = 0;

UPDATE r3sim_fort_temp
SET zeta = 'NaN'
WHERE
    mask = 'True';
