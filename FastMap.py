'''
@author: ankita
'''
import random
import math
from matplotlib import pyplot as plt
ob1=[]
ob2=[]
dis1=[]
M1=[]
Dnew=[]
X,PA=[],[]
Oa, Ob =0,0
flag=0
c=0
def ReadFile():
    global ob1, ob2, dis1, M1
    l1 = []
    with open("./fastmap-data.txt", "r") as fo:
        for line in fo:
            l1.append(line)
    fo.close()
    for line in l1:
        item = line.split()
        ob1.append(int(item[0]))
        ob2.append(int(item[1]))
        dis1.append(int(item[2]))
    k=0
    M1=make2dList(max(ob1), max(ob2))
    for i in range(10):
        for j in range(10):
            if((i)==(j)):
                M1[i][j]=0
            else:
                if M1[i][j]==0:
                    M1[i][j]= dis1[k]
                    M1[j][i]=dis1[k]
                    if(k<(len(dis1)-1)):
                        k=k+1
          
     
def make2dList(rows, cols):
    a=[]
    for row in xrange(rows+1): a += [[0]*cols]
    return a
  
def DistantObjects(B,M):  
    global Oa, Ob,flag
    d = max(M[B-1])
    for i in range (len (M[B-1])):
        if (d==M[B-1][i]):
            An=i
            break
    if(flag==0):
        Oa = An+1
    else:
        Ob= An+1
    if(Oa !=B):
        flag=1
        DistantObjects(Oa,M)  
    else:  
        pass


def D(i,M):
    dai= M[Oa-1][i]
    dab=M[Oa-1][Ob-1]
    dbi=M[Ob-1][i]
    q= float((dai**2 + dab**2 - dbi**2)/float(2*dab))
    return q
               

def NewD(i,j,X):
    Dij=M1[i][j]
    Xi=X[i][0]
    Xj=X[j][0]
    nD=math.sqrt((Dij**2)-(Xi-Xj)**2)
    return nD    
    
def FastMap(k,W):
    global X,PA,c, Oa, Ob,flag
    Ob= random.choice(ob1)
    #print "hhhh",Ob
    flag=0
    DistantObjects(Ob,W)  
    
    #print "fdfdddddddddd Oa Ob", Oa,Ob     
    PA[0][c]=Oa
    PA[1][c]=Ob
    for i in range(10):
        X[i][c]= D(i,W)
    #print X
    f()
    if(k<=1):
        return
    else:
        c=c+1
        FastMap(k-1, Dnew)
           
def f():
    for i in range(10):
        for j in range(10):
            if(i==j):
                Dnew[i][j]=0
            else:
                p=NewD(i,j,X)
                #print p
                Dnew[i][j] = p
    #print "DNew = "
    #for r in Dnew:
        #print r 
                   
def plotting():
    X1=[]
    X2=[]
    l1,n = [],[]
    for i in range (len(X)): 
        X1.append(X[i][0])
        X2.append(X[i][1])
    with open("./fastmap-wordlist.txt", "r") as fo:
        for line in fo:
            l1.append(line)
    fo.close()
    for line in l1:
        item = line.split()
        n.append(item[0])
    fig, ax = plt.subplots()
    ax.scatter(X1, X2)

    for i, txt in enumerate(n):
        ax.annotate(txt, (X1[i],X2[i]))
    plt.axis([0,15, 0, 10])              
    plt.show()
                

    
ReadFile()
X=make2dList(max(ob1), 2)
PA=make2dList(1, 2)
Dnew = make2dList(max(ob1), max(ob2))
FastMap(2, M1)



print "**********************************************************************"
print "Coordinates in 2d space:\n"

print X


print "\nPivot Matrix during the 2 iterations"
print "Pivot 1 = [", PA[0][0],",",PA[1][0],"]"
print "Pivot 1 = [", PA[0][1],", ",PA[1][1],"]\n"
    
print "***********************************************************************"
plotting()           