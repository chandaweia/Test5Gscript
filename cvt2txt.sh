#!/bin/bash 
RESULT=./test_report/$2
echo "time,Transfer,Bandwidth,Units,Jitter,Lost,Total" > $RESULT

#[ ID]

function write_data()
{
	echo "$1,$8,$9,${10},${12},${13}"
	echo "bianliang shuliang:"$#
	if [[ $# != 14 ]]
	then
		return
	else
			echo "$1,$8,$9,${10},${12},${13}" >> $RESULT
	fi

}

function readfile()
{
	echo "file:$1"
	count=0
	flag=0
	while read line
	do
		if [[ $line =~ ID] ]]
		then
			flag=1
			continue
		fi
		if [[ $line =~ 3] ]] && [[ $flag == 1 ]]
		then
			echo "chuanru:"$line
			write_data $count $line
			let count+=1
		fi


	done < $1
}

function readdir()
{
	echo $DIR
	for file in $DIR/*.txt
	do
		if test -f $file
		then
			echo $file
			readfile $file
		fi
	done
}

echo "file:$1"
echo "save to:$2"
readfile $1
