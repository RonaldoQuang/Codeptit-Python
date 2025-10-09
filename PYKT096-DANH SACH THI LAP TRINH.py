"""
Mỗi team thi lập trình ICPC có 3 sinh viên đến từ cùng một trường đại học.
Thông tin về một team gồm:
Mã team (tự động tăng, tính từ Team01)
Tên team: không quá 50 ký tự
Tên trường: không quá 150 ký tự
Thông tin mỗi thí sinh gồm:
Mã thí sinh (tự động tăng, tính từ C001)
Họ và tên: không quá 50 ký tự.
Mã team
Hãy nhập và in ra danh sách thí sinh thi lập trình được sắp xếp theo họ tên (thứ tự từ điển).
Input
Dòng đầu ghi số team. Mỗi team ghi trên 2 dòng gồm tên team và tên trường.
Tiếp theo là một dòng ghi số thí sinh. Mỗi thí sinh ghi trên 2 dòng gồm họ tên và mã team.
Output
Ghi ra danh sách đã sắp xếp theo họ tên thí sinh (thứ tự từ điển) gồm các thông tin:
Mã thí sinh
Họ và tên thí sinh
Tên team
Tên trường
Input
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
Output
C003 Giang Minh Tung BAV_MIS Banking Academy of Vietnam
C001 Le Trung Toan BAV_MIS Banking Academy of Vietnam
C004 Nguyen Hang Giang FTU Knights1 Foreign Trade University
C005 Nguyen Thanh Nhan FTU Knights1 Foreign Trade University
C002 Nguyen Trinh Quoc Long BAV_MIS Banking Academy of Vietnam
C006 Nguyen Viet Duc FTU Knights1 Foreign Trade University
"""

from math import *

class part:
    def __init__(self, ma, ten):
        self.ma=ma
        self.ten=ten
        
class tv:
    x=part
    def __init__(self, x, ma, ten):
        self.x=x
        self.ma=ma
        self.ten=ten
    def kq(self):
        print(self.ma,self.ten,self.x.ma,self.x.ten)
                
if __name__ == '__main__':
    a=[]
    mp={}
    n=int(input())
    for i in range (1,n+1):
        if i<10:
            ma="Team0"+str(i)
        else:
            ma="Team"+str(i)
        ten=input()
        truong=input()
        mp[ma]=part(ten,truong)
    m=int(input())
    for i in range (1,m+1):
        if i<10:
            ma="C00"+str(i)
        elif i>=10 and i<100:
            ma="C0"+str(i)
        else:
            ma="C"+str(i)
        ten=input()
        team=input()
        a.append(tv(mp[team],ma,ten))
    a.sort(key=lambda x:x.ten)
    for i in a:
        i.kq()


    

    
                