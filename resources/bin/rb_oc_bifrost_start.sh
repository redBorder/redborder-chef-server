#!/bin/bash
exec 2>&1

export PATH=/opt/opscode/bin:/opt/opscode/embedded/bin:/usr/local/bin:/usr/local/sbin:/bin:/sbin:/usr/bin:/usr/sbin

umask 022

exec veil-env-helper --use-file -f /etc/opscode/private-chef-secrets.json -s oc_bifrost.sql_password -s oc_bifrost.superuser_id -- chpst -P -u opscode -U opscode env ERL_EPMD_ADDRESS=0.0.0.0 HOME=/var/opt/opscode/oc_bifrost /opt/opscode/embedded/service/oc_bifrost/bin/oc_bifrost foreground