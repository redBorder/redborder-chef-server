#!/bin/bash

DIR=/opt/opscode/embedded/service/oc_id
export RAILS_ENV=production
export PATH=/opt/opscode/embedded/bin:$PATH
export LD_LIBRARY_PATH=/opt/opscode/embedded/lib
export HOME=$DIR

cd $DIR
exec /opt/opscode/embedded/bin/bundle exec rails server -p 9090 -b 127.0.0.1
