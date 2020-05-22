#!/bin/bash

dpkg -s $1 &> /dev/null

if [ $? == 0 ]; then
    echo "Package  is installed!"
else
    echo "Package  is NOT installed!"
fi