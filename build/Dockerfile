# set the base image
FROM debian

# author
MAINTAINER Jim McManus

# extra metadata
LABEL version="1.0"
LABEL description="regin3db image with Dockerfile."

# update sources list
RUN apt-get clean

# install basic apps, one per line for better caching
RUN apt-get update && apt-get install -qy git \
    locales \
    nano \
    tmux \
    wget \
    curl \
    vim \
    lsb-release \
    gnupg2 \
    unzip 

# add users and groups
RUN groupadd -r -g 70 postgres && useradd --no-log-init -r -u 70 -g 70 postgres
RUN useradd --no-log-init -r -u 1324 data 
RUN usermod -a -G postgres data

# get postgres, postgis and timescaledb repos
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -c -s)-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN sh -c "echo 'deb https://packagecloud.io/timescale/timescaledb/debian/ `lsb_release -c -s` main' > /etc/apt/sources.list.d/timescaledb.list"
RUN wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | apt-key add -

# install postgres, postgis and timescaledb
RUN apt-get update && apt-get install -qy postgresql-11-postgis-3 \
    timescaledb-postgresql-11

# cleanup
RUN apt-get -qy autoremove

# add scripts to the container
ADD .bashrc /root/.bashrc
ADD .profile /root/.profile

# locales to UTF-8
RUN locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8

