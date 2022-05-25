#!/usr/bin/python3

from cProfile import label
from collections import namedtuple
from tkinter import font
from turtle import color
import drawgraphs
import sys
import csv
import numpy as np
import pandas as pd
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12,9)
plt.rc('font', size=25)
#plt.rcParams.update({
#    "figure.facecolor":  (1.0, 0.0, 0.0, 0.3),  # red   with alpha = 30%
#    "axes.facecolor":    (0.0, 1.0, 0.0, 0.5),  # green with alpha = 50%
#    "savefig.facecolor": (0.0, 0.0, 1.0, 0.2),  # blue  with alpha = 20%
#})
graphsdir="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/Graphs"
#plt.rcdefaults()

#For Experiment 1
def stacked_bargraph(labels, highlist, lowlist, otherlist,highlist2, lowlist2,otherlist2):
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
    
    ax.bar(labels-1.5, lowlist2, 3, label="LOW PHY-Real Radio",color='red',edgecolor='k',hatch='////')
    ax.bar(labels-1.5, highlist2, 3, bottom=lowlist2, label="HIGH PHY-Real Radio",color='limegreen',edgecolor='k',hatch='....')
    ax.bar(labels-1.5, otherlist2, 3, bottom=lowlist2+highlist2, label='(L2+L3)-Real Radio',color='mediumslateblue',edgecolor='k',hatch='\\\\\\\\')

    ax.bar(labels+1.5, lowlist, 3, label="LOW PHY-Simulated Radio",color='red',edgecolor='k',hatch='----')
    ax.bar(labels+1.5, highlist, 3, bottom=lowlist, label="HIGH PHY-Simulated Radio",color='limegreen',edgecolor='k',hatch='++++')
    ax.bar(labels+1.5, otherlist, 3, bottom=lowlist+highlist, label='(L2+L3)-Simulated Radio',color='mediumslateblue',edgecolor='k',hatch='xxxx')

    ax.set_xticks(labels)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Sending Rate(Mbps)",fontweight='bold')
    ax.set_ylabel("CPU Usage(%)",fontweight='bold')
    ax.set_ylim(0,150)
    #ax.set_title("CPU Usage: Emulated Radio vs Real Radio")
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    
    #plt.ylim(0,150)
    figpath=graphsdir+"/realvssimulation.pdf"

    #ax.set_facecolor('transparent')
    ax.legend(loc='upper right',framealpha=0.8,fontsize=17)
    #ax.set_facecolor("transparent")
    #ax.set(facecolor = "transparent")
    plt.savefig(figpath,transparent=True)
    plt.show()


#For Experiment 1
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
            if(row['ID']=="Cuidi"):
                ratelist.append(float(row['Rate'].rstrip('%')))
                highlist.append(float(row['HIGH PHY_CPU'].rstrip('%')))
                lowlist.append(float(row['LOW PHY_CPU'].rstrip('%')))
                otherlist.append(float(row['OTHERS_CPU'].rstrip('%')))
            elif(row['ID']=="Ahan"):
                highlist_ahan.append(float(row['HIGH PHY_CPU'].rstrip('%')))
                lowlist_ahan.append(float(row['LOW PHY_CPU'].rstrip('%')))
                otherlist_ahan.append(float(row['OTHERS_CPU'].rstrip('%')))
    ratelist=np.array(ratelist)
    stacked_bargraph(ratelist, highlist, lowlist, otherlist, highlist_ahan, lowlist_ahan, otherlist_ahan)

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
def stacked_std_linegraph2(labels, culist, dulist, cudulist, gnblist):
    print("stacked_std_linegraph")

    plt.plot(labels, culist, label='CU', color='orange', marker='x', linestyle='solid', linewidth=2)
    plt.plot(labels, dulist, label='DU', color='red', marker='v', linestyle='solid', linewidth=2)
    plt.plot(labels, gnblist, label='GNB', color='darkcyan', marker='o', linestyle='solid', linewidth=2)
    #plt.set_ylim([-1,90])
    plt.xlabel("Sending Rate(Mbps)")
    plt.ylim(0, 90)
    plt.ylabel("CPU Usage(%)")
    plt.legend(loc="upper left")
    #plt.title("CPU Usage of CU/DU and gNB")
    #plt.grid(color = 'green', linestyle = '-', linewidth = 0.5)
    #ax.set(facecolor = "transparent")
    #plt.grid(True,color='black',linestyle = '--', linewidth = 0.5)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    plt.savefig(graphsdir+"/linegraph.pdf", transparent=True)
    plt.box()
    plt.show()

