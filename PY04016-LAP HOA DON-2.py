"""
Khách sạn XYZ có đơn giá (theo ngày) được quy định khác nhau theo từng tầng. 
Khách hàng đến thuê phòng sẽ được tính tổng số tiền ở theo đơn giá cộng thêm chi phí dịch vụ phát sinh nếu có.
ĐƠN GIÁ THEO TẦNG:
Tầng     1     2     3     4
Giá      25    34    50    80
Hãy giúp khách sạn tính tiền phải trả cho từng khách hàng và sắp xếp theo thứ tự tổng tiền giảm dần.
Input
Dòng đầu ghi số khách hàng (không quá 20)
Mỗi khách hàng ghi trên 4 dòng gồm:
Tên khách hàng (xâu ký tự độ dài không quá 100)
Số phòng
Ngày nhận phòng (định dạng dd/mm/yyyy)
Ngày trả phòng (định dạng dd/mm/yyyy)
Tiền dịch vụ phát sinh (số nguyên dương nhỏ hơn 100)
Output
Ghi ra danh sách đã được sắp xếp theo tổng tiền giảm dần bao gồm lần lượt các thông tin:
Mã khách hàng (tự động tăng theo thứ tự nhập, tính từ KH01)
Tên khách hàng
Số phòng
Số ngày ở
Thành tiền
Input
3
Huynh Van Thanh   
103 
05/06/2010   
05/06/2010   
15
Le Duc Cong  
106 
08/03/2010   
01/05/2010   
220
Tran Thi Bich Tuyen   
207 
10/04/2010   
21/04/2010   
96
Output
KH02 Le Duc Cong 106 55 1595
KH03 Tran Thi Bich Tuyen 207 12 504
KH01 Huynh Van Thanh 103 1 40
"""

from math import *
from datetime import datetime

class kh:
    def __init__(self, ma, ten, phong, ngay, tien):
        self.ma=ma
        self.ten=ten
        self.phong=phong
        self.ngay=ngay
        self.tien=tien
    def kq(self):
        print(self.ma,self.ten,self.phong,self.ngay,self.tien)

if __name__ == '__main__':
    mp={
        '1': 25,
        '2': 34,
        '3': 50,
        '4': 80
    }
    a=[]
    n=int(input())
    for i in range (1,n+1):
        if i<10:
            ma="KH0"+str(i)
        else:
            ma="KH"+str(i)
        ten=input().strip()
        phong=input().strip()
        bd=input().strip()
        kt=input().strip()
        ngay=(datetime.strptime(kt,"%d/%m/%Y")-
        datetime.strptime(bd,"%d/%m/%Y")).days+1
        dv=int(input())
        tien=ngay*mp[phong[0]]+dv
        a.append(kh(ma,ten,phong,ngay,tien))
    a.sort(key=lambda x:-x.tien)
    for i in a:
        i.kq()
        



    

    
                