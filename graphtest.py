#!/usr/bin/python3

from cProfile import label
from collections import namedtuple
from tkinter import Frame, font
from turtle import color
#import drawgraphs
import sys
import csv
import numpy as np
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab  


matplotlib.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12,9)
plt.rc('font', size=25)
#plt.rcParams.update({
#    "figure.facecolor":  (1.0, 0.0, 0.0, 0.3),  # red   with alpha = 30%
#    "axes.facecolor":    (0.0, 1.0, 0.0, 0.5),  # green with alpha = 50%
#    "savefig.facecolor": (0.0, 0.0, 1.0, 0.2),  # blue  with alpha = 20%
#})
graphsdir="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/Graphs"


#% formatter something like '{:06}'

def export_legend(legend, filename="legend.png"):
    figpath=graphsdir+"/realvssimulation_separate_legend.png"
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(figpath, dpi="figure", bbox_inches=bbox)

#For Experiment 1
#TWO BARS in a graph: Emulated and Real Radio
def stacked_bargraph(labels, highlist, lowlist, otherlist,highlist2, lowlist2,otherlist2):
    plt.rcParams['figure.figsize'] = (12,8)
    fix,ax = plt.subplots()
    #plt.rcParams['font.size'] = 100
    print(labels)
    print(highlist)
    lowlist=np.array(lowlist)
    highlist=np.array(highlist)
    otherlist=np.array(otherlist)
    lowlist2=np.array(lowlist2)
    highlist2=np.array(highlist2)
    otherlist2=np.array(otherlist2)
    
    
    ax.bar(labels-1.5, lowlist2, 3, label="LOW PHY: Real Radio",color='lightcoral',edgecolor='k',hatch='/')
    ax.bar(labels-1.5, highlist2, 3, bottom=lowlist2, label="HIGH PHY: Real Radio",color='green',edgecolor='k',hatch='.')
    ax.bar(labels-1.5, otherlist2, 3, bottom=lowlist2+highlist2, label='(L2+L3+SYS): Real Radio',color='gold',edgecolor='k',hatch='\\')

    ax.bar(labels+1.5, lowlist, 3, label="LOW PHY: Emulated Radio",color='saddlebrown',edgecolor='k',hatch='-')
    ax.bar(labels+1.5, highlist, 3, bottom=lowlist, label="HIGH PHY: Emulated Radio",color='olive',edgecolor='k',hatch='|')
    ax.bar(labels+1.5, otherlist, 3, bottom=lowlist+highlist, label='(L2+L3+SYS): Emulated Radio',color='orange',edgecolor='k',hatch='x')
    ax.set_ylim(0,140)
    figpath=graphsdir+"/realvssimulation_separate.png"

    ax.set_xticks(labels)
    ax.set_xticklabels(labels)
    ax.set_xlabel("UE Throughput (Mbps)",fontweight='bold')
    ax.set_ylabel("CPU Usage (%)",fontweight='bold')
    
    #ax.set_title("CPU Usage: Emulated Radio vs Real Radio")
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    plt.grid(b=None)
    #plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')

    legend=ax.legend(loc='upper right',framealpha=0,fontsize=17)
    export_legend(legend)
    #plt.legend('')
    #plt.legend('')
    plt.legend('',frameon=False)
    #plt.savefig(figpath,transparent=True,dpi=500)
    
    plt.show()

def readCpuUsage2(csvfile):
    ratelist=[]
    highlist=[]
    lowlist=[]
    otherlist=[]
    highlist_ahan=[]
    lowlist_ahan=[]
    otherlist_ahan=[]
    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            if(row['ID']=="Cuidi"):   #Cuidi 
                ratelist.append(float(row['Rate'].rstrip('%')))
                highlist.append(float(row['HIGH PHY_CPU'].rstrip('%')))
                lowlist.append(float(row['LOW PHY_CPU'].rstrip('%')))
                otherlist.append(float(row['OTHERS_CPU'].rstrip('%')))
            elif(row['ID']=="Ahan"):    #Ahan
                highlist_ahan.append(float(row['HIGH PHY_CPU'].rstrip('%')))
                lowlist_ahan.append(float(row['LOW PHY_CPU'].rstrip('%')))
                otherlist_ahan.append(float(row['OTHERS_CPU'].rstrip('%')))
    ratelist=np.array(ratelist)
    stacked_bargraph(ratelist, highlist, lowlist, otherlist, highlist_ahan, lowlist_ahan, otherlist_ahan)  #posted in paper

    #For Experiment 1 in Presentation
file1="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/rate_usage_stackedbarc_emuvsreal_ahan.csv"  #posted in paper
readCpuUsage2(file1)