#!/bin/bash

repos_array=("guo122/zTime" 
			"guo122/ggShell" 
			"guo122/ssNotes" 
			"guo122/YellowS")

for i in ${repos_array[@]} ; do
	if [ "$1" != "" ] ; then
		outputPath=${1}
	else
		outputPath="./tmpGitClone/"
	fi
	
	git clone https://github.com/${i}.git ${outputPath}/${i}
done
