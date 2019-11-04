import numpy as np

x = np.array([[19, 30, 50, 10],
             [70, 30, 40, 60],
             [40, 8, 70, 20]])

m, n = x.shape

supply = [30, 50, 20]
demand = [20, 40, 30, 10]

c = np.array([[5, 0, 0, 2],
             [0, 0, 7, 2],
             [0, 8, 0, 10]])
p = np.zeros((3, 4), int)
u = [0, 0, 0]
v = [0, 0, 0, 0]

def cal():
    
    count = 0
    for i in range(m):
        u[i] = 0
    for j in range(n):
        v[j] = 0
        
    for i in range(m):
        for j in range(n):
            if c[i][j] != 0:
                count += 1
    if count == m+n-1:
        temp = 9
        while(temp > 0):
            for i in range(m):
                for j in range(n):
                    if c[i][j]:
                        if v[j] or u[i] or j == 3:
                            if v[j] or j == 3:
                                u[i] = x[i][j] - v[j]
                                temp = temp - i
                            elif u[i]:
                                v[j] = x[i][j] - u[i]
                                temp = temp - j
    else:
        print("Invalid ")
        
def set(p, q):
    for i in range(p+1, m):
        if c[i][q] != 0:
            p1, q1 = i, q
            break
    for j in range(q+1, n):
        if c[i][j] != 0:
            p2, q2 = i, j
            break
    p3, q3 = p, j
    minall = min(c[p1][q1], c[p3][q3])
    c[p][q] += minall
    c[p1][q1] -= minall
    c[p2][q2] += minall
    c[p3][q3] -= minall


def printCost():
    ans = 0
    for i in range(m):
        for j in range(n):
            if c[i][j] != 0:
                ans += c[i][j]*x[i][j]
    print("Cost is : ", ans)


print(c)


pen, flag, temp, minpen, pi, qj = 0, 0, 0, 0, 0, 0
xx=0
cal()
while(xx <3):
    xx -= 1
    
    print(u, v)
    for i in range(m):
        for j in range(n):
            p[i][j]=0
    print("Penalty  \n", p)
    for i in range(m):
        for j in range(n):
            if c[i][j] == 0:
                p[i][j] = x[i][j] - (u[i] + v[j])
                if(p[i][j] < 0):
                    flag = 1
                    if p[i][j] < minpen:
                        minpen = p[i][j]
                        pi, qj = i, j
    print("Penalty  \n", p)
    if flag == 0:
        temp = 1
        printCost()
    else:
        print("Neg penalty on :", pi, qj)
        set(pi, qj)
        cal()
        print(u, v)
        print("\nCo Matri: \n", x)
        print("\nAllocation  : \n", c)
        break
printCost()







