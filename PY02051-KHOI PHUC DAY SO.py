"""
Bình có sẵn dãy số A có N phần tử và tạo ra ma trận B kích thước N*N theo quy tắc:
B[i][i] = 0
B[i][j] = A[i] + A[j] (với i#j)
Bình đưa cho Nam ma trận B và đố Nam khôi phục dãy số A ban đầu.
Hãy giúp Nam nhé.
Input
Dòng đầu ghi số N (1 < N <= 1000).
N dòng tiếp theo ghi ma trận B, các số đều nguyên dương và không quá 100.000. 
Output
Ghi ra dãy số A tìm được trên một dòng, mỗi số cách nhau 1 khoảng trống.
Input
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
Output
2 1 4 5
"""
from math import *

if __name__ == '__main__':
    n=int(input())
    a=[]
    s=0
    for i in range (n):
        b=list(map(int,input().split()))
        s+=sum(b)
        a.append(b)
    sum=a[0][n-1]
    for i in range (n-1):
        sum+=a[i][i+1]
    sum//=2
    if n==2:
        print(1,s//2-1)
    else:
        for i in range (n):
            tong=0
            for j in range (n):
                tong+=a[i][j]
            print((tong-sum)//(n-2),end=" ")


                