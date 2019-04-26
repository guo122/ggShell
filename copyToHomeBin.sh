#!/bin/bash

src_array=(
	"src/cpmerge"
	"src/fad"
	"src/gitSS"
	"src/mmpic"
	"src/mmvv"
	"src/optionTest"
	"src/tkof"
	"src/tuon"
)

if [ -d ~/bin ] ; then
	for i in ${src_array[@]}
	do
		cp $i ~/bin
	done
fi
