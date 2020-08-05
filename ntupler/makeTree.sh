#!/bin/bash

eventDir='Events/'

set -e

for n in `ls $eventDir`
do
    echo $n
    if [ ${n: -7} == ".lhe.gz" ];then
	name=$(basename $n .lhe.gz)
	echo "Unzip $n..."
	gunzip --keep ${eventDir}/$n
	echo "Making Tree on $name..."
	python ntupler.py ${eventDir}/$name.lhe Ntuples/$name.root
	rm ${eventDir}/$name.lhe
    else
	name=$(basename $n .lhe)
	echo "Making Tree on $name..."
	python ntupler.py ${eventDir}/$name.lhe Ntuples/$name.root
	echo "Done"
	rm ${eventDir}/$name.lhe
    fi
done
