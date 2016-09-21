#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env - PATH=$PATH \
DIR=/opt/opscode/embedded/service/oc_id \
RAILS_ENV=production \
PATH=/opt/opscode/embedded/bin:$PATH \
LD_LIBRARY_PATH=/opt/opscode/embedded/lib \
HOME=$DIR \
cd $DIR \
/opt/opscode/embedded/bin/bundle exec rails server -p 9090 -b 127.0.0.1

