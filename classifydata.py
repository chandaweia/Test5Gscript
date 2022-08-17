#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

def symbolclassify(str,lastlinestr):
    for i in range(1, len(symbollist)):
        #print("symbollist str_list[0]",str_list[0])
        #if symbollist[i][2].find(str_list[4]) != -1: #-1 not found, 0 found
        if str.find(symbollist[i][2]) != -1:
            res=lastlinestr+","+symbollist[i][3]+","+symbollist[i][4]+","+symbollist[i][5]+"\n"
            #print("symbollist str_list[0]",str_list[0])
            str_list=lastlinestr.split()
            res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str.replace('\n', '').replace('\r', '')+","\
                +symbollist[i][3]+","+symbollist[i][4]+","+symbollist[i][5]+"\n"
            return res
    return ""

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
            #res=""
            if(str.find('dft')!=-1 and commandlist[i][5].strip()==""):
                #print("find dft:",str)
                res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str_list[4]+","\
                +commandlist[i][3]+","+commandlist[i][4]+",DFT"+"\n"
                return res
            else:
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
            #print("匹配：symbollist[i][2]",symbollist[i][2])
            return res
    for i in range(1, len(objectlist)):
        #print("objectlist str_list[0]",str_list[0])
        #if objectlist[i][1].find(str_list[2]) != -1: #-1 not found, 0 found
        if str_list[2].find(objectlist[i][1]) != -1:
            #print("objectlist str_list[0]",str_list[0])
            res = str_list[0]+","+str_list[1]+","+str_list[2]+","+str_list[3]+","+str_list[4]+","\
                +objectlist[i][3]+","+objectlist[i][4]+","+objectlist[i][5]+"\n"
            #print("匹配：objectlist[i][1]",objectlist[i][1])
            return res
        
    return ""

def doclassify(path,filename,resdir):
    filename_left=resdir+"/"+filename+"_left.txt"
    filename_classified=resdir+"/"+filename+"_classified.csv"
    readfilenm=path+"/"+filename
    print("Report is save to:",filename_classified)
    f = open(readfilenm)
    fw_left = open(filename_left,"w")
    fw_classified = open(filename_classified,"w")
    fw_classified.write("Overhead,Command,Object,Symbol,Layer,Layer2,Layer3\n")

    line = f.readline()
    lastline=""
    lastlines=[]
    while line:
        #print("line:",line)
        #print("Last line:",lastline)
        #print(line)
        linestr = line.lstrip(" ")
        if linestr.startswith('#'):
            #Write to another file
            fw_left.write(line)
        elif linestr.find("%") != -1 and linestr.startswith('#')==False and linestr.startswith('|')==False and linestr.startswith('-')==False:
            #do classify
            #print("Do classify:",linestr)
            if(lastline!=""):
                fw_left.write(lastline)
                fw_left.writelines(lastlines)
                lastline=""
                lastlines=[]
            res_layer = layerclassify(linestr)
            #print("分类结果：",res_layer)
            if res_layer == "":
                #print("第一行line识别不出来，写入lastline")
                lastline=line
            else:
                fw_classified.write(res_layer) 
            line = f.readline()
            continue
        elif lastline!="" and ( linestr.startswith('|') or linestr.startswith('-') or linestr.find("%") == -1):
            #print('该行是未识别信息的下一行，lastline:',lastline)
            res_layer=symbolclassify(linestr,lastline)
            lastlines.append(line)
            if res_layer != "":
                fw_classified.write(res_layer) 
                fw_left.writelines(lastlines)
                lastline=""   
                lastlines=[]
            line = f.readline()
            continue
        else:
            #print("classify++",linestr)
            #print(line)
            fw_left.write(line)
            #Write to another file
        line = f.readline()
    
    f.close()
    fw_left.close()
    fw_classified.close()

def makefolder(foldername):
    folder = os.path.exists(foldername)
    if not folder:
        #print("Create folder")
        os.makedirs(foldername)
    #else:
    #    print("folder exists")

def doclassify_dir(filePath):
    for i,j,k in os.walk(filePath):
        for ki in range(len(k)):
            if k[ki].endswith(('txt')) and k[ki].endswith(('left.txt'))==False:
                resdir=i+"/perf_classify_res"
                makefolder(resdir)
                #print(k[ki])
                file=i+"/"+k[ki]
                print("")
                print("classfy file:",file)
                doclassify(i,k[ki],resdir)
                #print("Path:",i,"file:",k[ki],"resdir:",resdir)

#----------------main function-----------
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


#if it is a dir, then create a directory called perf_classify_res
#if it is a file, save report to the current 
for i in range(len(sys.argv)-1):
    if os.path.isdir(sys.argv[i+1]):
        doclassify_dir(sys.argv[i+1])
    elif os.path.isfile(sys.argv[i+1]):
        doclassify(".",str(sys.argv[i+1]),".")
        

#doclassify("perf_99hz_v3.data_nochildren.txt")
"""print("Command:++++++++",len(commandlist))
print(commandlist)
print("Object:++++++++++",len(objectlist))
print(objectlist)
print("Symbol+++++++++++++",len(symbollist))
print(symbollist)
"""
