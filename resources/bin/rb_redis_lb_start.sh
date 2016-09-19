#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env - PATH=$PATH \
chpst -P -o 131071 -u opscode -U opscode -o 100000 env HOME="/var/opt/opscode/redis_lb" /opt/opscode/embedded/bin/redis-server /var/opt/opscode/redis_lb/etc/redis.conf

