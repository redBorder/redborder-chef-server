#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env - PATH=$PATH \
chpst -P -u opscode -U opscode /usr/bin/env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/rabbitmq /opt/opscode/embedded/bin/rabbitmq-server

