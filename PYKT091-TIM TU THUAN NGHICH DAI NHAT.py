"""
Cho dữ liệu vào dạng file văn bản.
Hãy tìm ra từ thỏa mãn tính chất thuận nghịch và có độ dài lớn nhất trong file đó. 
Đếm xem từ đó xuất hiện bao nhiêu lần.
Nếu có nhiều từ cùng có độ dài lớn nhất thì in ra tất cả các từ đó theo thứ tự xuất hiện trong file ban đầu.
Input: File văn bản VANBAN.in Không quá 1000 từ.
Output:
Ghi ra trên màn hình một dòng từ thuận nghịch có độ dài lớn nhất và số lần xuất hiện của nó. 
Nếu có nhiều từ cùng có độ dài lớn nhất thì các từ được liệt kê theo thứ tự xuất hiện ban đầu
Input
AAA BAABA HDHDH ACBSD SRGTDH DDDDS
DUAHD AAA AD DA HDHDH AAA AAA AAA AAA
DDDAS HDHDH HDH AAA AAA AAA AAA AAA
AAA AAA AAA
DHKFKH DHDHDD HDHDHD DDDHHH HHHDDD
TDTD
Output
HDHDH 3
"""

from math import *

import sys
    
if __name__ == '__main__':
    sys.stdin=open("VANBAN.in")
    mp={}
    max1=0
    s=sys.stdin.read().split()
    for i in s:
        if i==i[::-1]:
            mp[i]=mp.get(i,0)+1
            max1=max(max1,len(i))
    for x, y in mp.items():
        if len(x)==max1:
            print(x,y)
    
