docker run -ti --name region3db_container \
   -p 5434:5432 \
   --volume /projects/regionthree/ingestProcessing:/home/data \
   --volume /projects/regionthree/dockerstorage:/var/local/postgresql \
  region3db_image_test /bin/bash

