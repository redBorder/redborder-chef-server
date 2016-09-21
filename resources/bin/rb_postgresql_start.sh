#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env - PATH=$PATH \
/opt/opscode/embedded/bin/postgres -D /var/opt/opscode/postgresql/9.2/data
