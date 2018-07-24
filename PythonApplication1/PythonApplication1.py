import numpy as np
import matplotlib.pyplot as plt
import math
import pprint
def d(a,b):
    c = 0.0
    for i in range(len(a)):
        c+=math.pow(a[i] - b[i],2)
    return math.sqrt(c)
def 
csvname=input("請輸入檔名")
#csvname = "陳宇強"
f = open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\" + csvname + ".txt", "r")
data = f.readlines()
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
pole=4#取四個極點
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

print("雙腳著地")
pprint.pprint(max)
print("單腳站立")
pprint.pprint(min)
for a in adata:
    if a["time"]==max[0][0]:
        pprint.pprint(a)
    elif a["time"]==max[1][0]:
        pprint.pprint(a)
    elif a["time"]==min[0][0]:
        pprint.pprint(a)
    elif a["time"]==min[1][0]:
        pprint.pprint(a)
plt.show()


 