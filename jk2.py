import numpy as np
cj=[12.0,16.0,0.0,0.0]
s1=np.array([[10.0,20.0,1.0,0.0],[8.0,8.0,0.0,1.0]])
cb=[0.0,0.0]
zj=[0.0,0.0,0.0,0.0]
cr=np.array([cj[0]-zj[0],cj[1]-zj[1],cj[2]-zj[2],cj[3]-zj[3]])
s=[120.0,80.0]
r=[0.0,0.0]
while(np.max(cr)>0.0):
    s2=np.array([s1[0],s1[1]])
    
    ty1,=np.where(cr==max(cr))
    ma=ty1[0]
    kc=np.array(s2[:,ma])
    r[0]=s[0]/kc[0]
    r[1]=s[1]/kc[1]
    mi=r.index(min(r))
    kr=np.array(s2[mi])
    ke=s2[mi][ma]
    j=0
    o=len(kc)
    while(j<o):
        if(j==mi):
            j=j+1
        else:
            s[j]=s[j]-((s[mi]*kc[j])/ke)
            j=j+1
    s[mi]=s[mi]/ke
    #print(r)
    #print(kr)
    #print(kc)
    #print(ke)
    i=0
    while(i<len(kc)):
        i2=0
        while(i2<len(kr)):
            if(i==mi):
                s1[i][i2]=s1[i][i2]/ke
                i2=i2+1
            else:
                s1[i][i2]=s2[i][i2]-((kr[i2]*kc[i])/ke)
                i2=i2+1            
        i=i+1
    print(s2)
    print(s1)
    cb[mi]=cj[ma]   
    i3=0
    while(i3<len(kr)):
        i2=0
        k=0
        while(i2<len(kc)):
            k=k+(s1[i2][i3]*cb[i2])
            i2=i2+1
        zj[i3]=k
        i3=i3+1  
    print(zj)
    cr[0]=cj[0]-zj[0]
    cr[1]=cj[1]-zj[1]
    cr[2]=cj[2]-zj[2]
    cr[3]=cj[3]-zj[3]
    print(cr)
    print(r)
    print(s)
yu=0
sol=0
while(yu<len(s)):
    sol=sol+cb[yu]*s[yu]
    yu=yu+1
print(sol)
    
    
    