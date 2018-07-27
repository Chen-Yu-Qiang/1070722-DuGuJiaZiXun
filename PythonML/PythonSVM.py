import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import pprint

people=3
datanum=400
n_samples=people*datanum
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
digits = datasets.load_digits()
data=[]
target=[]
for i in range(people):
    for j in range(datanum):
        data+=[adata[i][j]]
        target+=[i]
bdata=[[0 for i in range(466-datanum)] for j in range(3)]
for i in range(3):
    for j in range(datanum,466):
        f=open("D:\\kinect\\1070722-讀出骨架\\1070722-DuGuJiaZiXun\\BodyBasics-WPF\\資料區\\角度資料\\" + str(i+1)+"-"+str(j+1) + ".txt","r")
        bdata[i][j-datanum]=f.readlines()
        f.close()

for i in range(len(bdata)):
    for j in range(len(bdata[i])):
        for k in range(len(bdata[i][j])):
            bdata[i][j][k]=float(bdata[i][j][k])
testdata=[]
testtarget=[]
for i in range(len(bdata)):
    for j in range(len(bdata[i])):
        testdata+=[bdata[i][j]]
        testtarget+=[i]
classifier = svm.SVC(gamma=0.001)

classifier.fit(data,target)
expected = testtarget
predicted = classifier.predict(testdata)
print("Confusion matrix:\n%s"% metrics.confusion_matrix(expected, predicted))print("Classification report for classifier"+":\n"+str(metrics.classification_report(expected, predicted))+"\n")