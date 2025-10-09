"""
Cho số nguyên dương N, hãy liệt kê các số thuận nghịch M nhỏ hơn N và thỏa mãn điều kiện:
Chỉ có các chữ số 0,2,4,6,8
Số chữ số của khác nhau chia cho 2 dư 1
Input
Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)
Output
Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.
Input
2
30
100
Output
22
22 44 66 88
"""
from math import *

def check(s):
    if len(s)%2==1 or s!=s[::-1]:
        return 0
    for i in s:
        if int(i)%2==1:
            return 0
    return 1

if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        for i in range (22,n,2):
            if check(str(i)):
                print(i,end=' ')
        print()
                
    
    
    
