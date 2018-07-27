import os
import random
path="D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" 
nn=[495,467,482,512]
name=["1","2","3","4"]
def mymain(num,n):
    tdata=[-1 for i in range(n)]
    for i in range(n):
        a=random.randint(0,n-1)
        while 1:
            if not(a in tdata):
                tdata[i]=a
                break
            else:
                a=random.randint(0,n-1)
        #print(i)

    for i in range(n):
        os.rename(path+num+"-"+str(i+1)+".txt",path+"N-"+str(tdata[i]+1)+".txt")
        
    for i in range(n):
        os.rename(path+"N-"+str(i+1)+".txt",path+num+"-"+str(i+1)+".txt")

for i in range(4):
    mymain(name[i],nn[i])