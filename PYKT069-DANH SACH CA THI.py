"""
Học viện Hoàng gia tổ chức thi thời kỳ giãn cách theo các hình thức thi linh hoạt, phù hợp với từng môn học.
Mỗi ca thi gồm các thông tin:
Mã ca thi: tự động tăng, tính từ C001
Ngày thi: đúng định dạng dd/mm/yyyy
Giờ thi: theo đúng định dạng hh:mm
Phòng thi: một dãy chữ số đại diện cho ID phòng online, không quá 12 chữ số
Hãy nhập danh sách các ca thi và sắp xếp theo thời gian thi (từ sớm nhất đến muộn nhất). Nếu hai ca thi cùng giờ thì sắp xếp theo mã ca thi tăng dần.
Input - file văn bản CATHI.in
Dòng đầu ghi số ca thi. Mỗi ca thi ghi trên 3 dòng gồm Ngày, Giờ và ID phòng thi.
Output
Ghi ra danh sách các ca thi theo thứ tự thời gian, nếu cùng giờ thì sắp xếp theo mã ca thi.
Input
2
09/01/2022
15:30
70172
09/01/2022
10:00
70279
Output
C002 09/01/2022 10:00 70279
C001 09/01/2022 15:30 70172
"""

from math import *

import sys

class cathi:
    def __init__(self, ma, ngay, d, m, y, tg, gio, phut, id):
        self.ma=ma
        self.ngay=ngay
        self.d=d
        self.m=m
        self.y=y
        self.tg=tg
        self.gio=gio
        self.phut=phut
        self.id=id
    def kq(self):
        print(self.ma,self.ngay,self.tg,self.id)
    
if __name__ == '__main__':
    sys.stdin=open("CATHI.in")
    a=[]
    n=int(input())
    for i in range (1,n+1):
        if i<10:
            ma="C00"+str(i)
        elif i<100 and i>=10:
            ma="C0"+str(i)
        else:
            ma="C"+str(i)
        ngay=input()
        c=list(ngay.split("/"))
        d=int(c[0])
        m=int(c[1])
        y=int(c[2])
        tg=input()
        b=list(tg.split(":"))
        gio=int(b[0])
        phut=int(b[1])
        id=input()
        a.append(cathi(ma,ngay,d,m,y,tg,gio,phut,id))
    a.sort(key=lambda x:(x.y,x.m,x.d,x.gio,x.phut,x.ma))
    for i in a:
        i.kq()

        
    
    
