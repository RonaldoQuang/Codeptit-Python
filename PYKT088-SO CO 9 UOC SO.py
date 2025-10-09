"""
Cho số nguyên dương N. Hãy đếm các số nguyên dương không lớn hơn N và có đúng 9 ước số.
Input
Chỉ có một dòng ghi số N (1 ≤ N ≤ 109).
Output
Ghi ra số lượng các số có 9 chữ số
Input
888
Output
8
"""

from math import *

max=100005
prime=[1]*(max)
a=[0]*(max+1)

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(max))+1):
        if prime[i]:
            for j in range (i*i,max,i):
                prime[j]=0

def sang1():
    for i in range (2,max+1):
        a[i]=i
    for i in range (2,int(sqrt(max))+1):
        if a[i]==i:
            for j in range (i*i,max+1,i):
                if a[j]==j:
                    a[j]=i

if __name__ == '__main__':
    sang()
    sang1()
    n=int(input())
    cnt=0
    for i in range (2,round(n**(1/8))+1):
        if prime[i] and i**8<=n:
            cnt+=1
    for i in range (2,int(sqrt(n))+1):
        if prime[a[i]] and prime[i//a[i]] and a[i]!=i//a[i] and i**2<=n:
            cnt+=1
    print(cnt)

        