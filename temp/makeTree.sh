#!/bin/bash

lheDir='LHE/'

set -e

for n in `ls $lheDir`
do
    echo $n
    if [ ${n: -7} == ".lhe.gz" ];then
	name=$(basename $n .lhe.gz)
	echo "Unzip $n..."
	gunzip --keep ${lheDir}/$n
	echo "Making Tree on $name..."
	python ntupler.py ${lheDir}/$name.lhe Ntuples/$name.root
	rm ${lheDir}/$name.lhe
    else
	name=$(basename $n .lhe)
	echo "Making Tree on $name..."
	python ntupler.py ${lheDir}/$name.lhe Ntuples/$name.root
	echo "Done"
    fi
done
