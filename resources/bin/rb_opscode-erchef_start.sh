#!/bin/bash

/opt/opscode/bin/wait-for-rabbit

exec env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/opscode-erchef  /opt/opscode/embedded/service/opscode-erchef/bin/oc_erchef foreground