def stacked_std_linegraph3(labels, culist, dulist, cudulist, gnblist):
    print("stacked_std_linegraph")
    #fig=plt.figure()
    #ax=fig.add_subplot(111)
    fig,ax=plt.subplots()
    cu=ax.plot(labels, culist, label='CU', color='limegreen', marker='x', linestyle='solid', linewidth=3,markersize=14)
    ax.plot(labels, dulist, label='DU', color='red', marker='v', linestyle='solid', linewidth=3,markersize=14)
    ax.plot(labels, gnblist, label='GNB', color='darkcyan', marker='o', linestyle='solid', linewidth=3,markersize=14)

    #plt.title("CPU Usage of CU/DU and gNB")
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.set_xlabel("Sending Rate(Mbps)",fontweight='bold')
    ax.set_ylabel("CPU Usage(%)",fontweight='bold')
    ax.set_ylim(0,90)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    plt.legend(framealpha=0.8,fontsize=22)
    plt.savefig(graphsdir+"/CPU_CUvsDUvsgNB.pdf", transparent=True)
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
            
    stacked_std_linegraph3(ratelist, culist, dulist, cudulist, gnblist)

#For Experiment 3
def linegraph_latency(labels,cudu_avg_rtt,gnb_avg_rtt,cudu_min_rtt,gnb_min_rtt,cudu_max_rtt,gnb_max_rtt):
    print(labels)
    plt.plot(labels, cudu_avg_rtt, label='CUDU', color='orange', marker='1', linestyle='solid')
    plt.plot(labels, gnb_avg_rtt, label='gNB', color='darkcyan', marker='2', linestyle='solid')
    plt.xlabel("Sending Rate(Mbps)")
    plt.ylim(10, 20)
    plt.ylabel("RTT(ms)")
    plt.legend(loc="upper left")
    #plt.title("Latency of CUDU and gNB")
    plt.show()
#For Experiment 3
def smoothline_latency(labels, cudu_avg_rtt,gnb_avg_rtt,cudu_min_rtt,gnb_min_rtt,cudu_max_rtt,gnb_max_rtt):
    from scipy.interpolate import make_interp_spline
    xnew=np.linspace(labels.min(), labels.max(), 300)
    cudu_avg_line=make_interp_spline(labels,cudu_avg_rtt)(xnew)
    gnb_avg_line=make_interp_spline(labels,gnb_avg_rtt)(xnew)
    #cudu_min_line=make_interp_spline(labels,cudu_min_rtt)(xnew)
    #gnb_min_line=make_interp_spline(labels,gnb_min_rtt)(xnew)
    #cudu_max_line=make_interp_spline(labels,cudu_max_rtt)(xnew)
    #gnb_max_line=make_interp_spline(labels,gnb_max_rtt)(xnew)
    plt.plot(xnew,cudu_avg_line,label='CUDU',color='orange')#
    plt.plot(xnew,gnb_avg_line,label='gNB',color='darkcyan')#,color='lightcoral'
    #plt.plot(xnew,cudu_min_line,label='CUDU-min',color='orange')#,color='deepskyblue'
    #plt.plot(xnew,gnb_min_line,label='gNB-min',color='cyan')#,color='tomato'
    #plt.plot(xnew,cudu_max_line,label='CUDU-max',color='fuchsia')#,color='blue'
    #plt.plot(xnew,gnb_max_line,label='gNB-max',color='navy')#,color='red'
    plt.xlabel("Sending Rate(Mbps)")
    #plt.ylim(10, 20)
    plt.ylabel("RTT(ms)")
    plt.legend(loc="upper left")
    plt.title("Latency: CUDU vs gNB")
    plt.show()

    #For Experiment 3
