#!/bin/bash

ulimit -n 32768

exec env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/opscode-chef-mover /opt/opscode/embedded/service/opscode-chef-mover/bin/mover foreground

