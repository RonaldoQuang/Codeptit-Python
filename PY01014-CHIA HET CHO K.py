"""
Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:
a + b ≤ N
a + b chia hết cho K
Input
Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).
Output
Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.
Nếu không tìm được số nào in ra -1
Input
10 1 10
10 6 40
Output
-1
2 8 14 20 26
"""
from math import *

if __name__ == '__main__':
    a, K, N=map(int,input().split())
    ok=0
    i=a%K
    for b in range (K-i,N-a+1,K):
        ok=1
        print(b,end=" ")
    if ok==0:
        print("-1")


                
    
    
    
