#!/bin/bash

/opt/opscode/bin/wait-for-rabbit

cd /opt/opscode/embedded/service/opscode-expander
export HOME=/opt/opscode/embedded/service/opscode-expander 

exec /opt/opscode/embedded/bin/bundle exec /opt/opscode/embedded/service/opscode-expander/bin/opscode-expander-cluster -n 2 -c /var/opt/opscode/opscode-expander/etc/expander.rb

