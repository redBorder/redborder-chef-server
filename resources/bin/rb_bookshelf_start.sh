#!/bin/bash

exec env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/bookshelf /opt/opscode/embedded/service/bookshelf/bin/bookshelf foreground

