#!/bin/bash

exec env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/oc_bifrost /opt/opscode/embedded/service/oc_bifrost/bin/oc_bifrost foreground

