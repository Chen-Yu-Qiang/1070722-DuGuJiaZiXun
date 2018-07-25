import numpy as np
import matplotlib.pyplot as plt
import math
import pprint
def d(a,b):
    c = 0.0
    for i in range(len(a)):
        c+=math.pow(a[i] - b[i],2)
    return math.sqrt(c)
def ang(j1,j2,j3):
    a=[0,0,0]
    b=[0,0,0]
    for i in range(3):
        a[i]=j1[i]-j2[i]
        b[i]=j3[i]-j2[i]
    c=a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    l=math.sqrt((a[0]**2+a[1]**2+a[2]**2)*(b[0]**2+b[1]**2+b[2]**2))
    return math.acos(c/l)*(180/math.pi)
def datatoang(data):
    b=[ang(data["FootLeft"],data["AnkleLeft"],data["KneeLeft"]),#1
       ang(data["FootRight"],data["AnkleRight"],data["KneeRight"]),
       ang(data["FootLeft"],data["KneeLeft"],data["HipLeft"]),
       ang(data["FootRight"],data["KneeRight"],data["HipRight"]),
       ang(data["KneeLeft"],data["HipLeft"],data["SpineBase"]),#5
       ang(data["KneeRight"],data["HipRight"],data["SpineBase"]),
       ang(data["AnkleLeft"],data["SpineBase"],data["AnkleRight"]),
       ang(data["KneeLeft"],data["SpineBase"],data["KneeRight"]),
       ang(data["ElbowLeft"],data["SpineBase"],data["ElbowRight"]),
       ang(data["FootLeft"],data["SpineBase"],data["WristLeft"]),#10
       ang(data["FootRight"],data["SpineBase"],data["WristRight"]),
       ang(data["SpineBase"],data["SpineShoulder"],data["Head"]),
       ang(data["ElbowLeft"],data["SpineShoulder"],data["ElbowRight"]),
       ang(data["WristLeft"],data["SpineShoulder"],data["WristRight"]),
       ang(data["SpineBase"],data["ShoulderLeft"],data["ElbowLeft"]),#15
       ang(data["SpineBase"],data["ShoulderRight"],data["ElbowRight"]),
       ang(data["SpineShoulder"],data["ShoulderLeft"],data["ElbowLeft"]),
       ang(data["SpineShoulder"],data["ShoulderRight"],data["ElbowRight"]),
       ang(data["ShoulderLeft"],data["ElbowLeft"],data["WristLeft"]),
       ang(data["ShoulderRight"],data["ElbowRight"],data["WristRight"]),#20
       ang(data["ShoulderLeft"],data["Head"],data["ShoulderRight"])]
    a=[ang(data["FootLeft"],data["AnkleLeft"],data["KneeLeft"]),#1
       ang(data["FootRight"],data["AnkleRight"],data["KneeRight"]),
       ang(data["AnkleLeft"],data["KneeLeft"],data["HipLeft"]),
       ang(data["AnkleRight"],data["KneeRight"],data["HipRight"]),
       ang(data["KneeLeft"],data["HipLeft"],data["SpineBase"]),#5
       ang(data["KneeRight"],data["HipRight"],data["SpineBase"]),
       ang(data["AnkleLeft"],data["SpineBase"],data["AnkleRight"]),
       ang(data["KneeLeft"],data["SpineBase"],data["KneeRight"]),
       ang(data["ElbowLeft"],data["SpineBase"],data["ElbowRight"]),
       ang(data["FootLeft"],data["SpineBase"],data["WristLeft"]),#10
       ang(data["FootRight"],data["SpineBase"],data["WristRight"]),
       ang(data["SpineBase"],data["SpineShoulder"],data["Head"]),
       ang(data["ElbowLeft"],data["SpineShoulder"],data["ElbowRight"]),
       ang(data["WristLeft"],data["SpineShoulder"],data["WristRight"]),
       ang(data["SpineBase"],data["ShoulderLeft"],data["ElbowLeft"]),#15
       ang(data["SpineBase"],data["ShoulderRight"],data["ElbowRight"]),
       ang(data["SpineShoulder"],data["ShoulderLeft"],data["ElbowLeft"]),
       ang(data["SpineShoulder"],data["ShoulderRight"],data["ElbowRight"]),
       ang(data["ShoulderLeft"],data["ElbowLeft"],data["WristLeft"]),
       ang(data["ShoulderRight"],data["ElbowRight"],data["WristRight"]),#20
       ang(data["ShoulderLeft"],data["Head"],data["ShoulderRight"])]
    return b
