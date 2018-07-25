import math
people=2
datanum=5
def d(a,b):
    c = 0.0
    for i in range(len(a)):
        c+=math.pow(a[i] - b[i],2)
    return math.sqrt(c)
adata=[[0 for i in range(datanum)] for j in range(people)]
for i in range(people):
    for j in range(datanum):
        f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + str(i+1)+"-"+str(j+1) + ".txt","r")
        adata[i][j]=f.readlines()
        f.close()
for i in range(len(adata)):
    for j in range(len(adata[i])):
        for k in range(len(adata[i][j])):
            adata[i][j][k]=float(adata[i][j][k])
while 1:
    testname=input("請輸入測試資料")
    f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + testname + ".txt","r")
    tdata=f.readlines()
    f.close()
    for i in range(len(tdata)):
        tdata[i]=float(tdata[i])
    nowmin=d(adata[0][0],tdata)
    whomin=0
    for i in range(people):
        for j in range(datanum):
            if(nowmin>d(adata[i][j],tdata)):
                whomin=i
                nowmin=d(adata[i][j],tdata)
    print(whomin+1,nowmin)