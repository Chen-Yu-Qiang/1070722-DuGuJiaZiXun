from sklearn.neural_network import MLPClassifier
people=5
datanum=130
adata=[[0 for i in range(datanum)] for j in range(people)]
for i in range(people):
    for j in range(datanum):
        f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + str(i+1)+"-"+str(j+1) + ".txt","r")
        adata[i][j]=f.readlines()
        f.close()
for i in range(len(adata)):
    for j in range(len(adata[i])):
        for k in range(len(adata[i][j])):
            adata[i][j][k]=(float(adata[i][j][k])-50)/100
data=[]
target=[]
for i in range(people):
    for j in range(datanum):
        data+=[adata[i][j]]
        target+=[i]


bdata=[[0 for i in range(167-datanum)] for j in range(3)]
for i in range(3):
    for j in range(datanum,167):
        f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + str(i+1)+"-"+str(j+1) + ".txt","r")
        bdata[i][j-datanum]=f.readlines()
        f.close()

for i in range(len(bdata)):
    for j in range(len(bdata[i])):
        for k in range(len(bdata[i][j])):
            bdata[i][j][k]=(float(bdata[i][j][k])-50)/100
testdata=[]
testtarget=[]
for i in range(len(bdata)):
    for j in range(len(bdata[i])):
        testdata+=[bdata[i][j]]
        testtarget+=[i]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(1000,100), random_state=1)
clf.fit(data,target)
output=clf.predict(testdata)p=[0,0,0,0,0]for i in range(len(output)):    if testtarget[i]!=output[i]:        p[testtarget[i]]=p[testtarget[i]]+1
print(len(output),p)