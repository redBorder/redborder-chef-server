#!/bin/bash

PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec env ERL_EPMD_ADDRESS=0.0.0.0 HOME=/var/opt/opscode/bookshelf /opt/opscode/embedded/service/bookshelf/bin/bookshelf foreground
