#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

ulimit -c 0
ulimit -d unlimited
ulimit -e 0
ulimit -f unlimited
ulimit -i 62793
ulimit -l 64
ulimit -m unlimited
# WARNING: Increasing the global file descriptor limit increases RAM
# consumption on startup dramatically!
ulimit -n 50000
ulimit -q 819200
ulimit -r 0
ulimit -s 10240
ulimit -t unlimited
ulimit -u unlimited
ulimit -v unlimited
ulimit -x unlimited
echo "1000000" > /proc/sys/fs/file-max

umask 022

exec env - PATH=$PATH \
runsv /opt/opscode/sv/nginx
