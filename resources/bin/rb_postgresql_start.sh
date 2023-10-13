#!/bin/bash
exec 2>&1
exec /opt/opscode/embedded/bin/postgres -D /var/opt/opscode/postgresql/13/data
