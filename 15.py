# -*- coding: UTF-8 -*-

n=int(input("please input\n"))

with open("hightemp.txt","r") as f:
    for line in f.readlines()[-n:]:
        print(line.strip('\n'))
