#!/bin/bash
exec 2>&1

umask 022

DIR=/opt/opscode/embedded/service/oc_id
export RAILS_ENV=production
PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin
export LD_LIBRARY_PATH=/opt/opscode/embedded/lib
export HOME=$DIR

export GEM_PATH=/opt/opscode/embedded/service/gem/ruby/2.7.0 
export GEM_HOME=/opt/opscode/embedded/service/gem/ruby/2.7.0 

rm -f $DIR/tmp/pids/server.pid
cd $DIR

exec veil-env-helper -f /etc/opscode/private-chef-secrets.json --use-file -s chef-server.webui_key -s oc_id.sql_password -s oc_id.secret_key_base -- chpst -P -u opscode -U opscode /opt/opscode/embedded/bin/bundle exec bin/rails server -p 9090 -b 127.0.0.1
