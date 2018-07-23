import numpy as np
import matplotlib.pyplot as plt
import math
def d(a,b):
    c=0.0
    for i in range(len(a)):
        c+=math.pow(a[i]-b[i],2)
    return math.sqrt(c)
#csvname=input("請輸入檔名")
csvname="陳宇強"
f = open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\"+csvname+".txt", "r")
data=f.readlines()
for i in range(len(data)):
    data[i]=data[i].split(",")
    data[i][2]=float(data[i][2])
    data[i][3]=float(data[i][3])
    data[i][4]=float(data[i][4])
for a in data:
    p1=[0,0,0]
    p2=p1
    if a[1]=="AnkleRight":
        #plt.scatter(float(a[2]),float(a[3]),c="r")
        p1=[a[2],a[3],a[4]]
    elif a[1]=="AnkleLeft":
        #plt.scatter(float(a[2]),float(a[3]),c="r")
        p2=[a[2],a[3],a[4]]  
    
    print(p1,p2,d(p1,p2))

#plt.show()