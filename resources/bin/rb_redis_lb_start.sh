#!/bin/bash

exec env HOME="/var/opt/opscode/redis_lb" /opt/opscode/embedded/bin/redis-server /var/opt/opscode/redis_lb/etc/redis.conf

