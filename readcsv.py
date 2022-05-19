#!/usr/bin/python3

from collections import namedtuple
from turtle import color
import drawgraphs
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def readCpuUsage(csvfile):
    ratelist=[]
    gnblist=[]
    culist=[]
    dulist=[]

    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            #print(row)
            if row['ID']=="Cuidi":
                ratelist.append(float(row['Rate'].rstrip('%')))
                gnblist.append(float(row['gNB-1ue'].rstrip('%')))
                culist.append(float(row['CU'].rstrip('%')))
                dulist.append(float(row['DU'].rstrip('%')))
    #f_csv.close()
    print("In readcsv!!")
    print(ratelist)
    return ratelist, gnblist, culist,dulist

def stacked_bargraph(labels, highlist, lowlist, otherlist):
    fix,ax = plt.subplots()
    print(labels)
    print(highlist)
    ax.bar(labels-1.5, highlist, 3, label="HIGH PHY-Emulated Radio")
    ax.bar(labels-1.5, lowlist, 3, bottom=highlist, label="LOW PHY-Emulated Radio")
    ax.bar(labels-1.5, otherlist, 3, bottom=lowlist, label='OTHERS-Emulated Radio')

    ax.bar(labels+1.5, highlist, 3, label="HIGH PHY-Real Radio")
    ax.bar(labels+1.5, lowlist, 3, bottom=highlist, label="LOW PHY-Real Radio")
    ax.bar(labels+1.5, otherlist, 3, bottom=lowlist, label='OTHERS-Real Radio')

    ax.set_xlabel("Sending Rate(mbps)")
    ax.set_ylabel("CPU Usage(%)")
    ax.set_title("CPU Usage Over Sending Rate(%)")
    ax.legend()
    plt.ylim(0,150)
    plt.show()

def readCpuUsage(csvfile):
    ratelist=[]
    highlist=[]
    lowlist=[]
    otherlist=[]
    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            ratelist.append(float(row['Rate'].rstrip('%')))
            highlist.append(float(row['HIGH PHY_CPU'].rstrip('%')))
            lowlist.append(float(row['LOW PHY_CPU'].rstrip('%')))
            otherlist.append(float(row['OTHERS_CPU'].rstrip('%')))
    ratelist=np.array(ratelist)
    stacked_bargraph(ratelist, highlist, lowlist, otherlist)

#For Experiment 2
#Called by readgnbvscudu_trend
def stacked_std_linegraph(labels, culist, dulist, cudulist, gnblist):
    print("stacked_std_linegraph")
    fix,ax = plt.subplots()

    ax.plot(labels, culist, label='CU', color='orange', marker='1', linestyle='solid')
    ax.plot(labels, dulist, label='DU', color='red', marker='2', linestyle='solid')
    ax.plot(labels, gnblist, label='GNB', color='darkcyan', marker='o', linestyle='solid')
    ax.set_ylim([-1,90])
    plt.show()

#For Experiment 2
#Call stacked_std_linegraph
def readgnbvscudu_trend(csvfile):
    ratelist=[]
    culist=[]
    dulist=[]
    cudulist=[]
    gnblist=[]
    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            ratelist.append(float(row['Rate(Mbps)'].rstrip('%')))
            culist.append(float(row['CU'].rstrip('%')))
            dulist.append(float(row['DU'].rstrip('%')))
            cudulist.append(float(row['CUDU'].rstrip('%')))
            gnblist.append(float(row['gNB-1ue'].rstrip('%')))
    stacked_std_linegraph(ratelist, culist, dulist, cudulist, gnblist)
#############main##############
"""file1="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/cuidi_CPUusage.csv"
file2="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/cuidi_CPUusage_gnb_rate.jpg"
ratelist, gnblist, culist, dulist=readCpuUsage(file1)
drawgraphs.bargraph_value(ratelist, gnblist, file2)
"""
#For Experiment 1
file1="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/rate_usage_stackedbar.csv"
readCpuUsage(file1)

#For Experiment 2
#file2="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/gnbvscudu_trend.csv"
#readgnbvscudu_trend(file2)