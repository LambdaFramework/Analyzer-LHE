#!/bin/bash

set -e

#all=`ls ../samples/*`
#all=`ls ../samples/DiJetsDM_LO_*.lhe`
#all=`ls ../samples/BBbarDM_LO_*.lhe`
#all=`ls ../samples/DiJetsDM_LO_MZprime-1000_Mhs-150_Mchi-10_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph.lhe`
#all=`ls ../samples/BBbarDM_LO_MZprime-2500_Mhs-90_Mchi-300_gSM-0p25_gDM-1p0_th_0p01_13TeV-madgraph.lhe`

zip=0
#for all in HadronicDM-v1  Monojet-v1 VisibleZpDM-v1 VisiblehsDM-v1
for n in `ls ../samples/${all}/`
do
    echo $n
    if [ ${n: -7} == ".lhe.gz" ];then
	zip=1
	name=$(basename $n .lhe.gz)
	echo "Unzip $n..."
	gunzip $n
	echo "Making Tree on $name..."
	python lhe2root.py ../samples/$all/$name.lhe $name.root
    elif [ ${n: -4} == ".lhe" ];then
	name=$(basename $n .lhe)
	echo "Making Tree on $name..."
        python lhe2root.py ../samples/$all/$n $name.root
    else
	continue
    fi
done

#if [ zip==1 ];then
#    ./zip.sh
#fi
