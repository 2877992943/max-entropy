import random
import os
import sys
import math



inpath = "D://python2.7.6//MachineLearning//maxEntropy//me-0"
outfile1 = "D://python2.7.6//MachineLearning//maxEntropy//1.txt"
outfile2 = "D://python2.7.6//MachineLearning//maxEntropy//2.txt"
outfile3 = "D://python2.7.6//MachineLearning//maxEntropy//3.txt"
outfile4 = "D://python2.7.6//MachineLearning//maxEntropy//4.txt"
     
 
global feaDic; 
global feaParaDic; 
global feaEmp; 
global docList; 
global classList;classList=["business","auto","sport","it","yule"]
 
 
global maxIter;maxIter=20
######################

def loadData():
    global feaDic;feaDic={}
    global feaParaDic;feaParaDic={}
    global feaEmp;feaEmp={}
    global docList;docList=[]

    ###################build docList wordDic 

    for filename in os.listdir(inpath):
        for c in classList:
            if filename.find(c)!=-1:
                eachDoc=[{},c,0]
        content=open(inpath+'/'+filename,'r').read().strip()
        words=content.replace('\n',' ').split(' ')
        #############
        for word in words:
            if len(word.strip())<=2:continue
            if word not in feaDic:
                feaDic[word]={"business":0,"auto":0,"sport":0,"it":0,"yule":0};
                feaEmp[word]={"business":0,"auto":0,"sport":0,"it":0,"yule":0}
                feaParaDic[word]={"business":0,"auto":0,"sport":0,"it":0,"yule":0}
                eachDoc[0][word]=1;
            elif word in feaDic:
                if word not in eachDoc[0]:eachDoc[0][word]=1
                else:eachDoc[0][word]+=1
        docList.append(eachDoc)

    for wid in feaEmp:
        for c in classList:
            ######for each f(w,c)
            for doc in docList:
                if doc[1]==c and wid in doc[0]:
                    feaEmp[wid][c]+=doc[0][wid]
                    feaDic[wid][c]=1
    ##########  f# for each sample
    for doc in docList:
        for w,v in doc[0].items():
            doc[2]+=v
                
                    
     
 

    ###################output    
    outPutfile=open(outfile1,'w')
    for (wid,d) in feaDic.items():
        outPutfile.write(str(wid));
        outPutfile.write('\n')
        outPutfile.write(str(feaEmp[wid]))
        outPutfile.write('\n')
        outPutfile.write(str(feaDic[wid]));
        outPutfile.write('\n')
    outPutfile.close()
 
    outPutfile=open(outfile2,'w')
    for i in range(len(docList)):
        outPutfile.write(str(docList[i]))
        outPutfile.write('\n')
    outPutfile.close() 

    

def train():
    global feaDic; 
    global feaParaDic; 
    global feaEmp; 
    global docList;
    for wid in feaDic.keys():
        for c in classList:
            
            ############for each fi(wid c)
            empEf=feaEmp[wid][c]
            eq=0.0
            eqD=0.0
            change1=-10.0
            change2=0.0;i=0
            while abs(change2-change1)>0.1 and i<20:
                change1=change2;
                for doc in docList:
                    if wid in doc[0] and c==doc[1]:###if f(w c)==1
                        ff=doc[2]
                        pyx=calcPyx(doc,c)
                        eq+=pyx*math.exp(change1*ff); 
                        eqD+=pyx*math.exp(change1*ff)*ff;
                change2=change1-(eq-empEf)/(eqD+0.00001)
                i+=1
                #print change1,change2
            ##############
            feaParaDic[wid][c]+=change2;#print 'w',change2,'\n'

    ###################
    logll=0.0
    for doc in docList:
        trueL=doc[1]
        p=calcPyx(doc,trueL);print p
        logll+=math.log(p)
    print 'loglikely',logll
                
                    
                
                
def calcPyx(doc,c):
    global feaDic; 
    global feaParaDic; 
    global feaEmp; 
    global docList;
    ##########calc fenmu first Z
    pyx={};fenmu=0.0
    for cc in classList:
        pyx[cc]=0.0
        fenzi=0.0
        for wid in doc[0]:
            fenzi+=feaDic[wid][cc]*feaParaDic[wid][cc]
        pyx[cc]=math.exp(fenzi)
        fenmu+=pyx[cc]

    for cc in classList:
        pyx[cc]/=fenmu

    return pyx[c]
                 
            
 
        
    
    



#########################main
loadData()
for i in range(10):
    
    train()
        
    
    
    







    
    
