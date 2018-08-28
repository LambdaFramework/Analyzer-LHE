#!/bin/bash

all=`ls ../samples/*`

for n in $all
do
    if [[ ! $n == *".lhe.gz"* ]]; then
	echo "gzip -c $n > $n.gz"
	gzip -c $n > $n".gz"
	rm $n
	#echo "gzip -c $n > $n.gz"
    fi
done