def std_latency(labels,cudu_avg_rtt,gnb_avg_rtt,cudu_std_rtt,gnb_std_rtt):
    x=labels
    plt.rc('font', size=18)
    plt.rcParams['figure.figsize'] = (9,9)
    plt.errorbar(x,cudu_avg_rtt,cudu_std_rtt,color='orange',linestyle='solid',marker='o',label='CU+DU')
    plt.errorbar(x,gnb_avg_rtt,gnb_std_rtt,color='darkcyan',linestyle='solid',marker='o',label='gNB')
    plt.xlabel("Sending Rate(Mbps)")
    plt.ylabel("RTT(ms)")
    plt.ylim(0,20)
    plt.legend()
    fignm=graphsdir+"/std_latency.pdf"
    plt.savefig(fignm)
    plt.show()

def std_latency2(labels,cudu_avg_rtt,gnb_avg_rtt,cudu_std_rtt,gnb_std_rtt):
    plt.rcParams['figure.figsize'] = (9,9)
    plt.rc('font', size=38)
    fig,ax=plt.subplots()
    fig.subplots_adjust(bottom=0.17)
    fig.subplots_adjust(left=0.17)
    x=labels
    ax.errorbar(x,cudu_avg_rtt,cudu_std_rtt,color='red',linestyle='solid',marker='o',label='CU+DU',linewidth=3,markersize=14)
    ax.errorbar(x,gnb_avg_rtt,gnb_std_rtt,color='blue',linestyle='solid',marker='x',label='gNB',linewidth=3,markersize=14)
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.set_xlabel("Sending Rate(Mbps)",fontweight='bold')
    ax.set_ylabel("RTT(ms)",fontweight='bold')
    ax.set_ylim(0,25)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    ax.legend(loc='lower left',framealpha=0.8,fontsize=32)
    #ax.xlabel("Sending Rate(Mbps)")
    #plt.ylabel("RTT(ms)")
    #plt.ylim(0,20)
    fignm=graphsdir+"/std_latency_extra_errorbar.pdf"
    plt.savefig(fignm, transparent=True)
    plt.show()

def std_latency2_extralatency(labels,cudu_avg_rtt,gnb_avg_rtt,cudu_std_rtt,gnb_std_rtt):
    plt.rcParams['figure.figsize'] = (9,9)
    
    plt.rc('font', size=38)
    x=labels
    fig,ax=plt.subplots()
    fig.subplots_adjust(bottom=0.17)
    fig.subplots_adjust(left=0.17)
    
    
    cudu_avg_rtt=np.array(cudu_avg_rtt)
    ax.plot(x,cudu_avg_rtt+5,color='red',linestyle='solid',marker='o',label='CU+DU',linewidth=3,markersize=14)
    ax.plot(x,gnb_avg_rtt,color='blue',linestyle='solid',marker='x',label='gNB',linewidth=3,markersize=14)
    #ax.errorbar(x,cudu_avg_rtt,cudu_std_rtt,color='red',linestyle='solid',marker='o',label='CU+DU',linewidth=3,markersize=14)
    #ax.errorbar(x,gnb_avg_rtt,gnb_std_rtt,color='blue',linestyle='solid',marker='x',label='gNB',linewidth=3,markersize=14)
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.set_xlabel("Sending Rate(Mbps)",fontweight='bold')
    ax.set_ylabel("RTT(ms)",fontweight='bold')
    ax.set_ylim(0,30)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    ax.legend(loc='lower left',framealpha=0.8,fontsize=32)
    #ax.xlabel("Sending Rate(Mbps)")
    #plt.ylabel("RTT(ms)")
    #plt.ylim(0,20)
    fignm=graphsdir+"/std_latency_extra.pdf"
    plt.savefig(fignm, transparent=True)
    plt.show()

