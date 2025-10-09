"""
Cho dãy số A[], B[] và C[] là dãy không giảm và có lần lượt N, M, K phần tử. 
Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 20).
Mỗi test gồm số nguyên N, M và K (1≤ N, M, K ≤ 100 000).
Dòng tiếp theo gồm N số nguyên A[i], rồi M số nguyên B[i] và K số nguyên C[i].
(0 ≤ A[i], B[i], C[i] ≤ 109).
Output: 
Với mỗi test, in ra trên một dòng là đáp án thu được. Nếu không tìm được đáp án, in ra “NO”.
Input
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
Output
20 80
5 5
No
"""
from math import *

if __name__ == '__main__':
    for _ in range (int(input())):
        ok=0
        n, m, l=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=list(map(int,input().split()))
        i, j, k=0, 0, 0
        while i<n and j<m and k<l:
            if a[i]==b[j] and b[j]==c[k]:
                print(a[i],end=" ")
                i+=1
                j+=1
                k+=1
                ok=1
            elif i<n and j<m and a[i]<b[j]:
                i+=1
            elif j<m and k<l and b[j]<c[k]:
                j+=1
            else:
                k+=1
        if ok==0:
            print("NO",end="")
        print()

                