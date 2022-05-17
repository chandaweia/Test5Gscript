#!/bin/bash
#RUN COMMAND: ./run_perf.sh perf_gnb_20mbps.data
#OUTPUT: (1)perf_gnb_20mbps.data   and   (2)perf_gnb_20mbps.data-data.txt
echo $1
DIRPATH=/usr/local/cuidi/perfdata_v2
DIRTXT=$DIRPATH/perfreport
TIME=10

if [ $# != 1 ]; then
	echo "Missing number of parameters!"
	echo "Please input:./run_perf.sh [perf.data]"
	exit
fi

if [ ! -d $DIRPATH ];then
	mkdir $DIRPATH
else 
	echo "perf data will save to:"$DIRPATH/$1
fi

if [ ! -d $DIRTXT ];then
        mkdir $DIRTXT
else
        echo "perf report will save to:"$DIRTXT/$1-data.txt
fi

sudo perf record -a -F 99 -g -p $(pgrep nr-softmodem -d ',') -o $DIRPATH/$1 -- sleep $TIME

sudo perf report -i $DIRPATH/$1 --no-children > $DIRTXT/$1-data.txt