#For Experiment 3
def readlatencycsv(csvfile):
    ratelist=[]
    cudu_avg_rtt=[]
    gnb_avg_rtt=[]
    cudu_min_rtt=[]
    gnb_min_rtt=[]
    cudu_max_rtt=[]
    gnb_max_rtt=[]
    cudu_std_rtt=[]
    gnb_std_rtt=[]
    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)
            if(row['ID']=="Ahan"):
                if row['Version']=="cudu" and row['UEs']=="1":
                    print(row)
                    ratelist.append(int(row['Rate(Mbps)']))
                    cudu_avg_rtt.append(float(row['avg rtt(ms)']))
                    cudu_min_rtt.append(float(row['min rtt(ms)']))
                    cudu_max_rtt.append(float(row['max rtt(ms)']))
                    cudu_std_rtt.append(float(row['mdev rtt(ms)']))
                elif row['Version']=="gnb" and row['UEs']=="1":
                    gnb_avg_rtt.append(float(row['avg rtt(ms)']))
                    gnb_min_rtt.append(float(row['min rtt(ms)']))
                    gnb_max_rtt.append(float(row['max rtt(ms)']))
                    gnb_std_rtt.append(float(row['mdev rtt(ms)']))
    ratelist=np.array(ratelist)
    #linegraph_latency(ratelist,cudu_avg_rtt,gnb_avg_rtt,cudu_min_rtt,gnb_min_rtt,cudu_max_rtt,gnb_max_rtt)
    #smoothline_latency(ratelist,cudu_avg_rtt,gnb_avg_rtt,cudu_min_rtt,gnb_min_rtt,cudu_max_rtt,gnb_max_rtt)
    
    #std_latency2_extralatency(ratelist,cudu_avg_rtt,gnb_avg_rtt,cudu_std_rtt,gnb_std_rtt)
    std_latency2(ratelist,cudu_avg_rtt,gnb_avg_rtt,cudu_std_rtt,gnb_std_rtt)

#For Experiment 4
#def graph_4DLvs4UL(labelslist,highlist,lowlist,otherlist,ldpclist,dftlist,totalcpus,\
 #       highlist_cpu,lowlist_cpu,otherlis#t_cpu,ldpclist_cpu,dftlist_cpu):


#For Experiment 4
def func4DLvs4UL(filename):
    datas=pd.readcsv('filename',usecols=['Rate(Mbps)','HIGH PHY','LOW PHY','OTHERS','LDPC','DFT','TotalCPU'])
    print(datas)
            
"""def func4DLvs4UL(filename):
    labelslist=[]
    highlist=[]
    lowlist=[]
    otherlist=[]
    ldpclist=[]
    dftlist=[]
    totalcpus=[]
    highlist_cpu=[]
    lowlist_cpu=[]
    otherlist_cpu=[]
    ldpclist_cpu=[]
    dftlist_cpu=[]
    totalcpus_cpu=[]
    with open(filename) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            labelslist.append(row['Rate'])
            highlist.append(row['HIGH PHY'])
            lowlist.append(row['LOW PHY'])
            otherlist.append(row['OTHERS'])
            ldpclist.append(row['LDPC'])
            dftlist.append(row['DFT'])
            totalcpus.append(row['TotalCPU'])
            highlist_cpu.append(row['HIGH PHY_CPU'])
            lowlist_cpu.append(row['LOW PHY_CPU'])
            otherlist_cpu.append(row['OTHERS_CPU'])
            ldpclist_cpu.append(row['LDPC_CPU'])
            dftlist_cpu.append(row['DFT_CPU'])
    graph_4DLvs4UL(labelslist,highlist,lowlist,otherlist,ldpclist,dftlist,totalcpus,\
        highlist_cpu,lowlist_cpu,otherlist_cpu,ldpclist_cpu,dftlist_cpu)
"""

