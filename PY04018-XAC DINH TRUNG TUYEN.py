"""
Trường THPT ACB tuyển giáo viên mới cho ba môn Toán, Lý, Hóa. 
Theo yêu cầu mới, bài thi tuyển gồm 2 nội dung: Tin học và Chuyên môn. 
Điểm thi Tin học sẽ được nhân đôi khi tính tổng điểm.
Mỗi GV có thể có điểm ưu tiên được xét theo mã như trong bảng sau:
Mã ưu tiên     Điểm
    1           2.0
    2           1.5
    3           1.0
    4           0.0
Mã xét tuyển gồm 2 thành phần. 
Chữ cái đầu tiên ứng với môn học: A là Toán, B là Lý và C là Hóa; tiếp theo là 1 chữ số thể hiện mã ưu tiên.
Tổng điểm sau khi cộng điểm ưu tiên nếu từ 18 trở lên sẽ được xét TRÚNG TUYỂN, nhỏ hơn sẽ bị LOẠI.
Viết chương trình nhập danh sách điểm thi và sắp xếp GV theo thứ tự tổng điểm giảm dần. 
Mã GV dự thi được tự động gán theo thứ tự bắt đầu từ 01.
Input
Dòng đầu thi số giáo viên đăng ký thi tuyển (không quá 20).
Mỗi GV được viết trên 4 dòng gồm:
Tên GV (xâu ký tự độ dài không quá 50)
Mã xét tuyển
Điểm tin học (số thực trong phạm vi 0 đến 10)
Điểm chuyên môn (số thực trong phạm vi 0 đến 10)
Output
Ghi ra danh sách đã sắp xếp. 
Thông tin mỗi GV gồm: Mã GV, Tên, Môn học, Tổng điểm (1 chữ số phần thập phân), Kết quả. 
Mỗi thông tin cách nhau một khoảng trống.
Input
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
Output
GV03 Hoang Thi Tam HOA 21.5 TRUNG TUYEN
GV01 Le Van Binh TOAN 19.0 TRUNG TUYEN
GV02 Tran Van Toan LY 16.0 LOAI
"""

from math import *

class gv:
    def __init__(self, ma, ten, mon, diem, tt):
        self.ma=ma
        self.ten=ten
        self.mon=mon
        self.diem=diem
        self.tt=tt
    def kq(self):
        print(self.ma,self.ten,self.mon,"{:.1f}".format(self.diem),self.tt)
    
if __name__ == '__main__':
    a=[]
    n=int(input())
    for i in range (1,n+1):
        ma=""
        if i<10:
            ma+="GV0"+str(i)
        else:
            ma+="GV"+str(i)
        ten=input()
        sign=input()
        if sign[0]=='A':
            mon="TOAN"
        elif sign[0]=='B':
            mon="LY"
        elif sign[0]=='C':
            mon="HOA"
        tin=float(input())
        cm=float(input())
        if sign[1]=='1':
            diem=tin*2.0+cm+2.0
        elif sign[1]=='2':
            diem=tin*2.0+cm+1.5
        elif sign[1]=='3':
            diem=tin*2.0+cm+1.0
        else:
            diem=tin*2.0+cm
        if diem>=18:
            tt="TRUNG TUYEN"
        else:
            tt="LOAI"
        a.append(gv(ma,ten,mon,diem,tt))
    a.sort(key=lambda x:-x.diem)
    for i in a:
        i.kq()