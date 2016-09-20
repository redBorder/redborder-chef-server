#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

/opt/opscode/bin/wait-for-rabbit

cd /opt/opscode/embedded/service/opscode-expander

exec env - PATH=$PATH HOME=/opt/opscode/embedded/service/opscode-expander \
/opt/opscode/embedded/bin/bundle exec /opt/opscode/embedded/service/opscode-expander/bin/opscode-expander-cluster -n 2 -c /var/opt/opscode/opscode-expander/etc/expander.rb

