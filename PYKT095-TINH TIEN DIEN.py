"""
Các hộ gia đình trong thành phố X được chia thành 3 loại A, B, C với định mức sử dụng điện như sau:
Loại A: Định mức 100 kWh
Loại B: Định mức 500 kWh
Loại C: Định mức 200 kWh
Hãy tính toán số tiền phải thanh toán theo quy tắc:
Tính tiền trong định mức:
Nếu số điện (Số cuối - Số đầu) nhỏ hơn định mức thì bằng số điện * 450                 
Nếu số điện lớn hơn hoặc bằng định mức thì bằng định mức *450                                             
Tiền vượt định mức                                                                                  
Nếu số điện lớn hơn định mức thì bằng (số điện - định mức) *1000                                      
Ngược lại thì bằng 0
Thuế VAT = 5% số tiền vượt định mức
Chú ý: tiền thuế VAT cũng là số nguyên dương nên có thể lấy số tiền vượt định mức chia phần nguyên cho 20.
Số tiền phải nộp = Tiền trong định mức + Tiền vượt định mức + Thuế VAT
Input
Dòng đầu ghi số khách hàng (không quá 50).
Mỗi khách hàng ghi trên 2 dòng:
Họ tên: có thể chưa chuẩn hóa
Loại hộ gia đình, chỉ số đầu, chỉ số cuối. Mỗi thông tin cách nhau một khoảng trống.
Output
Ghi ra danh sách đã sắp xếp theo tổng số tiền phải trả giảm dần gồm các thông tin:
Mã khách hàng: tính từ KH01 theo thứ tự nhập
Họ tên đã chuẩn hóa
Tiền trong định mức
Tiền vượt định mức
Thuế VAT
Tổng số tiền phải nộp.
Dữ liệu đảm bảo không có hai hộ gia đình nào có cùng số tiền nộp bằng nhau.
Input
2
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 160
Output
KH01 Nguyen Hong Ngat 35100 0 0 35100
KH02 Chu Thi Minh 18000 0 0 18000
"""

from math import *

class kh:
    def __init__(self, ma, ten, trong, vuot, thue, tien):
        self.ma=ma
        self.ten=ten
        self.trong=trong
        self.vuot=vuot
        self.thue=thue
        self.tien=tien
    def chuanhoa(self):
        s=list(self.ten.split())
        self.ten=""
        for i in range (len(s)):
            s[i]=s[i][0:1].upper()+s[i][1:len(s[i])].lower()
            if i<len(s)-1:
                self.ten+=s[i]+" "
            else:
                self.ten+=s[i]
    def kq(self):
        print(self.ma,self.ten,self.trong,self.vuot,self.thue,self.tien)
                
if __name__ == '__main__':
    a=[]
    mp={
        "A": 100,
        "B": 500,
        "C": 200
    }
    for i in range (1,int(input())+1):
        if i<10:
            ma="KH0"+str(i)
        else:
            ma="KH"+str(i)
        ten=input()
        loai, cu, moi=input().split()
        cu, moi=int(cu), int(moi)
        if moi-cu<mp[loai]:
            trong=(moi-cu)*450
        else:
            trong=mp[loai]*450
        if (moi-cu)>mp[loai]:
            vuot=(moi-cu-mp[loai])*1000
        else:
            vuot=0
        thue=vuot//20
        a.append(kh(ma,ten,trong,vuot,thue,trong+vuot+thue))
    a.sort(key=lambda x:-x.tien)
    for i in a:
        i.chuanhoa()
        i.kq()
        



    

    
                