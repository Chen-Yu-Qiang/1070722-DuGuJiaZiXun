import math
import os
import matplotlib.pyplot as plt
people=4
#datanum=300
test_max_num=466
def d(a,b):
    c = 0.0
    for i in range(len(a)):
        c+=math.pow(a[i] - b[i],2)
    return math.sqrt(c)

def readdata():
    #adata=[[0 for i in range(datanum)] for j in range(people)]
    for i in range(people):
        for j in range(datanum):
            f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + str(i+1)+"-"+str(j+1) + ".txt","r")
            adata[i][j]=f.readlines()
            f.close()
    for i in range(len(adata)):
        for j in range(len(adata[i])):
            for k in range(len(adata[i][j])):
                adata[i][j][k]=float(adata[i][j][k])
def mytest(who,num):
    #testname=input("請輸入測試資料")
    f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + who+"-"+str(num)+".txt","r")
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
    #print(whomin+1,nowmin)
    return [whomin+1,nowmin]
p1=[]
p2=[]
p3=[]
p4=[]
for xxx in range(1,460,25):
    datanum=xxx
    p2+=[xxx]
    ave=0
    for yyy in range(10):
        os.system("py ..\\PythonRename\PythonRename.py")
        adata=[[0 for i in range(datanum)] for j in range(people)]
        readdata()

        for who in range(1,people+1):
            p=[0 for i in range(people+1)]
            for i in range(datanum+1,test_max_num):
                a=mytest(str(who),i)
                p[a[0]]=p[a[0]]+1
            print(who,p,p[who]/(test_max_num-datanum))
            ave+=p[who]/(test_max_num-datanum)
    p1+=[ave/40]
    print("+++++++")
plt.plot(p2,p1)
plt.show()