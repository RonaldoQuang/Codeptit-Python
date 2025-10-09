"""
Chúng ta đều biết chỉ có 4 chữ số nguyên tố là 2, 3, 5, 7. 
Hãy liệt kê tất cả các số có ít nhất 4 chữ số nhưng không quá N chữ số và thỏa mãn tất cả các điều kiện sau:
Chỉ có các chữ số 2, 3, 5, 7
Có đầy đủ 4 chữ số 2, 3, 5, 7
Không phải là số chẵn.
Input
Chỉ có 1 dòng ghi số N (3 < N < 10)
Output
Ghi ra lần lượt các số thỏa mãn theo thứ tự tăng dần, mỗi số trên một dòng 
Input
4
Output
2357
2375
2537
2573
2735
2753
3257
3275
3527
3725
5237
5273
5327
5723
7235
7253
7325
7523
"""

from math import *

se=set()

def Try(s,n):
    if len(s)>n:
        return
    if len(s)>=4 and len(s)<=n and "2" in s and "3" in s and "5" in s and "7" in s and s[len(s)-1]!='2':
        se.add(int(s))
    if len(s)<n:
        Try(s+"2",n)
        Try(s+"3",n)
        Try(s+"5",n)
        Try(s+"7",n)
    
if __name__ == '__main__':
    n=int(input())
    Try("",n)
    for i in sorted(se):
        print(i)
    
    
