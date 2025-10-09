"""
Theo quy định mới, điểm tuyển sinh vào trường đại học XYZ sau khi tính tổng sẽ được cộng ưu tiên, cụ thể:
Thí sinh khu vực 1 ưu tiên 1.5 điểm
Thí sinh khu vực 2 ưu tiên 1 điểm
Thí sinh khu vực 3 không ưu tiên
Thí sinh dân tộc Kinh không ưu tiên
Thí sinh các dân tộc khác ưu tiên 1.5 điểm
Hãy tính tổng điểm đã ưu tiên và xác định tình trạng trúng tuyển. Biết điểm chuẩn của trường năm nay là 20.5 điểm.
Input
Dòng đầu ghi số thí sinh.
Mỗi thí sinh ghi trên 4 dòng gồm:
Họ tên: có thể chưa chuẩn hóa
Điểm thi: giá trị số thực không quá 30
Dân tộc
Khu vực
Output
Ghi ra danh sách đã sắp xếp theo tổng điểm (đã tính ưu tiên) giảm dần, nếu tổng điểm bằng nhau thì sắp xếp theo mã thí sinh tăng dần. 
Các thông tin cần liệt kê gồm:
Mã thí sinh (tính theo thứ tự nhập từ TS01)
Họ tên đã chuẩn hóa
Tổng điểm với đúng 1 chữ số phần thập phân
Trạng thái: Do hoặc Truot
Input
2
Nguyen  hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3
Output
TS01 Nguyen Hong Ngat 23.5 Do
TS02 Chu Thi Minh 15.5 Truot
"""

from math import *

class ts:
    def __init__(self, ma, ten, diem, tt):
        self.ma=ma
        self.ten=ten
        self.diem=diem
        self.tt=tt
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
        print(self.ma,self.ten,"{:.1f}".format(self.diem),self.tt)       

if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range (1,n+1):
        if i<10:
            ma="TS0"+str(i)
        else:
            ma="TS"+str(i)
        ten=input()
        diem=float(input())
        dt=input()
        kv=int(input())
        if dt!="Kinh":
            diem+=1.5
        if kv==1:
            diem+=1.5
        elif kv==2:
            diem+=1.0
        if diem>=20.5:
            tt="Do"
        else:
            tt="Truot"
        a.append(ts(ma,ten,diem,tt))
    a.sort(key=lambda x:(-x.diem,x.ma))
    for i in a:
        i.chuanhoa()
        i.kq()