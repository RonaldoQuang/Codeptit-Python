"""
Công ty XYZ mỗi năm đều cập nhật hồ sơ và gán lại mã cho nhân viên (có đúng 5 ký tự) theo quy tắc sau:
Ký tự đầu tiên là phân loại nhân viên, có 4 nhóm là A, B, C, D
Hai chữ số tiếp theo mô tả số năm công tác
Hai ký tự cuối là mã phòng ban.
Dựa trên loại nhân viên và số năm công tác, hệ số nhân để tính lương được cho trong bảng sau:
Nhóm      1-3 năm     4-8 năm     9-15 năm     Trên 16 năm
A           10          12          14              20
B           10          11          13              16
C           9           10          12              14
D           8           9           11              13
Mỗi nhân viên theo hợp đồng sẽ có một giá trị lương cơ bản có thể rất khác nhau. 
Lương tháng được tính bằng tích của lương cơ bản với số ngày công và hệ số nhân.
Cho trước danh sách phòng ban, gồm mã phòng và tên phòng. 
Cho trước các thông tin nhân viên gồm mã, tên, lương cơ bản (tính theo ngày - đơn vị nghìn VNĐ) và số ngày công. 
Hãy tính toán và in ra bảng lương nhân viên trong tháng.
Input
Dòng đầu ghi số phòng ban, mỗi phòng ban viết trên một dòng gồm mã phòng và tên phòng.
Tiếp theo là một dòng ghi số nhân viên, mỗi nhân viên ghi trên 4 dòng gồm mã, tên, lương cơ bản (tính theo ngày), số ngày công.
Output
Lập bảng lương của nhân viên theo đúng thứ tự nhập. Mỗi nhân viên cần ghi ra các thông tin sau đây trên một dòng:
Mã nhân viên
Tên nhân viên
Phòng ban
Lương tháng
Input
2
HC Hanh chinh
KH Ke hoach Dau tu
2
C06HC
Tran Binh Minh
65
25
D03KH
Le Hoa Binh
59
24
Output
C06HC Tran Binh Minh Hanh chinh 16250000
D03KH Le Hoa Binh Ke hoach Dau tu 11328000
"""

from math import *

class nv:
    def __init__(self, ma, ten, phong, luong):
        self.ma=ma
        self.ten=ten
        self.phong=phong
        self.luong=luong
    def kq(self):
        print(self.ma,self.ten,self.phong,self.luong)

def heso(s):
    y = int(s[1:3])
    if 1<=y and y<=3:
        if s[0]=='A': return 10
        elif s[0]=='B': return 10
        elif s[0]=='C': return 9
        return 8
    elif 4<=y and y<=8:
        if s[0]=='A': return 12
        elif s[0]=='B': return 11
        elif s[0]=='C': return 10
        return 9
    elif 9<=y and y<=15:
        if s[0]=='A': return 14
        elif s[0]=='B': return 13
        elif s[0]=='C': return 12
        return 11
    else: 
        if s[0]=='A': return 20
        elif s[0]=='B': return 16
        elif s[0]=='C': return 14
        return 13
                
if __name__ == '__main__':
    mp={}
    a=[]
    for _ in range (int(input())):
        b=list(input().split())
        s=""
        for i in range (1,len(b)):
            if i<len(b)-1:
                s+=b[i]+" "
            else:
                s+=b[i]
        mp[b[0]]=s
    for _ in range (int(input())):
        ma=input()
        ten=input()
        cong=int(input())
        ngay=int(input())
        a.append(nv(ma,ten,mp[ma[3:5]],cong*ngay*heso(ma)*1000))
    for i in a:
        i.kq()
    
        



    

    
                