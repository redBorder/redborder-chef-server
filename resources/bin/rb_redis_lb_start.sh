#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env HOME="/opt/opscode/embedded/service/redis_lb" /opt/opscode/embedded/bin/redis-server /var/opt/opscode/redis_lb/etc/redis.conf



#!/bin/bash
exec 2>&1
PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin
exec /opt/opscode/embedded/bin/veil-env-helper -f /etc/opscode/private-chef-secrets.json -s REDIS_PASSWORD=redis_lb.password -- chpst -P -o 131071 -u opscode -U opscode -o 100000 env HOME="/var/opt/opscode/redis_lb" /opt/opscode/embedded/bin/redis-server /var/opt/opscode/redis_lb/etc/redis.conf --requirepass "${REDIS_PASSWORD}"
