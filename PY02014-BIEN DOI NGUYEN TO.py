"""
Cho dãy số A[] có N số nguyên dương. 
Người ta muốn biến đổi tất cả các số trong dãy về số nguyên tố. 
Tại mỗi bước, mỗi số chưa nguyên tố được phép tăng hoặc giảm 1 đơn vị để biến đổi dần về số nguyên tố gần nhất.
Hãy tính xem cần ít nhất bao nhiêu bước cần thực hiện để biến đổi tất cả các phần tử của dãy về nguyên tố.
Input
Dòng đầu ghi số N là số phần tử của dãy (không quá 200).
Dòng thứ 2 ghi N số của dãy, các giá trị đều nguyên dương và không quá 10000.
Output
Ghi ra số bước ít nhất tính được.
Input
8
13 5 8 7 9 15 26 34
Output
3
"""

from math import *

prime=[1]*(10005)
pr=[1]*(10005)

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(10005))+1):
        if prime[i]:
            for j in range (i*i,10005,i):
                prime[j]=0

def nto():
    x=2
    for i in range (1,10001):
        if prime[i]:
            x=i
        pr[i]=x

def nto2():
    x=10007
    for i in range (10000,1,-1):
        if prime[i]:
            x=i
            pr[i]=i
        else:
            if x-i<abs(i-pr[i]):
                pr[i]=x
                
if __name__ == '__main__':
    sang()
    nto()
    nto2()
    n=int(input())
    a=list(map(int,input().split()))
    max1=-1e9
    for i in a:
        max1=max(max1,abs(i-pr[i]))
    print(max1)