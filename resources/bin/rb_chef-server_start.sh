#!/bin/bash

chef_services="opscode-bookshelf opscode-oc_bifrost opscode-chef-mover opscode-expander opscode-postgresql opscode-redis_lb opscode-nginx opscode-oc_id opscode-erchef opscode-solr4 opscode-rabbitmq"

for i in $chef_services; do service $i start; done
