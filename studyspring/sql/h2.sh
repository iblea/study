#!/bin/sh
# jdbc:h2:tcp://localhost/~/test
# add -webAllowOthers option in docker
dir=$(dirname "$0")
java -cp "$dir/h2-2.2.224.jar:$H2DRIVERS:$CLASSPATH" org.h2.tools.Console -webAllowOthers "$@"
