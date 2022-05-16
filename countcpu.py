#!/usr/bin/python3
from collections import namedtuple
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def countoverhead(filename):
	#print(layers)
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
		#print("sums:",sums)
		return layersum

def bargraph(X,Y):
	print("bar graph")
	print("X:",X)
	print("Y:",Y)
	Xticks=np.arange(len(X))
	plt.bar(X, Y, 0.8, color="blue")  
	#plt.bar(XX,YY,1,color="yellow")
	plt.xlabel("Layers")  
	plt.ylabel("Function Usage Percentage(%)")  
	plt.title("Perf Sample Functions Usage Percentage(%)")
	#use text to show the value
	for a,b in zip(Xticks,Y):
		plt.text(x=a-0.25 , y=b+0.05 , s=f"{b}" , fontdict=dict(fontsize=10))
		#plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
	
	plt.ylim(0,100)    #set y-axis range
	plt.show()


#if __name__=="__main__":
print('len(sys.argv):',len(sys.argv))
print(str(sys.argv[1]))
layers=['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
sums=[0]*7
layers2=['HIGH PHY','LOW PHY']
sums2=[0]*2
layers3=['LDPC']
sums3=[0]

layersum=round(countoverhead(str(sys.argv[1])),2)
"""print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG','Sum':",sums)
print("HIGH PHY, LOW PHY:",sums2)
print("LDPC:",sums3)"""

sums=[round(i,2) for i in sums]
sums2=[round(i,2) for i in sums2]
sums3=[round(i,2) for i in sums3]
print("layersum:",layersum)
print("Layers:",layers)
print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG'",sums)
print("HIGH PHY, LOW PHY,PDCP:",sums2)
print("LDPC:",sums3)
bargraph(layers,sums)
bargraph(layers2,sums2)


