#!/bin/bash

# clean up all .pyc files
for file in `find . -name *.pyc`
do
rm $file
done

# backup files
for file in `find . -name *~`
do
rm $file
done
