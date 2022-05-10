#!/usr/bin/python

import re
import os
import sys
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

"""def searchlist(layerlist, word):
    print("searchlist:word:",word)
    for i in range(1, len(layerlist)):
        if layerlist[0].find(word) == 0: #-1 not found, 0 found
            return layerlist[i]
    return -1
"""

def layerclassify(str):
    #print("\nlayerclassify:+++++",str,end='')
    str_list=str.split()
    #str_list:  24.09%  thread_FH      librfsimulator.so   [.] rfsimulator_read
    if len(str_list) < 5:
        return ""
    for i in range(1, len(commandlist)):
        #print("commandlist[i][0]:{0},str_list[1]:{1},len(str_list):{2}".format(commandlist[i][0],str_list[1],len(str_list)))
        #if commandlist[i][0].find(str_list[1]) != -1: #-1 not found, 0 found
        if str_list[1].find(commandlist[i][0]) != -1:
            #print("commandlist[i][0]:{0},str_list[1]:{1},len(str_list):{2}".format(commandlist[i][0],str_list[1],len(str_list)))
            #print("commandlist str_list[0]",str_list[0])
            res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str_list[4]+","\
                +commandlist[i][3]+","+commandlist[i][4]+","+commandlist[i][5]+"\n"
            return res
    for i in range(1, len(symbollist)):
        #print("symbollist str_list[0]",str_list[0])
        #if symbollist[i][2].find(str_list[4]) != -1: #-1 not found, 0 found
        if str_list[4].find(symbollist[i][2]) != -1:
            #print("symbollist str_list[0]",str_list[0])
            res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str_list[4]+","\
                +symbollist[i][3]+","+symbollist[i][4]+","+symbollist[i][5]+"\n"
            return res
    for i in range(1, len(objectlist)):
        #print("objectlist str_list[0]",str_list[0])
        #if objectlist[i][1].find(str_list[2]) != -1: #-1 not found, 0 found
        if str_list[2].find(symbollist[i][1]) != -1:
            #print("objectlist str_list[0]",str_list[0])
            res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str_list[3]+","+str_list[4]+","\
                +objectlist[i][3]+","+objectlist[i][4]+","+objectlist[i][5]+"\n"
            return res
        
    return ""

def doclassify(filename):
    filename_left=filename+"_left.txt"
    filename_classified=filename+"_classified.csv"

    f = open(filename)
    fw_left = open(filename_left,"w")
    fw_classified = open(filename_classified,"w")
    fw_classified.write("Overhead,Command,Object,Symbol,Layer,Layer2,Layer3\n")

    line = f.readline()
    while line:
        #print(line)
        linestr = line.lstrip(" ")
        if linestr.startswith('#') or linestr.startswith('|') or linestr.startswith('-'):
            #print("Start with++",linestr)
            #Write to another file
            #print(linestr)
            fw_left.write(line)
        elif linestr.find("%") != -1:
            #do classify
            #print("Contain++",linestr)
            res_layer = layerclassify(linestr)
            #print(res_layer)
            if res_layer == "":
                fw_left.write(line)
            else:
                fw_classified.write(res_layer) 
            
        else:
            #print("classify++",linestr)
            #print(line)
            fw_left.write(line)
            #Write to another file
        line = f.readline()
    
    f.close()
    fw_left.close()
    fw_classified.close()

#main function
commandlist=[]
symbollist=[]
objectlist=[]
#General layers including six layers and NG
layerlist=[]
#Detailed classification including LOW PHY, HIGH PHY
layer2list=[]
#Detailed classification including LDCP in PHY layer
#print(str(sys.argv[1]))
readlayersmap('LayersMap.csv')

doclassify(str(sys.argv[1]))
#doclassify("perf_99hz_v3.data_nochildren.txt")
"""print("Command:++++++++",len(commandlist))
print(commandlist)
print("Object:++++++++++",len(objectlist))
print(objectlist)
print("Symbol+++++++++++++",len(symbollist))
print(symbollist)
"""
