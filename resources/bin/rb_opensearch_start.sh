#!/bin/sh
exec 2>&1

ulimit -n 65536

export ES_HOME=/var/opt/opscode/opensearch            #/var/opt/opscode/elasticsearch
export ES_DATA=/var/opt/opscode/opensearch/data       #/var/opt/opscode/elasticsearch/data

export JAVA_HOME=/opt/opscode/embedded/open-jre/
export ES_PATH_CONF=/var/opt/opscode/opensearch/config
export PATH=/opt/opscode/embedded/bin:$JAVA_HOME/bin:$ES_HOME:$PATH #/opt/opscode/embedded/bin

export TMPDIR=/var/opt/opscode/opensearch/tmp
export ES_TMPDIR=/var/opt/opscode/opensearch/tmp

export GEM_PATH=/opt/opscode/embedded/service/gem/ruby/2.7.0 
export GEM_HOME=/opt/opscode/embedded/service/gem/ruby/2.7.0 

cd $ES_HOME
exec chpst -P -u opscode -U opscode /opt/opscode/embedded/opensearch/bin/opensearch