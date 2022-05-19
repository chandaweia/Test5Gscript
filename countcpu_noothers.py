#!/usr/bin/python3
from collections import namedtuple
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def countoverhead(filename):
	#print(layers)
	sums=[0]*7
	sums2=[0]*2
	sums3=[0]
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
		
		return layersum,sums,sums2,sums3

def bargraph(X,Y,savefig):
	Xticks=np.arange(len(X))
	plt.bar(X, Y, 0.8, color="blue")  
	#plt.bar(XX,YY,1,color="yellow")
	plt.xlabel("Layers")  
	plt.ylabel("Function Usage Percentage(%)")  
	plt.title("Perf Sample Functions Usage Percentage(%)")
	print("will save to:",savefig)
	#use text to show the value
	for a,b in zip(Xticks,Y):
		plt.text(x=a-0.25 , y=b+0.05 , s=f"{b}" , fontdict=dict(fontsize=10))
		#plt.text(x=a-0.25 , y=b+0.05, fontdict=dict(fontsize=10))
		#plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
	
	plt.ylim(0,100)    #set y-axis range
	#plt.savefig(savefig)
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
	sums=[(round(i,2)*totalcpu) for i in sums]
	sums2=[(round(i,2)*totalcpu) for i in sums2]
	
	sums3=[(round(i,2)*totalcpu) for i in sums3]
	print("layersum:",layersum)
	print("Layers:",layers)
	print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG'",sums)
	print("HIGH PHY, LOW PHY,PDCP:",sums2)
	print("LDPC:",sums3)
	savefig=savetopic+".jpg"
	bargraph(layers,sums,savefig)
	savefig=savetopic+"_PHY.jpg"
	bargraph(layers2,sums2,savefig)

def drawdir(dirPath):
	for i,j,k in os.walk(dirPath):
		for ki in range(len(k)):
			if k[ki].endswith(('_classified.csv')):
				filenm=i+"/"+k[ki].lstrip()
				print("file name:",filenm)
				draw1file(filenm,1)

#if __name__=="__main__":
layers=['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
sums=[0]*7
layers2=['HIGH PHY','LOW PHY']
sums2=[0]*2
sums2list=[]
layers3=['LDPC']
sums3=[0]
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