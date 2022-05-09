#!/usr/bin/python
from collections import namedtuple
import sys
import csv

def countoverhead(filename, layers, protos):
	print(protos[0])
	sums=[0]*7
	sums_protos=0
	with open(filename) as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
			for i in range(6):
				if row['Layer'] == layers[i]:
					sums[i]+=float(row['Overhead'])
					sums[6]+=float(row['Overhead'])
					#print(row['Overhead'])
					break
			if row['Protocol'] == protos[0]:
				sums_protos += float(row['Overhead'])
				

	return sums,sums_protos
				#lines.append(row)

#if __name__=="__main__":
print('len(sys.argv):',len(sys.argv))
print(str(sys.argv[1]))
#sum_phy=countoverhead(str(sys.argv[1]), 'PHY')
layers=['RRC','SDAP','PDCP','RLC','MAC','PHY']
protos=['LDCP']

sums,sums_protos=countoverhead(str(sys.argv[1]), layers, protos)
print("'RRC','SDAP','PDCP','RLC','MAC','PHY','Sum':",sums)
print("LDCP:",sums_protos)


