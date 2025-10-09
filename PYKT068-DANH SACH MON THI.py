"""
Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
Thông tin về mỗi môn học gồm:
Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
Tên môn: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
Hình thức thi: xâu ký tự không có thể có  khoảng trống không quá 100 ký tự
Hãy nhập danh sách và in danh sách sắp xếp theo mã môn.
Input
Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.
Output
Ghi ra danh sách đã sắp xếp theo mã môn, thứ tự từ điển.
Input
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
Output
BAS1203 Giai tich 1 Thi viet + Van dap truc tuyen
MUL1320 Nhap mon da phuong tien Bai tap lon + Van dap truc tuyen
"""

from math import *

class mon:
    def __init__(self, ma, ten, ht):
        self.ma=ma
        self.ten=ten
        self.ht=ht
    def kq(self):
        print(self.ma,self.ten,self.ht)
    
if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range (n):
        ma=input()
        ten=input()
        ht=input()
        a.append(mon(ma,ten,ht))
    a.sort(key=lambda x:x.ma)
    for i in a:
        i.kq()