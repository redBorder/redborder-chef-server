#!/bin/bash
exec 2>&1

umask 022

export PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

export GEM_PATH=/opt/opscode/embedded/service/gem/ruby/2.7.0 
export GEM_HOME=/opt/opscode/embedded/service/gem/ruby/2.7.0 

exec veil-env-helper --use-file -f /etc/opscode/private-chef-secrets.json -s chef-server.webui_pub_key -s opscode_erchef.sql_password -s bookshelf.access_key_id -s bookshelf.secret_access_key -s oc_bifrost.superuser_id -o data_collector.token -o ldap.bind_password -- chpst -P  -u opscode -U opscode env ERL_EPMD_ADDRESS=0.0.0.0 HOME=/var/opt/opscode/opscode-erchef /opt/opscode/embedded/service/opscode-erchef/bin/oc_erchef foreground
