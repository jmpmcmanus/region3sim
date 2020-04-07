CREATE TABLE "r3sim_fort_geom"(
    node INTEGER,
    lon  NUMERIC,
    lat NUMERIC,
    bathymetry NUMERIC
);
ALTER TABLE r3sim_fort_geom ADD COLUMN geom geometry(POINT,4326);
CREATE INDEX r3sim_fort_geom_index ON r3sim_fort_geom USING SPGIST ( geom );
