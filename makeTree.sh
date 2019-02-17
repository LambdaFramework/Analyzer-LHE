#!/bin/bash

set -e

for n in `ls Events/`
do
    echo $n
    if [ ${n: -7} == ".lhe.gz" ];then
	name=$(basename $n .lhe.gz)
	echo "Unzip $n..."
	gunzip --keep Events/$n
	echo "Making Tree on $name..."
	python ntupler.py Events/$name.lhe Ntuples/$name.root
	rm Events/$name.lhe
    else
	continue
    fi
done
