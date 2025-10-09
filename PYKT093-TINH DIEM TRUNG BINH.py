"""
Nhóm sinh viên PTIT cùng nhau đăng ký 3 môn học trong Học kỳ hè năm 2021 theo đúng thứ tự:
Môn 1: Lập trình hướng đối tượng: 3 tín chỉ
Môn 2: Ngôn ngữ lập trình C++: 3 tín chỉ
Môn 3: Tin học cơ sở 2: 2 tín chỉ
Người ta muốn xếp hạng thứ tự các sinh viên trong danh sách theo điểm trung bình giảm dần. 
Biết rằng điểm trung bình tính đến 2 số phần thập phân và nếu điểm bằng nhau thì thứ hạng cũng bằng nhau.
Input
Dòng đầu ghi số sinh viên (không quá 20).
Mỗi sinh viên ghi trên 4 dòng gồm:
Họ tên: có thể chưa được chuẩn hóa
Điểm môn 1
Điểm môn 2
Điểm môn 3
Các giá trị điểm là số nguyên và đảm bảo trong phạm vi từ 0 đến 10.
Output
Ghi ra danh sách sinh viên đã tính điểm và sắp xếp theo xếp hạng từ cao nhất đến thấp nhất, gồm các thông tin:
Mã sinh viên (tự động tăng theo thứ tự nhập, tính từ SV01)
Họ tên đã chuẩn hóa
Điểm trung bình với đúng 2 số phần thập phân
Xếp hạng
Chú ý: 2 sinh viên có điểm trung bình bằng nhau thì xếp hạng bằng nhau, và nếu có 2 sinh viên hạng là X thì sinh viên tiếp theo trong danh sách có hạng X+2.
Trong trường hợp xếp hạng bằng nhau thì cần sắp xếp theo mã sinh viên tăng dần.
Input
2
 ha Thi kieu     anh
7
6
7
Pham    THI  HAO
6
7
6
Output
SV01 Ha Thi Kieu Anh 6.63 1
SV02 Pham Thi Hao 6.38 2
"""

from math import *

from decimal import Decimal, ROUND_HALF_UP

class sv:
    def __init__(self, ma, ten, diem):
        self.ma=ma
        self.ten=ten
        self.diem=diem
    def chuanhoa(self):
        s=list(self.ten.split())
        self.ten=""
        for i in range (len(s)):
            s[i]=s[i][0:1].upper()+s[i][1:len(s[i])].lower()
            if i<len(s)-1:
                self.ten+=s[i]+" "
            else:
                self.ten+=s[i]
    def lam_tron(self):
        return Decimal(str(self.diem)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    def kq(self):
        print(self.ma,self.ten,self.lam_tron(),sep=" ",end=" ")       

if __name__ == '__main__':
    n=int(input())
    a=[]
    mp={}
    for i in range (1,n+1):
        if i<10:
            ma="SV0"+str(i)
        else:
            ma="SV"+str(i)
        ten=input()
        p1=float(input())
        p2=float(input())
        p3=float(input())
        diem=(p1*3.0+p2*3.0+p3*2.0)/8.0
        a.append(sv(ma,ten,diem))
    a.sort(key=lambda x:(-x.diem,x.ma))
    for i in range (len(a)):
        a[i].chuanhoa()
        a[i].kq()
        if i==0:
            print(i+1)
            mp[a[i].diem]=i+1
        else:
            if a[i].diem==a[i-1].diem:
                print(mp[a[i-1].diem])
                mp[a[i].diem]=mp[a[i-1].diem]
            else:
                print(i+1)
                mp[a[i].diem]=i+1