#!/bin/bash

exec /usr/bin/env ERL_EPMD_ADDRESS=127.0.0.1 HOME=/var/opt/opscode/rabbitmq /opt/opscode/embedded/bin/rabbitmq-server

