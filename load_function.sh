#sudo docker exec -it region3db psql -U postgres -d postgres -f /var/lib/postgresql/data/funcs/st_tileenvelope.sql
sudo docker exec -it region3db psql -U postgres -d postgres -f /var/lib/postgresql/data/funcs/region3-function.sql
