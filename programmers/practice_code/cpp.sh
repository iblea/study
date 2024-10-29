#!/bin/bash

binName=ouput
clang++ --std=c++17 -Wall -g "fullcode.cpp" -o "${binName}"
if [ -f "$binName" ]; then
	./$binName
	rm -f $binName
else
	echo "compile error"
fi
