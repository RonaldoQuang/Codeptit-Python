"""
Cho dãy số nguyên A[] gồm có N phần tử. 
Nhiệm vụ của bạn là tìm dãy số B[] có tổng phần tử nhỏ nhất thỏa mãn tính chất A[i] / B[i] = A[i+1] / B[i+1] với mọi chỉ số i (0 ≤ i ≤ N-2).
Phép chia trong bài toán này là phép chia nguyên (tức là chỉ lấy phần nguyên của kết quả: ví dụ 5/3 = 1).   
Dữ liệu vào:
Dòng đầu tiên là số lượng phần tử N (1 ≤ N ≤ 1000).
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 2000).
Kết quả: 
In ra một số nguyên là tổng các phần tử của dãy số B[] tìm được.
Input
5
18 27 16 22 6
Output
25
"""
from math import * 

if __name__ == '__main__': 
    n=int(input())
    a=list(map(int,input().split()))
    m=1e9
    for i in range (len(a)):
        m=min(m,a[i])
    min1=1e9
    for i in range (m,0,-1):
        sum=0
        for j in range (n):
            if a[j]//i!=a[j]//(i+1):
                sum+=a[j]//(i+1)+1
            else:
                sum=0
                break
        if sum!=0:
            min1=min(min1,sum)
    print(min1)