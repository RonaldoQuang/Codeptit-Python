"""
Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
Thông tin về mỗi môn học gồm:
Mã môn: xâu ký tự không có khoảng trống, không quá 15 ký tự
Tên môn: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
Hình thức thi: xâu ký tự không có thể có  khoảng trống, không quá 100 ký tự
Mỗi ca thi gồm các thông tin:
Mã ca thi: tự động tăng, tính từ C001
Ngày thi: đúng định dạng dd/mm/yyyy
Giờ thi: theo đúng định dạng hh:mm
Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
Lịch thi được xây dựng dựa trên mã môn và mã ca thi và mã nhóm lớp. 
Theo quy định, nhóm lớp đơn giản là các giá trị chữ số, bắt đầu từ 01 và không quá 99. 
Mỗi nhóm sẽ có số sinh viên tham gia ca thi đó.
Hãy nhập lịch thi và sắp xếp lại theo thứ tự thời gian. Nếu cùng giờ thì sắp theo mã ca thi (thứ tự từ điển).
Input - gồm 3 file văn bản.
MONTHI.in
Dòng đầu ghi số môn học. Mỗi môn ghi trên 3 dòng lần lượt là mã môn, tên môn, hình thức thi.
CATHI.in
Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.
LICHTHI.in
Dòng đầu ghi số lượng các dòng trong lịch thi.
Mỗi dòng tiếp theo ghi 4 thông tin: mã ca thi, mã môn, mã nhóm, số sinh viên. 
Mỗi thông tin cách nhau một khoảng trống.
Output
Ghi ra danh sách lịch thi đã sắp xếp theo yêu cầu, các thông tin cần liệt kê gồm:
Ngày thi
Giờ thi
ID Phòng thi
Tên môn
Nhóm
Số sinh viên
Các thông tin liệt kê cách nhau đúng một khoảng trống
MONTHI.in
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
CATHI.in
2
09/01/2022
15:30
70172
09/01/2022
10:00
70279
LICHTHI.in
2
C001 MUL1320 01 46
C002 BAS1203 04 72
"""

from math import *

import sys

class cathi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma=ma
        self.ngay=ngay
        self.gio=gio
        self.phong=phong

class lichthi:
    x=cathi
    def __init__(self, ma, tg, ngay, thang, nam, tg2, gio, phut, phong, mon, nhom, sv):
        self.ma=ma
        self.tg=tg
        self.ngay=ngay
        self.thang=thang
        self.nam=nam
        self.tg2=tg2
        self.gio=gio
        self.phut=phut
        self.phong=phong
        self.mon=mon
        self.nhom=nhom
        self.sv=sv
    def kq(self):
        print(self.tg,self.tg2,self.phong,self.mon,self.nhom,self.sv)

if __name__ == '__main__':
    mp, mp1={}, {}
    a=[]
    sys.stdin=open("MONTHI.in","r")
    for _ in range (int(input())):
        ma=input()
        ten=input()
        ht=input()
        mp[ma]=ten
    sys.stdin=open("CATHI.in","r")
    for i in range (1,int(input())+1):
        ma=f"C{i:03d}"
        ngay=input()
        gio=input()
        phong=input()
        mp1[ma]=cathi(ma,ngay,gio,phong)
    sys.stdin=open("LICHTHI.in","r")
    for _ in range (int(input())):
        ma, ma_mon, nhom, sv=input().split()
        tg=mp1[ma].ngay
        ngay, thang, nam=tg.split("/")
        ngay=int(ngay)
        thang=int(thang)
        nam=int(nam)
        tg2=mp1[ma].gio
        gio, phut=tg2.split(":")
        gio=int(gio)
        phut=int(phut)
        a.append(lichthi(ma,tg,ngay,thang,nam,tg2,gio,phut,mp1[ma].phong,mp[ma_mon],nhom,sv))
    a.sort(key=lambda x:(x.nam,x.thang,x.ngay,x.gio,x.phut,x.ma))
    for i in a:
        i.kq()