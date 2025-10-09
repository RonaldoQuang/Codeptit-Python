"""
Cho dãy số A[] có N phần tử. 
Nhiệm vụ của bạn là tìm dãy con liên tiếp có độ dài nhỏ nhất, sao cho Ước số chung lớn nhất của tất cả các phần tử trong dãy đúng bằng K.
Input
Dòng đầu tiên là số lượng bộ test T (T <= 10).
Mỗi test bắt đầu bằng 2 số nguyên N và K.
Dòng tiếp theo gồm N số nguyên A[i] .
Giới hạn: 1 <= N <= 1000; 1 <= A[i], K <= 10^9
Output
Với mỗi test, hãy in ra đáp án trên một dòng. 
Nếu không tìm được dãy con nào, in ra -1.
Input
3
8 3
6 9 7 10 12 24 36 27
4 3
2 4 6 8
4 6
1 2 3 6
Output
2
-1
1
"""

from math import *
                
if __name__ == '__main__':
    for _ in range(int(input())):
        b=list(map(int,input().split()))
        if len(b)==1:
            x=int(input())
            b.append(x)
        n, k=b[0], b[1]
        a=list(map(int,input().split()))
        while len(a)<n:
            x=list(map(int,input().split()))
            for i in x:
                a.append(i)
        ok=0
        min1=1e9
        for i in range (n):
            x=a[i]
            for j in range (i,n):
                if gcd(x,a[j])==k:
                    ok=1
                    min1=min(min1,j-i+1)
                    break
                else:
                    x=gcd(x,a[j])
        if ok:
            print(min1)
        else:
            print(-1)

