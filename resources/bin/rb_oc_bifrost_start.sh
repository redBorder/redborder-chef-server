#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env - PATH=$PATH \
env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/oc_bifrost /opt/opscode/embedded/service/oc_bifrost/bin/oc_bifrost foreground

