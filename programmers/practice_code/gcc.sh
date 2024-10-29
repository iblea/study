#!/bin/bash

filename=fullcode.c

gcc -Wall -g -o test fullcode.c

./test
rm -rf test
