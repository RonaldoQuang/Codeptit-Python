"""
Cho dãy số A gồm N phần tử là các số nguyên. Hãy tính tích lớn nhất của 2 hoặc 3 phần tử trong dãy.
Input
Dòng đầu tiên ghi số N (3 ≤ N ≤ 10000)
Dòng thứ 2 ghi N số của dãy A (|Ai| ≤ 1000)
Outpput
Ghi ra kết quả trên một dòng
Input
6
5 10 -2 3 5 2
Output
250
"""
from math import *

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print(max(a[0]*a[1],a[n-1]*a[n-2],a[0]*a[1]*a[n-1],a[n-1]*a[n-2]*a[n-3]))


                