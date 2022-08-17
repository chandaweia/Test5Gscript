#!/usr/bin/python3
from collections import namedtuple
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
import string
#plt.rcdefaults()
graphsdir="/Users/cuidi/iCloud/Research/5G/Sigcomm_Test/UsefulData/Graphs"
plt.rcParams['figure.figsize'] = (9,6)
plt.rc('font', size=20)
def countoverhead(filename):
	#print(layers)
	sums=[0]*LEN_sum
	sums2=[0]*2
	sums3=[0]*2
	layersum=0
	with open(filename) as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
			for i in range(len(layers)):
				overhead = row['Overhead'].rstrip('%')
				if row['Layer'] == layers[i]:
					#overhead = row['Overhead'].rstrip('%')
					sums[i] += float(overhead)
					layersum += float(overhead)
					#print("overhead{0},sums[{1}]:{2},layers[{1}]:{3}".format(overhead,i,sums[i],layers[i]))
					break
			for j in range(len(layers2)):
				if row['Layer2']!="" and row['Layer2'] == layers2[j]:
					sums2[j] += float(overhead)
					#print("overhead{0},sums2[{1}]:{2},layers[{1}]:{3}".format(overhead,j,sums2[j],layers2[j]))
					break
			for k in range(len(layers3)):
				if row['Layer3'] != "" and row['Layer3'] == layers3[k]:
					sums3[k] += float(overhead)
					break
		sum_r=sum(sums)
		sums[7]=100-sum_r
		return layersum,sums,sums2,sums3

def bargraph_cpuusage(X,Y,savefig):
	#print("X:",X)
	#print("Y:",Y)
	plt.rc('font', size=18)
	Xticks=np.arange(len(X))
	plt.bar(X, Y, 0.8, color="blue")  
	#plt.bar(XX,YY,1,color="yellow")
	plt.xlabel("Layers",fontweight='bold')  
	plt.ylabel("CPU Usage (%)",fontweight='bold')  
	#plt.title("CPU Usage")
	#use text to show the value
	for a,b in zip(Xticks,Y):
		plt.text(x=a-0.4 , y=b+0.05, s=f"{b}%", fontdict=dict(fontsize=16))
		#plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
	
	plt.ylim(0,100)    #set y-axis range
	plt.savefig(savefig)
	plt.show()

def bargraph(X,Y,savefig):
	print(X)
	print(Y)
	Xticks=np.arange(len(X))
	plt.bar(X, Y, 0.8, color="blue")  
	#plt.bar(XX,YY,1,color="yellow")
	plt.xlabel("Layers")  
	plt.ylabel("Function Usage Percentage(%)")  
	plt.title("Perf Sample Functions Usage Percentage(%)")
	print("will save to:",savefig)
	#use text to show the value
	for a,b in zip(Xticks,Y):
		plt.text(x=a-0.25 , y=b+0.05 , s=f"{b}%" , fontdict=dict(fontsize=10))
		#plt.text(x=a-0.25 , y=b+0.05, fontdict=dict(fontsize=10))
		#plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
	
	plt.ylim(0,100)    #set y-axis range
	plt.show()

def draw1file(filename,totalcpu):
	savetopic=filename.rstrip(".csv")

	layersum,sums,sums2,sums3=countoverhead(filename)
	layersum=round(layersum,2)
	#layersum,sums,sums2,sums3=round(countoverhead(filename),2)
	"""print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG','Sum':",sums)
	print("HIGH PHY, LOW PHY:",sums2)
	print("LDPC:",sums3)"""
	#print("sums in drawgraph:",sums)
	sums=[(round(i,2)) for i in sums]
	sums2=[(round(i,2)) for i in sums2]
	sums3=[(round(i,2)) for i in sums3]
	print("layersum:",layersum)
	#print("Layers:",layers)
	print("+++Perf Sample:",layers,":",sums)
	print("+++Perf Sample:",layers2,sums2,end=',')
	print("L2+L3+SYS:",100-sum(sums2))
	print("+++Perf Sample:",layers3,sums3)
	
	bargraph(layers,sums,"")
	#savefig=savetopic+"/4MbpsUL_highlow.jpg"
	
	bargraph(layers2,sums2,"")

	if(totalcpu==0):
		return
	#print("+++++++totalcpu:",totalcpu)
	sums=[(round(i*totalcpu,2)) for i in sums]
	sums2=[(round(i*totalcpu,2)) for i in sums2]
	sums3=[(round(i*totalcpu,2)) for i in sums3]
	print("+++CPU Usage:",layers,":",sums)
	print("+++CPU Usage:",layers2,sums2,end=',')
	print("L2+L3+SYS:",totalcpu*100-sum(sums2))
	print("+++CPU Usage:",layers3,sums3)
	savefig=graphsdir+"/90MbpsDL_overall_dis.pdf"
	bargraph_cpuusage(layers,sums,savefig)
	print("+++++save to:",savefig)
	savefig=graphsdir+"/90MbpsDL_highlow_dis.pdf"
	bargraph_cpuusage(layers2,sums2,savefig)
def draw1file_perfsample(filename):
	savetopic=filename.rstrip(".csv")
	layersum,sums,sums2,sums3=countoverhead(filename)
	
	"""print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG','Sum':",sums)
	print("HIGH PHY, LOW PHY:",sums2)
	print("LDPC:",sums3)"""
	#print("sums in drawgraph:",sums)
	sums=[(round(i,2)) for i in sums]
	sums2=[(round(i,2)) for i in sums2]
	sums3=[(round(i,2)) for i in sums3]
	layersum=round(layersum,2)
	print("layersum without OTHERS:",layersum)
	#print("Layers:",layers)
	print("+++",layers,":",sums)
	print("+++",layers2,sums2)
	print("+++",layers3,sums3)
	savefig=savetopic+".jpg"
	bargraph(layers,sums,savefig)
	savefig=savetopic+"_PHY.jpg"
	bargraph(layers2,sums2,savefig)

def drawdir(dirPath):
	for i,j,k in os.walk(dirPath):
		for ki in range(len(k)):
			if k[ki].endswith(('_classified.csv')):
				filenm=i+"/"+k[ki].lstrip()
				print("")
				print("+++file name:",filenm)
				draw1file(filenm,0)
				

#if __name__=="__main__":
#layers=['RRC','SDAP','PDCP','RLC','MAC','PHY','NG','OTHERS']
layers=['PHY','MAC','RLC','PDCP','RRC','SDAP','NG','OTHERS']
LEN_sum=8
sums=[0]*LEN_sum
layers2=['HIGH PHY','LOW PHY']

sums2=[0]*2
#sums2list=[]
layers3=['LDPC','DFT']
sums3=[0]*2
print('len(sys.argv):',len(sys.argv))
print(str(sys.argv[1]))
for i in range(len(sys.argv)-2):
	if os.path.isdir(sys.argv[i+1]):
		print("Is DIr")
		drawdir(sys.argv[i+1])
	elif os.path.isfile(sys.argv[i+1]):
		print("Is file")
		draw1file(sys.argv[i+1],float(sys.argv[2])/100)
        #doclassify(".",str(sys.argv[i+1]),".")

#python countcpu.py ../perfdata_v2/perfreport 1