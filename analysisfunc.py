from collections import namedtuple
import sys
import csv
from turtle import title
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
from builtins import str

def readcsv(file1,file2,file3):
    tmpfile3=file3+"_tmp.csv"
    fw=open(tmpfile3,"w")
    fw_final=open(file3,"w")
    titlehead="Overhead1,Overhead2,Command,Object,Symbol,Layer,Layer2,Layer3,Overhead1-Overhead2,Overhead1-Overhead2,,CPU1(all):72.26%,CPU1,CPU2(all)176.21%,CPU2,CPU1-CPU2\n"
    fw.write(titlehead)
    fw_final.write(titlehead)
    with open(file1) as f1:
        f_csv1 = csv.DictReader(f1)
        for row1 in f_csv1:
            flag=-1
            diffval=-1000
            with open(file2) as f2:
                f_csv2 = csv.DictReader(f2)
                strline=""
                for row2 in f_csv2:
                    #print("row1:",row1)
                    #print("row2:",row2)
                    if row1['Command']==row2['Command'] and row1['Object']==row2['Object'] and row1['Symbol']==row2['Symbol']:
                        diffval=float(row1['Overhead'].rstrip('%'))-float(row2['Overhead'].rstrip('%'))
                        if(diffval>=0):
                            strline=row1['Overhead']+","+row2['Overhead']+","+row2['Command']+","+row2['Object']+","+row2['Symbol']+","+row2['Layer']+","+row2['Layer2']+","+row2['Layer3']+","+str(diffval)+"%\n"
                        else:
                            strline=row1['Overhead']+","+row2['Overhead']+","+row2['Command']+","+row2['Object']+","+row2['Symbol']+","+row2['Layer']+","+row2['Layer2']+","+row2['Layer3']+","+","+str(diffval)+"%\n"

                        flag = 0
                        fw.write(strline)
                        fw_final.write(strline)
                        break

                # When a function exists in f1 but not in f2.
                if flag==-1:
                    strline=row1['Overhead']+","+"0%,"+row1['Command']+","+row1['Object']+","+row1['Symbol']+","+row1['Layer']+","+row1['Layer2']+","+row1['Layer3']+","+row1['Overhead']+"\n"
                    fw.write(strline)
                    fw_final.write(strline)
    fw.close()
    with open(file2) as f1:
        f_csv1 = csv.DictReader(f1)
        for row2 in f_csv1:
            flag=-1
            with open(tmpfile3) as f2:
                f_csv2 = csv.DictReader(f2)
                strline=""
                for row1 in f_csv2:
                    if row1['Overhead2']==row2['Overhead'] and row1['Command']==row2['Command'] and row1['Object']==row2['Object'] and row1['Symbol']==row2['Symbol']:
                        flag=0
                        break
            if flag == -1:    
                print(row2)
                #strline="0%,"+str(row2['Overhead'])+","+row2['Command']+","+row2['Object']+","+row2['Symbol']+","+row2['Layer']+","+row2['Layer2']+","+row2['Layer3']+","+",-"+row2['Overhead']+"\n"
                strline="0%,"+row2['Overhead']+","+row2['Command']+","+row2['Object']+","+row2['Symbol']+","+row2['Layer']+","+str(row2['Layer2'])+","+str(row2['Layer3'])+","+",-"+row2['Overhead']+"\n"
                fw_final.write(strline)
                
    fw_final.close()
    #f2.close()
    #f1.close()

#---------main---------
file1=str(sys.argv[1])
file2=str(sys.argv[2])
file3=str(sys.argv[3])
readcsv(file1,file2,file3)