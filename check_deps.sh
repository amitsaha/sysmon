#!/bin/bash

# check the dependencies and if not found, install them

deps="acpi python-pyudev python-django"
for dep in $deps
do
dpkg -s $dep >& /dev/null
if [[ $? != 0 ]]; then
    echo "Installing: $dep"
    sudo apt-get install $dep
fi
done
