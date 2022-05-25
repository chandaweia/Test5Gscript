#/bin/bash
#RUN COMMAND: ./run_perf.sh perf_gnb_1ue_4mbps_dl.data cpu_1_ue_4_mbps_ul_gnb.txt 
#OUTPUT: (1)perf_gnb_1ue_4mbps_dl.data   and   (2)perf_gnb_1ue_4mbps_dl.data-data.txt
#OUTPUT: cpu_1_ue_4_mbps_ul_gnb.txt

CURPATH=`pwd`/DataTest
DIRPATH=$CURPATH/perfdata_test
DIRTXT=$CURPATH/perfreport_test
CPUDIR=$CURPATH/cpuusage_test
TIME=10

curDate=`date +%Y%m%d%H%M%S`
datafile=$DIRPATH/$1-$curDate
datareportfile=$DIRTXT/$1-$curDate-data.txt
cpufile=$CPUDIR/$2-$curDate.txt

echo $curDate
if [ $# != 2 ]; then
	echo "Missing number of parameters!"
	echo "Please input:./run_perf_cpu.sh [perf.data] [cpu.txt]"
	echo "	eg. ./run_perf_cpu.sh perf_gnb_1ue_4mbps_dl.data cpu_gnb_1ue_4mbps_dl.txt"
	exit
fi

if [ ! -d $CURPATH ];then
        mkdir $CURPATH
fi

if [ ! -d $DIRPATH ];then
	mkdir $DIRPATH
fi
echo "perf data will save to:"$datafile

if [ ! -d $DIRTXT ];then
        mkdir $DIRTXT
fi
echo "perf report will save to:"$datareportfile

sudo perf record -a -F 99 -g -p $(pgrep nr-softmodem -d ',') -o $datafile -- sleep $TIME

sudo perf report -i $datafile --no-children > $datareportfile

if [ ! -d $CPUDIR ];then
        mkdir $CPUDIR
fi
echo "CPU Usage Record will save to:"$cpufile

python monitor_cpuusage.py $TIME > $cpufile

