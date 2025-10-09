"""
Trên hệ thống phim của một website có các thông tin bộ phim bao gồm Mã phim, Tên phim, Ngày khởi chiếu, Số tập phim, Thể loại. 
Mã phim được đánh số tự động từ P001, P002 và tự động tăng dần. 
Thể loại phim bao gồm thông tin Mã thể loại và Tên thể loại. 
Mã thể loại được đanh số tự động tăng dần từ TL001, TL002
Cho danh sách các phim trên hệ thống, hãy thực hiện sắp xếp danh sách các bộ phim theo thứ tự ưu tiên ngày khởi chiếu tăng dần, tên phim sắp xếp theo thứ tự từ điển, số tập phim giảm dần.
Input:
Dòng đầu tiên cho 2 số N, M lần lượt là số lượng thể loại và số lượng bộ phim.
N dòng tiếp theo là thông tin tên thể loại. Mã thể loại tự động sinh theo thứ tự nhập vào
M dòng còn lại mỗi dòng là thông tin phim bao gồm Mã thể loại, ngày khởi chiếu (dd/mm/yyyy) tên phim và số tập phim (số nguyên tối đa 10000).
Output:
Danh sách phim đã sắp xếp như mẫu, mỗi phim trên một dòng
Input
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
Output
P001 Hai huoc 25/11/2021 Phim so 1 10
P003 Tinh cam 25/11/2021 Phim so 3 5
P002 Hai huoc 04/12/2021 Phim so 2 15
"""

from math import *

class tl:
    def __init__(self, ma, ten):
        self.ma=ma
        self.ten=ten

class phim:
    type=tl
    def __init__(self, type, ma, ngay, d, m, y, tt, tap):
        self.type=type
        self.ma=ma
        self.ngay=ngay
        self.d=d
        self.m=m
        self.y=y
        self.tt=tt
        self.tap=tap
    def kq(self):
        print(self.ma,self.type.ten,self.ngay,self.tt,self.tap)

if __name__ == '__main__':
    n, m=map(int,input().split())
    mp={}
    a=[]
    for i in range (1,n+1):
        if i<10:
            ma="TL00"+str(i)
        elif i>=10 and i<100:
            ma="TL0"+str(i)
        else:
            ma="TL"+str(i)
        ten=input()
        mp[ma]=tl(ma,ten)
    for i in range (1,m+1):
        if i<10:
            ma="P00"+str(i)
        elif i>=10 and i<100:
            ma="P0"+str(i)
        else:
            ma="P"+str(i)
        theloai=input()
        ngay=input()
        b=list(ngay.split("/"))
        d=b[0]
        m=b[1]
        y=b[2]
        tt=input()
        tap=int(input())
        a.append(phim(mp[theloai],ma,ngay,d,m,y,tt,tap))
    a.sort(key=lambda x:(x.y,x.m,x.d,x.tt,-x.tap))
    for i in a:
        i.kq()
    
    
