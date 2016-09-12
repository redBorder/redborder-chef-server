#!/bin/bash

chef_services="bookshelf oc_bifrost opscode-chef-mover opscode-expander postgresql redis_lb nginx oc_id opscode-erchef opscode-solr4 rabbitmq"

for i in $chef_services; do service $i start; done

