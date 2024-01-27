#!/bin/bash

curpath=$(dirname $(realpath $0))
cd "$curpath"

if [ -f Main.class ]; then
    rm -f Main.class
fi

javac Main.java

if [ ! -f Main.class ]; then
    echo "Compile failed!"
    exit 1
fi

java Main
rm -f Main.class

exit 0