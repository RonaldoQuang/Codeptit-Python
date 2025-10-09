"""
Cho một xâu ký tự chỉ bao gồm các ký tự chữ cái, độ dài không quá 100. Hãy thực hiện:
Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái viết thường lớn hơn hoặc bằng số lượng chữ cái viết hoa.
Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết hoa lớn hơn số lượng chữ cái viết thường.
Input
Chỉ có một xâu ký tự độ dài không quá 100, không có khoảng trống
Output
Ghi ra xâu kết quả
Input
vietHoa
VIETTHuonG
Output
viethoa
VIETTHUONG
"""
from math import *

if __name__ == '__main__':
    s=input()
    thuong=0
    hoa=0
    for i in s:
        if i.islower():
            thuong+=1
        else:
            hoa+=1
    if thuong>=hoa:
        print(s.lower())
    else:
        print(s.upper())
    
