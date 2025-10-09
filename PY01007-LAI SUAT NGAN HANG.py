"""
Ngân hàng thông báo lãi suất là X % mỗi năm.
Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.
Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.
Input
Dòng đầu ghi số bộ test.
Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0<N<M<100000.
Output
Ghi ra số năm tính được.
Input
2
200.00 6.5 300
500 4 1000.00
Output
7
18
"""

from math import *

if __name__ == '__main__':
    t=int(input())
    while t>0:
        a, b, c= map(float,input().split())
        if int(log(float(c)/a,1+float(b)/100))==log(float(c)/a,1+float(b)/100):
            print(int(log(float(c)/a,1+float(b)/100)))
        else:
            print(int(log(float(c)/a,1+float(b)/100))+1)
        t-=1