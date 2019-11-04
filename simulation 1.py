import numpy as np

a=np.array ([[19,30,50,10],[70,30,40,60],[40,8,70,20]])
s=np.array ([7,9,18])
d=np.array ([5,8,7,14])
sum=0
i=0
j=0
while(i<4 and j<4):
    
    if(i==3 and j==3):
        print(sum)
        break
    r=np.amin(a)
    result = np.where(a == r)
    l=list(zip(result[0], result[1]))
    
    if(s[l[0][0]]>d[l[0][1]]):
        sum=sum+int(r*d[l[0][1]])
        s[l[0][0]]-=d[l[0][1]]
        d=np.delete(d,l[0][1])
        a=np.delete(a,l[0][1],axis=1)
        print(a)
        j=j+1
    else:
        sum=sum+int(r*s[l[0][0]])
        d[l[0][1]]-=s[l[0][0]]
        s=np.delete(s,l[0][0])
        a=np.delete(a,l[0][0],axis=0)
        print(a)
        i=i+1
    
