#!/bin/bash
exec 2>&1

export PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec veil-env-helper --use-file -f /etc/opscode/private-chef-secrets.json -s bookshelf.access_key_id -s bookshelf.secret_access_key -o bookshelf.sql_password -- chpst -P -u opscode -U opscode env ERL_EPMD_ADDRESS=0.0.0.0 HOME=/var/opt/opscode/bookshelf GEM_PATH=/opt/opscode/embedded/service/gem/ruby/2.7.0/gems GEM_HOME=/opt/opscode/embedded/service/gem/ruby/2.7.0/gems /opt/opscode/embedded/service/bookshelf/bin/bookshelf foreground

