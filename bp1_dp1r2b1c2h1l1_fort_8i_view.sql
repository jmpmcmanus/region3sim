CREATE VIEW bp1_dp1r2b1c2h1l1_fort_8i_view AS
    SELECT Z.node, Z.zeta, Z.mask, Z.timestamp, G.bathymetry, G.geom
    FROM bp1_dp1r2b1c2h1l1_fort_8i AS Z
    INNER JOIN r3sim_fort_geom AS G ON (Z.node=G.node)
    WHERE Z.timestamp = '2000-09-04T06:00:00';
