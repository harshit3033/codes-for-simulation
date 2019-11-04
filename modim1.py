import numpy as np
b=np.array([[5,0,0,2],[0,0,7,2],[0,8,0,10]])
a = np.array([[19,30,50,10],[70,30,40,60],[40,8,70,20]])
d = [30,50,20]
c=np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
s = [20,40,30,10]
u=[0,0,0]
v=[0,0,0,0]



for i in range(3):
    j=3
    if(i==0):
        v[i]=3*3
    elif(i==1):
        v[i]=9*-1-(i*3)
    else:
        v[i]=-20
for i in range(3):
    j=3    
    while(j>0):
        for k in range(3):
            if(b[i][j]>0):
                u[i]=a[i][j]-v[j]
        j=j-1

print(a)
print(v)
print(u)
for i in range(3):
    
    for j in range(3):
        if(b[i][j]==0):
            c[i][j]=c[i][j]-(u[i]+v[j])+a[i][j]
           
            
print(c)
h=np.amin(c)
if(np.amin(c)<0):
    
    result = np.where(c == h)
    l=list(zip(result[0], result[1]))
l1=[]
l1.append(l[0][0])
l1.append(l[0][1])
print(l1)
l2=[]    
    
m=0
co=0
b
print (l)
hy=l[0][0]
hy1=l[0][1]
b[hy][hy+2]=b[hy][hy+2]-2
b[hy+1][hy]=b[hy+1][hy]-2
b[hy+1][hy+2]=b[hy+1][hy+2]+2
b[hy][hy1]=b[hy][hy1]+2

for i in range(3):
    
    for j in range(4):
        if(b[i][j]>0):
            co=co+(a[i][j]*b[i][j])
        
print(co)


    
    

