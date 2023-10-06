#!/bin/bash

chef_services="opscode-bookshelf opscode-oc_bifrost opscode-postgresql opscode-redis_lb opscode-nginx opscode-oc_id opscode-erchef"

for i in $chef_services; do service $i start; done
