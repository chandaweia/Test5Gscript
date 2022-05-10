#!/usr/bin/python
from collections import namedtuple
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

def countoverhead(filename):
	print(layers)
	with open(filename) as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
			print("row:",row)
			for i in range(len(layers)):
				if row['Layer'] == layers[i]:
					overhead = row['Overhead'].rstrip('%')
					sums[i] += float(overhead)
					sums[7] += float(overhead)
					print("overhead{0},sums[{1}]:{2},layers[{1}]:{3}".format(overhead,i,sums[i],layers[i]))
					break
		
			"""if row['Layer2'] != "":
				for j in range(len(layers2)):
					if row['Layer2'] == layers2[j]:
						sums2[j] += float(overhead)
				if row['Layer3'] != "":
					for k in range(len(layers3)):
						if row['Layer3'] == layers3[k]:
							sums3[k] += float(overhead)"""
		print("sums:",sums)

def bargraph(X,Y):
	print("bar graph")
	Xticks=np.arange(len(X))
	plt.bar(X, Y, 0.8, color="blue")  
	#plt.bar(XX,YY,1,color="yellow")  #使用不同颜色  
	plt.xlabel("X-axis")  #设置X轴Y轴名称  
	plt.ylabel("Y-axis")  
	plt.title("bar chart")
	#使用text显示数值  
	for a,b in zip(Xticks,Y):
		plt.text(x=a-0.25 , y=b+0.05 , s=f"{b}" , fontdict=dict(fontsize=10))
		#plt.text(x=a , y = b , s=f"{b}" , fontdict=dict(fontsize=10))
	
	plt.ylim(0,45.00)    #设置Y轴上下限  
	plt.show()


#if __name__=="__main__":
print('len(sys.argv):',len(sys.argv))
print(str(sys.argv[1]))
layers=['RRC','SDAP','PDCP','RLC','MAC','PHY','NG']
sums=[0]*8
layers2=['HIGH PHY','LOW PHY']
sums2=[0]*2
layers3=['LDPC']
sums3=[0]

countoverhead(str(sys.argv[1]))
print("'RRC','SDAP','PDCP','RLC','MAC','PHY','NG','Sum':",sums)
print("HIGH PHY, LOW PHY:",sums2)
print("LDPC:",sums3)

sums=[round(i,2) for i in sums]
#bargraph(sums,layers)


