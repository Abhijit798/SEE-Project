from genericpath import isfile
import os
import pickle
import re
import argparse


#######to check the string in the file

def search(str1, list_file, i):
    list1 = []
    for each_file in list_file:
        fr = open(each_file,"r")
        if i:
            m = re.search(str1,fr.read(),re.I)
        else:
            m = re.search(str1,fr.read())
        if m:
            t1 = (m.group(),each_file)
            list1.append(t1)
    return list1


def OnlyFile(str1, dir, R =False, I = False):
    
    if R:
        main_list = []
        resp = os.walk(dir)
        for root,dirs,files in resp:
            if files:
                list_files = []
                for file in files:
                    file_with_path = root+"\\"+file
                    list_files.append(file_with_path) 
            list1 = search(str1, list_files, i = I)
            main_list.extend(list1)
        printdata(main_list)
        
    else:
        list_file = os.listdir(dir)
        list_file = [dir + "\\" + each for each in list_file]
        list_file = [each for each in list_file if os.path.isfile(each)]
        list1 = search(str1, list_file, i = I)
        
    printdata(list1)

def printdata(list1):
    for each in list1:
        str1,file,*line = each
        if line:
            for num in line:
                print(str1,"\t",file,"\t",num)
        else:
            print(str1,"\t",file)

        
        
#OnlyFile("youtube","D:\FINAL PROJECT\PLAN",r = True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", nargs=2, help="search the file in the given folder")
    parser.add_argument("-i", action="store_true",help= "Case-Insensitive")
    parser.add_argument("-r", action="store_true",help= "Case-Insensitive")
    arg = parser.parse_args()
    
    if arg.f:
        str1,dir = arg.f
        #print(arg.f,arg.i)
        OnlyFile(str1, dir, I = arg.i, R = arg.r)
        
        
main()