#Experiment 5 Failed
"""
def CPUUsage_Stackedbar(data):
    print(data)
    width=0.5
    X=np.arange(start=1,stop=(len(data['ID'])+1), step=1)
    fig,ax=plt.subplots()
    print(X)
    print(data['LOW PHY_CPU'])
    lowdata=np.array(data['LOW PHY_CPU'])
    highdata=np.array(data['HIGH PHY_CPU'])
    otherdata=np.array(data['OTHERS_CPU'])
    print(lowdata)
    lowbar=ax.bar(X,np.array(data['LOW PHY_CPU']),width,label="LOW PHY")
    #highbar=ax.bar(X,np.array(data['HIGH PHY_CPU']),width,bottom=lowbar,label="HIGH PHY")
    #otherbar=ax.bar(X,np.array(data['OTHERS_CPU']),width,bottom=highbar+lowbar,label="OTHERS")
    ax.set_xticks(np.array(data['Rate']))
    ax.set_xlabel("Sending Rate(mbps)")
    ax.set_ylabel("CPU Usage(%)")
    ax.set_title("CPU Usage Over Sending Rate(%)")
    ax.legend()
    plt.ylim(0,110)
    plt.show()
"""
#Experiment 5
def CPUUsage_Stackedbar(data):
    #xticks=data['Rate']
    xticks=['4UL','Idle','4DL','10DL','20DL','30DL','40DL','90DL']
    X=np.arange(start=1,stop=len(data['Rate'])+1,step=1)
    print(X)
    print(data['Rate'])
    #X=np.array(X)
    highphy=data['HIGH PHY_CPU']
    lowphy=data['LOW PHY_CPU']
    others=data['OTHERS_CPU']

    fig,ax = plt.subplots()
    ax.bar(X,lowphy,label="LOW PHY",color='red',edgecolor='k',hatch='////')
    ax.bar(X,highphy,bottom=lowphy,label='HIGH PHY',color='limegreen',edgecolor='k',hatch='....')
    ax.bar(X,others,bottom=lowphy+highphy,label="L2+L3",color='mediumslateblue',edgecolor='k',hatch='\\\\\\')
    ax.set_xticks(X)
    ax.set_xticklabels(xticks)
    ax.set_xlabel("Sending Rate(Mbps)",fontweight='bold')
    ax.set_ylabel("CPU Usage(%)",fontweight='bold')
    #ax.set_title("CPU Usage of Function Layers")
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    #ax.legend(facecolor='transparent',loc='upper center',fontsize=22)
    ax.legend(loc='upper center', fancybox=False, framealpha=0.8,fontsize=20)
    plt.savefig(graphsdir+"/highlowother_stacked.pdf",transparent=True)
    plt.show()
    print("save to:",graphsdir)

#Experiment 5
def read_CPUUsage_real(filename):
    
    data1=pd.read_csv(filename)    
    CPUUsage_Stackedbar(data1)

#for Experiment6
def graph_mcs_throughput(data1):
    plt.rcParams['figure.figsize'] = (12,12)
    plt.rc('font', size=38)
    fig,ax = plt.subplots()
    fig.subplots_adjust(bottom=0.15)
    fig.subplots_adjust(left=0.15)
    print(data1)
    ax.plot(data1['Index'],data1['Throughput(Mbps)'],linestyle='solid',color='darkcyan',marker='^',linewidth=3,markersize=14)

    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.set_xlabel("MCS Index",fontweight='bold')
    ax.set_ylabel("Throughput(Mbps)",fontweight='bold')
    ax.set_ylim(0,100)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    #plt.legend(framealpha=0.8,fontsize=22)
    plt.legend(frameon=False,fontsize=32)
    plt.savefig(graphsdir+"/MCS_throughput.pdf", transparent=True)
    plt.show()

