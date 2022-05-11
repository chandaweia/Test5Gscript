import sys
import os
import psutil
import thread
import time
from subprocess import check_output

#----PreRequirement to use the script-------
#pip install psutil

times=int(sys.argv[1])
#PID=int(sys.argv[1])

def get_pid(name):
    return map(int,check_output(["pidof",name]).split())

def getcpu(pid):
    p = psutil.Process(pid)

    usage=0
    for i in range(times):
        cpures=p.cpu_percent(interval=1)
        usage+=cpures
        print("pid:{0},time:{1},cpu ratio:{2}".format(pid,i,cpures))

    avgusage=round(usage/times,2)
    print("--------Result--------pid:{0},avg usage:{1}%".format(pid, avgusage))

#---------------main()--------------------
pids=get_pid('nr-softmodem')
print(pids)
print("len(pids)",len(pids))
try:
    #for i in range(len(pids)):
        thread.start_new_thread(getcpu, (pids[0],))
        thread.start_new_thread(getcpu, (pids[1],))
except:
   print "Error: unable to start thread"
while 1:
    pass