csvname=input("請輸入檔名")
#csvname = "陳宇強"
f = open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\" + csvname + ".txt", "r")
data = f.readlines()
f.close()
adata =[{"time":0,
    "SpineBase":[0,0,0],
    "SpineMid":[0,0,0],
    "Neck":[0,0,0],
    "Head":[0,0,0],
    "ShoulderLeft":[0,0,0],
    "ElbowLeft":[0,0,0],
    "WristLeft":[0,0,0],
    "HandLeft":[0,0,0],
    "ShoulderRight":[0,0,0],
    "ElbowRight":[0,0,0],
    "WristRight":[0,0,0],
    "HandRight":[0,0,0],
    "HipLeft":[0,0,0],
    "KneeLeft":[0,0,0],
    "AnkleLeft":[0,0,0],
    "FootLeft":[0,0,0],
    "HipRight":[0,0,0],
    "KneeRight":[0,0,0],
    "AnkleRight":[0,0,0],
    "FootRight":[0,0,0],
    "SpineShoulder":[0,0,0],
    "HandTipLeft":[0,0,0],
    "ThumbLeft":[0,0,0],
    "HandTipRight":[0,0,0],
    "ThumbRight":[0,0,0]} for i in range(int(len(data)/25))]

for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i][2] = int(data[i][0]) * 60000 + int(data[i][1]) * 1000 + int(data[i][2])
    data[i][4] = float(data[i][4])
    data[i][5] = float(data[i][5])
    data[i][6] = float(data[i][6])
    ii=int(i/25)
    adata[ii][data[i][3]]=[data[i][4],data[i][5],data[i][6]]
    adata[ii]["time"]=data[i][2]
    print(ii)

for a in adata:
    p1=a["AnkleRight"]
    p2=a["AnkleLeft"]
    print(a["time"],p1,p2,d(p1,p2))
    #plt.scatter(a["time"],d(p1,p2),c="r")
p1=[]
p2=[]
for a in adata:
    p2+=[d(a["AnkleRight"],a["AnkleLeft"])]
    p1+=[a["time"]]
plt.plot(p1,p2)
max=[]
min=[]
pole=10#取四個極點
for i in range(1,len(adata)-1):
    if p2[i]>p2[i+1] and p2[i]>p2[i-1]:
        print(p1[i],"雙腳著地")
        max+=[[p1[i],p2[i]]]
        pole=pole-1
    if p2[i]<p2[i+1] and p2[i]<p2[i-1]:
        print(p1[i],"單腳站立")
        min+=[[p1[i],p2[i]]]
        pole=pole-1
    if pole==0:
        break
plt.show();

first=int(input("請輸入欲採計之第一個波谷(0開始)"))
print("雙腳著地")
pprint.pprint(max)
print("單腳站立")
pprint.pprint(min)
d1=[]
d2=[]
d3=[]
d4=[]

for a in adata:
    if a["time"]==max[first][0]:
        pprint.pprint(a)
        d1+=datatoang(a)
    elif a["time"]==max[first+1][0]:
        pprint.pprint(a)
        d2+=datatoang(a)
    elif a["time"]==min[first][0]:
        pprint.pprint(a)
        d1+=datatoang(a)
    elif a["time"]==min[first+1][0]:
        pprint.pprint(a)
        d2+=datatoang(a)

cla=input("請輸入為哪類(W=1 C=2 Z=3)")
num=input("請輸入為第幾筆")
f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + cla+"-"+num + ".txt", "w")
for a in d1:
    f.write(str(a)+"\n")
f.close()
f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + cla+"-"+str(int(num)+1)+ ".txt", "w")
for a in d2:
    f.write(str(a)+"\n")
f.close()