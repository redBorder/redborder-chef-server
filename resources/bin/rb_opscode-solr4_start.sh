#!/bin/bash

/opt/opscode/bin/wait-for-rabbit

cd /opt/opscode/embedded/service/opscode-solr4/jetty

ulimit -n 50000

exec /usr/bin/env PATH=/opt/opscode/embedded/bin:/opt/opscode/bin:/opt/opscode/embedded/jre/bin:$PATH JAVA_HOME=/opt/opscode/embedded/jre java -Xmx947M -Xms947M  -XX:NewSize=59M -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -Xloggc:/var/log/opscode/opscode-solr4/gclog.log -verbose:gc -XX:+PrintHeapAtGC -XX:+PrintGCTimeStamps -XX:+PrintGCDetails -XX:+PrintGCApplicationStoppedTime -XX:+PrintGCApplicationConcurrentTime -XX:+PrintTenuringDistribution -Dsolr.data.dir=/var/opt/opscode/opscode-solr4/data -Dsolr.solr.home=/var/opt/opscode/opscode-solr4/home -Djava.io.tmpdir=/var/opt/opscode/opscode-solr4/ -server -jar '/opt/opscode/embedded/service/opscode-solr4/jetty/start.jar'

