#!/bin/bash

rootvr=`root-config --version`
if [[ ${rootvr:0:1} == "6" ]] ; then echo "Root version $rootvr is source"; else echo "ERROR: ROOT6 is needed"; fi

export ldir=`pwd`

