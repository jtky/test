# -*- coding: utf-8 -*-
import sys
import os
import re
import shutil

testpass="C:\\Users\\ky\\Desktop\\test\\datas"
filelist=[]


file = os.path.abspath("test.xlsx")
print(file)

filelist2=[]
num=0
for dpath,dnames,fnames in os.walk(testpass):
    #print(dpath,dnames,fnames)
    print(fnames)
    if(len(fnames)==0):
        #filelist2.append(dpath)
        print(dpath)
        pass
    else:
        #filelist2.append(dpath)
        print(dpath)
        print(testpass+"/t%06d" %(num))
        #shutil.copytree(dpath, testpass+"/t%06d" %(num))
        num+=1
