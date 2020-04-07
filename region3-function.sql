CREATE OR REPLACE
FUNCTION public.region3_sim_storms(z integer, x integer, y integer)
RETURNS bytea
AS $$
  bounds AS (
    SELECT ST_TileEnvelope(z, x, y) AS geom
  ),
  joined AS (
    SELECT Z.node, Z.zeta, Z.mask, Z.timestamp, G.bathymetry, G.geom
    FROM bp1_dp1r2b1c2h1l1_fort_8i AS Z
    INNER JOIN r3sim_fort_geom AS G ON (Z.node=G.node)
    WHERE Z.timestamp = '2000-09-04T06:00:00';
  ),
  mvtgeom AS (
    SELECT ST_AsMVTGeom(ST_Transform(j.geom, 3857), bounds.geom) AS geom,
      j.node, j.zeta, j.mask, j.timestamp, j.bathymetry
    FROM joined j, bounds
    WHERE ST_Intersects(j.vgeom, ST_Transform(bounds.geom, 26910))
  )
  SELECT ST_AsMVT(mvtgeom, 'public.region3_sim_storms') FROM mvtgeom
$$
LANGUAGE 'sql'
STABLE
PARALLEL SAFE;

COMMENT ON FUNCTION public.region3_sim_storms IS 'Given a tile address, storm name, and timestamp query database.';
