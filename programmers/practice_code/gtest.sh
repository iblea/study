#!/bin/bash

curpath=$(dirname $(realpath $0))
gtest_path=$(realpath $curpath/googletest)
echo $gtest_path

binName="gtest_output"

fileName=""
if [ $# -ge 1 ]; then
    fileName="$1"
else
    fileName="fullcode.cpp"
    # fileName="gtest_template.cpp"
fi

if [ ! -f $fileName ]; then
    echo "file not exist"
    exit 1
fi

# g++ -Wall -g \
#     -I $gtest_path/include \
#     -L $gtest_path/lib \
#     -o $binName $fileName \
#     -std=c++17 -pthread \
#     -lgtest -lgtest_main -lpthread

# g++
# /opt/homebrew/bin/g++-13

clang++ -Wall -g \
	-I $gtest_path/include \
	-L $gtest_path/lib \
	-std=c++17 \
	-o $binName $fileName \
	-lgtest -lgtest_main -lpthread

if [ -f "$binName" ]; then
	./$binName
	rm -f $binName
    if [ -d "$binName.dSYM/" ]; then
        rm -rf ./$binName.dSYM/
    fi
else
	echo "compile error"
fi