def graph_mcs_cpu(data1):
    plt.rcParams['figure.figsize'] = (12,12)
    plt.rc('font', size=38)
    fig,ax = plt.subplots()
    fig.subplots_adjust(bottom=0.15)
    fig.subplots_adjust(left=0.15)
    print(data1)
    ax.plot(data1['Index'],data1['TotalCPU'],linestyle='solid',marker='o',linewidth=3,markersize=14)

    
    ax.set_xlabel("MCS Index",fontweight='bold')
    ax.set_ylabel("CPU Usage(%)",fontweight='bold')
    ax.set_ylim(0,110)
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    #plt.legend(framealpha=0.8,fontsize=22)
    plt.legend(frameon=False,fontsize=32)
    plt.savefig(graphsdir+"/MCS_cpu.pdf", transparent=True)
    plt.show()

def graph_mcs_cpu_throughput(data1):
    plt.rcParams['figure.figsize'] = (12,8)
    plt.rc('font', size=25)
    fig,ax=plt.subplots()
    ax.plot(data1['Index'],data1['Throughput(Mbps)'],linestyle='solid',label='Throughput',marker='o',linewidth=3,markersize=14)
    ax.set_xlabel("MCS Index",fontweight='bold')
    ax.set_ylabel("Throughput(Mbps)",fontweight='bold',color='red')
    ax.set_ylim(0,110)
    

    ax2=ax.twinx()
    ax2.plot(data1['Index'],data1['TotalCPU'],linestyle='solid',label='CPU Usage',color='darkcyan',marker='^',linewidth=3,markersize=14)
    ax2.set_ylim(0,110)
    ax2.set_ylabel("CPU Usage(%)",fontweight='bold',color='darkcyan')
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax2.yaxis.label.set_color('black')
    ax.tick_params(colors='black')
    ax2.tick_params(colors='black')
    #plt.legend(framealpha=0.8,fontsize=22)
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    ax2.spines['bottom'].set_color('black')
    ax2.spines['top'].set_color('black')
    ax2.spines['left'].set_color('black')
    ax2.spines['right'].set_color('black')
    ax.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax2.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.legend(loc='lower left',framealpha=0.8,fontsize=25)
    ax2.legend(loc='lower right',framealpha=0.8,fontsize=25)
    #plt.legend(framealpha=0.8,fontsize=25)
    plt.savefig(graphsdir+"/MCS_cpu_throughput.pdf", transparent=True)
    plt.show()
#for Experiment6
def read_mcs_cpu_throughput(filename):
    
    data1=pd.read_csv(filename)
    graph_mcs_cpu_throughput(data1)
    #graph_mcs_throughput(data1)
    #graph_mcs_cpu(data1)


#############main##############
#For Experiment 1
#file1="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/rate_usage_stackedbar.csv"
#readCpuUsage2(file1)

#For Experiment 2
#file2="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/gnbvscudu_trend.csv"
#readgnbvscudu_trend(file2)

#For Experiment 3
file3="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/extralatency_cudugnb.csv"
readlatencycsv(file3)

#For Experiment 4 failed, See trypd.py
#file4="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/4DLvs4UL.csv"
#func4DLvs4UL(file4)

#For Experiment 5
#file5="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/real_cpu_rate_stackedbar.csv"
#os.system("sed -i '' 's/%//g' /Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/real_cpu_rate_stackedbar.csv")
#read_CPUUsage_real(file5)

#For Experiment 6
#file6="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/MCS_CPUThroughput.csv"
#os.system("sed -i '' 's/%//g' /Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/MCS_CPUThroughput.csv")
#read_mcs_cpu_throughput(file6)