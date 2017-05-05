# -*- coding: UTF-8 -*-

i=0
n=int(input("please input\n"))
#n=int(input('please input'))
with open("hightemp.txt","r") as f:
        while i<n:
                print(f.readline().strip('\n'))
                i+=1