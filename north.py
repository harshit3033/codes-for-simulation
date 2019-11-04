import numpy as np
d=np.array([20,95,35])
s=np.array([50,40,60])
a=np.array([[5,8,4],[6,6,3],[3,9,6]])
cost=0
i=0
k=0
j=0
print(a[0][0],s[j],d[k])
s1=np.shape(a)
print(s1)
d1=s1[0]+s1[1]-1
d2=s[0]
d3=s[1]
print(d1)
#a = np.delete(a, [0], axis=0)
#print(a[0][0])
while(i<d1):
    i=i+1

    print(a[0][0])
    f=int(d[k])
    
    if(k<d3 and j<d2 and d[k]>s[j]):
        
        cost=cost+(s[j]*a[0][0])
        
        d[k]=d[k]-s[j]
        j=j+1
        a=np.delete(a,[0],axis=0)
        print(a)
    else:
        cost=cost+(d[k]*a[0][0])
        s[j]=s[j]-d[k]
        k=k+1
        a=np.delete(a,[0],axis=1)
        print(a)
	
print(cost)		
		
