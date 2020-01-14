#!/bin/bash

src_array=(
	"src/cccto"
	"src/cpmerge"
	"src/fad"
	"src/ggBasicFunc"
	"src/ggitResetMaster"
	"src/ggitStatus"
	"src/ggitGetCurrentBranch"
	"src/ggitRemoteUrlSwap"
	"src/gitSS"
	"src/gpoo"
	"src/mmadd"
	"src/mmdel"
	"src/mmcut"
	"src/mmpic"
	"src/mmvv"
	"src/optionTest"
	"src/tkof"
	"src/tuon"
)

if [ -d ~/bin ] ; then
	echo -n "copy..."
	for i in ${src_array[@]}
	do
		cp $i ~/bin
	done
	echo "done"
else
	echo "no home bin dir"
fi
