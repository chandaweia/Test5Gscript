from cProfile import label
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
import random 
import graph_helper
import csv

matplotlib.style.use('ggplot')
#plt.rcParams['figure.figsize'] = (9,6)
plt.rcParams['figure.figsize'] = (12,8)
plt.rc('font', size=25)
import matplotlib.ticker as mtick
graphsdir="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/Graphs"

def graph4DLvs4UL(data):
    print(data)
    width=15
    X=np.arange(start=100,stop=(len(data['ID'])+1)*100, step=100)
    x_max=(len(data['ID'])+1)*100
    print("X:",X)
    print("HIGH PHY\n",data["HIGH PHY"])
    fig,ax=plt.subplots()
    highphy=ax.bar(X-2*width,data['HIGH PHY'],width,color='blue')
    lowphy=ax.bar(X-1*width,data['LOW PHY'],width,color='red')
    otherphys=ax.bar(X,data['OTHERS'],width,color='mediumslateblue')
    ldpc=ax.bar(X+1*width,data['LDPC'],width,color='deeppink')
    dft=ax.bar(X+2*width,data['DFT'],width,color='teal')
    """high_cpu=ax.bar(X*width,data['HIGH PHY_CPU'],width,color='saddlebrown')
    low_cpu=ax.bar(X+1*width,data['LOW PHY_CPU'],width,color='olive')
    ldpc_cpu=ax.bar(X+2*width,data['OTHERS_CPU'],width,color='cyan')
    dft_cpu=ax.bar(X+3*width,data['LDPC_CPU'],width,color='darkorchid')
    other_cpu=ax.bar(X+4*width,data['DFT_CPU'],width,color='orange')"""

    ax.set_xticks(X)
    ax.set_xticklabels(data['Rate(Mbps)'])
    ax.set_xlabel('Traffic Rate(Mbps)')
    ax.set_ylabel("Sample Function Percentage(%)")
    ax.set_title("Function Percentage: 4Mbps UL vs Idle vs 4Mbps DL")
    ax.set_xlim(0,x_max)
    ax.set_ylim(0,80)
    plt.legend([highphy,lowphy,otherphys,ldpc,dft],['High PHY','LOW PHY','OTHERS','LDPC','DFT'],loc='upper left',fontsize=18,frameon=False)
    #ax.yaxis.set_major_formatter(mtick.PercentFormatter()) #It could work
    #yvals=np.arange(start=0,stop=1.2,step=0.2)
    #ax.set_yticklabels(['{:,.2%}'.format(x) for x in yvals])
    
    plt.show()

def graph4DLvs4UL_CPU(data):
    print(data)
    width=15
    X=np.arange(start=100,stop=(len(data['ID'])+1)*100, step=100)
    x_max=(len(data['ID'])+1)*100
    print("Kan------->X:",X)
    fig,ax=plt.subplots()
    print(X-2*width)
    highphy=ax.bar(X-2*width,data['HIGH PHY_CPU'],width,color='limegreen',edgecolor='k',hatch='....') #peru
    lowphy=ax.bar(X-1*width,data['LOW PHY_CPU'],width,color='red',edgecolor='k',hatch='///') #limegreen
    otherphys=ax.bar(X,data['OTHERS_CPU'],width,color='mediumslateblue',edgecolor='k',hatch='\\\\\\\\') #gold
    ldpc=ax.bar(X+1*width,data['LDPC_CPU'],width,color='peru',edgecolor='k',hatch='++++')#deepink
    dft=ax.bar(X+2*width,data['DFT_CPU'],width,color='gold',edgecolor='k',hatch='xxxx')#teal

    ax.set_xticks(X)
    #ax.set_xticklabels(X)
    ax.set_xticklabels(data['Rate(Mbps)'])
    ax.set_xlabel('Sending Rate(Mbps)',fontweight='bold')
    ax.set_ylabel("CPU Usage(%)",fontweight='bold')
    #ax.set_title("CPU Usage: 4Mbps UL vs Idle vs 4Mbps DL")
    ax.set_xlim(0,x_max)
    ax.set_ylim(0,80)

    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['right'].set_color('black')
    plt.grid(True,color='black',linestyle='-.', linewidth = 0.5)
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.tick_params(colors='black')

    ax.legend([highphy,lowphy,otherphys,ldpc,dft],\
        ['High PHY','LOW PHY','L2+L3','LDPC','DFT'],loc='upper left',framealpha=0.8,fontsize=22)
    #plot.legend([highphy,lowphy,otherphys,ldpc,dft],\
    #    ['High PHY','LOW PHY','OTHERS','LDPC','DFT'],loc='upper left',framealpha=0.8,fontsize=22,frameon=False)
    #ax.legend(loc='upper center', fancybox=False, framealpha=0.8,fontsize=20)
    plt.savefig(graphsdir+"/4UL4DL90DL.pdf",transparent=True)
    plt.show()



#Not success
def args_graph(labels,lists):
    Xlabelname="X label"    #X label Name
    Ylabelname="Y label"    #Y label Name
    Titlename="Tile"        #Title Name
    width=10
    len_lists=len(lists)    
    widthofgroup=len(labels)*width*3  
    X=np.arange(start=widthofgroup,stop=(len_lists+2)*widthofgroup, step=widthofgroup)    
    fig,ax=plt.subplots()

    bars=[]
    bias=len_lists%2
    shift=len_lists/2
    print("labels:",labels)
    print("X:",X)
    print("list[0]:",lists[0])
    for i in range(len_lists):
        print("i:",i)
        print("X:",X+(i-shift)*width-bias)
        onebar=ax.bar(X+widthofgroup+(i-shift)*width-bias, lists[i],width,color=graph_helper.randomcolor())
        #onebar=ax.bar(X, lists[i],width,color=graph_helper.randomcolor())
        bars.append(onebar)

    ax.set_xticks(X)
    ax.set_xticklabels(labels)
    ax.set_xlabel(Xlabelname)
    ax.set_ylabel(Ylabelname)
    ax.set_title(Titlename)
    #ax.set_xlim(0,x_max)
    ax.set_ylim(0,80)
    plt.legend(bars,loc='upper right',frameon=False)
    plt.show()

#Not success
def args_is_diff_group(file1,*args):
    #For Example, args: TotalCPU, HIGH PHY for x axis.
    #args: All for x axis.
    #INPUT: 0Mbps: TotalCPU,HIGH PHY; 1Mbps: Total
    #OUTPUT Graph: All totalCPU values are in a group and all HIGH PHY value are in another group.
    lens=len(args)
    lists=[]
    #labels=args
    x_ticks=args
    #print("labels:",labels[0])

    for i in range(lens):
        onelist=[]
        with open(file1) as f:
            f_csv = csv.DictReader(f)
            for row in f_csv:
                onelist.append(row[x_ticks[i]])
        onelist=np.array(onelist)
        lists.append(onelist)
        print(lists)
    
    
    """with open(file1) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
    """
def read4DLvs4UL(file4):
    data1=pd.read_csv(file4)    
    graph4DLvs4UL(data1)
    graph4DLvs4UL_CPU(data1)

##################Main################
file4="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/4DLvs4UL.csv"
#os.system("sed -i '' 's/%//g' /Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/4DLvs4UL.csv")##Mac OS Version
#os.system("sed -i '' 's/%//g' 4DLvs4UL_test.csv") ##Linux Version
read4DLvs4UL(file4)
#args_is_diff_group(file4,'TotalCPU','LDPC_CPU')
#df = pd.read_csv(file4,encoding= 'utf-8',header=None)

