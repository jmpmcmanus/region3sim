CONTAINER="region3db_container"
DB="postgres"
TABLE="r3sim_fort_geom"

sudo docker exec -u postgres ${CONTAINER} psql -d ${DB} -f '/home/data/sql/region3db_fort_geo.sql'
sudo docker exec -u postgres ${CONTAINER} psql -d ${DB} -c "\COPY ${TABLE} FROM '/home/data/csv/Region3Geo.csv' DELIMITER ',' CSV HEADER"
sudo docker exec -u postgres ${CONTAINER} psql -d ${DB} -f '/home/data/sql/region3db_fort_geom.sql'
