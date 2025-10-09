"""
Cho file dữ liệu dạng văn bản DATA.in có thể chứa cả số và ký tự.
Hãy loại bỏ các số nguyên int, sắp xếp các nội dung còn lại trong file theo thứ tự từ điển và in ra trên một dòng.
Chú ý: file dữ liệu có rất nhiều dòng với rất nhiều số và ký tự xen kẽ nhau.
Input
File văn bản DATA.in có không quá 1000 dòng. Dữ liệu đảm bảo số lượng các từ trong dãy kết quả nhỏ hơn 10000.
Output
Ghi ra các nội dung không thỏa mãn kiểu int trên một dòng, sắp xếp theo thứ tự từ điển, mỗi từ cách nhau một khoảng trống. 
Input
12 3 4 5 6 7
Aaa 1 1 Bbb XXX yyy 5 5
999999999999999999999999
9
Output
999999999999999999999999 Aaa Bbb XXX yyy
"""

from math import *

import sys
    
if __name__ == '__main__':
    sys.stdin=open("DATA.in")
    a=[]
    s=sys.stdin.read().split()
    for i in s:
        try:
            x=int(i)
            if x>2**63: 
                a.append(i)
        except: 
            a.append(i)
    a.sort()
    for i in a:
        print(i,end=" ")

    
    
