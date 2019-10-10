#!/bin/bash

src_array=(
	"src/cpmerge"
	"src/fad"
	"src/ggitResetMaster"
	"src/ggitStatus"
	"src/ggitGetCurrentBranch"
	"src/gitSS"
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
