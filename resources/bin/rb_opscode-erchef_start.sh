#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

/opt/opscode/bin/wait-for-rabbit

exec env ERL_EPMD_ADDRESS=0.0.0.0 HOME=/var/opt/opscode/opscode-erchef  /opt/opscode/embedded/service/opscode-erchef/bin/oc_erchef foreground
