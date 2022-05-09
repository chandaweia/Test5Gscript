#!/usr/bin/python

import re
import os
from csv import reader

def readlayersmap(mapfile):
    with open(mapfile, 'r') as csv_file:
        csv_reader=reader(csv_file)
        list_of_rows =  list(csv_reader)
    csv_file.close()

    
    commandlist.append(list_of_rows[0])
    objectlist.append(list_of_rows[0])
    symbollist.append(list_of_rows[0])
    for i in range(1, len(list_of_rows)):
        if(list_of_rows[i][0]!=""):
            #Command list
            commandlist.append(list_of_rows[i])
        elif(list_of_rows[i][1]!=""):
            objectlist.append(list_of_rows[i])
        elif(list_of_rows[i][2]!=""):
            symbollist.append(list_of_rows[i])
    #return list_of_rows

def doclassify(filename):
    filename_left=filename+"_remaining"
    filename_classified=filename+"_classified"

    f = open(filename)
    fw_left = open(filename_left,"w")
    fw_classified = open(filename_classified,"w")

    line = f.readline()
    while line:
        #print(line)
        if line.startswith('#') or line.startswith('|') or line.startswith('-'):
            print("Start with++",line)
            #Write to another file
            #print(line)
            fw_left.write(line)
        elif line.find("%") != -1:
            #do classify
            print("Contain++",line)
            fw_classified.write(line)
        else:
            print("classify++",line)
            #print(line)
            fw_left.write(line)
            #Write to another file
        line = f.readline()
    
    f.close()
    fw_left.close()
    fw_classified.close()


def dellines(filename, str):
    list = []
    matchPattern = re.compile(r'INVALID PARAMETER')
    f = open(filename)
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
        
    #elif matchPattern.search(line):
    #pass
    #else:
    #list.append(line)
    #file.close()
    #file = open(r'C:\target.txt', 'w')
    #for i in list:
    #file.write(i)
    #file.close()

#main function
commandlist=[]
symbollist=[]
objectlist=[]
#General layers including six layers and NG
layerlist=[]
#Detailed classification including LOW PHY, HIGH PHY
layer2list=[]
#Detailed classification including LDCP in PHY layer
readlayersmap('LayersMap.csv')

doclassify("functionlaysdata.txt_classified")
"""print("Command:++++++++",len(commandlist))
print(commandlist)
print("Object:++++++++++",len(objectlist))
print(objectlist)
print("Symbol+++++++++++++",len(symbollist))
print(symbollist)
"""
