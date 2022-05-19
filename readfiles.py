#!/usr/bin/python3
#This file is a test for the code and has been copied to classify.py
import os
filePath = '/Users/cuidi/iCloud/Research/5G/csvAnalysis/filecodtest'

def makefolder(foldername):
    folder = os.path.exists(foldername)
    if not folder:
        #print("Create folder")
        os.makedirs(resdir)
    #else:
    #    print("folder exists")
        
for i,j,k in os.walk(filePath):
    
    for ki in range(len(k)):
        if k[ki].endswith(('txt')) and k[ki].endswith(('left.txt'))==False:
            resdir=i+"/perf_classify_res"
            makefolder(resdir)
        #if 'test.png'.endswith(('jpg','png','jpeg','bmp')):
            print(k[ki])
            file=i+"/"+k[ki]
            
            #print(file)
    #print(i,j,k)
    #file=str(i)+"/"+str(k)
    #print(i+"/"+k)
    