"""'RRC','SDAP','PDCP','RLC','MAC','PHY','NG','Sum': 
[1.5300000000000002, 0, 1.0, 5.7899999999999885, 0.03, 43.640000000000114, 30.24000000000002, 
82.2299999999997]
HIGH PHY, LOW PHY: [11.6, 31.680000000000028]
LDPC: [4.56]"""
#https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def bargraph_layer():
    width = 0.5
    fig,ax = plt.subplots()

    y = [1.5300000000000002, 0, 1.0, 5.7899999999999885, 0.03, 43.640000000000114, 30.24000000000002]
    y2 = [11.6, 31.680000000000028]
    y3 = [4.56]
    x = ['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
    xarr=[1,2,3,4,5,6,7]
    x2 = ['HIGH PHY','LOW PHY']
    x3 = ['LDPC']

    #plt.plot(xarr,y)
    #plt.xlabel(x)
    #plt.ylabel(y)

    plt.title('Layers Ratio')

    weight = ax.bar(x,y,width,color='green')

    ax.set_xticks(xarr)
    ax.set_xticklabels(x)#将横坐标替换成
    ax.set_xlabel('Skewness Level')
    ax.set_ylabel('Ratio(%)')
    ax.set_title('Improvement of Max/Min')
    
    plt.legend([weight],["Weight"])

bargraph_layer()