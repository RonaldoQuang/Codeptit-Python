"""
Một số số nguyên dương có thể được biểu diễn thành tổng của các số nguyên dương liên tiếp.
Ví dụ: 6 = 1 +2 + 3 hoặc 9 = 4 + 5 hoặc 9 = 2 + 3 + 4
Cho số nguyên dương N không quá 9 chữ số. 
Hãy đếm xem có bao nhiêu cách biểu diễn N thành tổng các số nguyên dương liên tiếp.
Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi một số nguyên dương N, không quá 9 chữ số.
Output
Ghi ra số cách tìm được.
Input
3
6
8
9
Output
1
0
2
"""

from math import *

if __name__=='__main__':
    for _ in range (int(input())):
        n=int(input())
        cnt, k=0, 2
        while k*(k-1)/2<n:
            if (n-k*(k-1)/2)%k==0:
                cnt+=1
            k+=1
        print(cnt)