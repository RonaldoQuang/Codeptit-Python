from math import * 

def tong(a, b, c, d):
    sum=0
    for i in range (c,c+3):
        for j in range (d,d+3):
            sum+=a[i][j]*b[i-c][j-d]
    return sum

if __name__ == '__main__':
    for _ in range (int(input())):
        n, m=map(int,input().split())
        sum=0
        a=[]
        for i in range (n):
            b=list(map(int,input().split()))
            a.append(b)
        b=[]
        for i in range (3):
            c=list(map(int,input().split()))
            b.append(c)
        for i in range (n-2):
            for j in range (m-2):
                sum+=tong(a,b,i,j)
        print(sum)
        