#!/bin/bash
exec 2>&1
umask 022

export GEM_PATH=/opt/opscode/embedded/service/gem/ruby/2.7.0
export GEM_HOME=/opt/opscode/embedded/service/gem/ruby/2.7.0
export PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

exec /opt/opscode/embedded/bin/veil-env-helper -f /etc/opscode/private-chef-secrets.json -s REDIS_PASSWORD=redis_lb.password -- env HOME="/var/opt/opscode/redis_lb" /opt/opscode/embedded/bin/redis-server /var/opt/opscode/redis_lb/etc/redis.conf --requirepass "${REDIS_PASSWORD}"
