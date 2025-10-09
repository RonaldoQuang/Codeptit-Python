"""
Khai báo lớp Số phức với hai thuộc tính là phần thực và phần ảo.
Viết chương trình thực hiện nhập hai số phức A, B và thực hiện các thao tác tính toán trên số phức
C = (A + B) x A
D = (A + B)2
Input:
Dòng đầu tiên là số bộ test T (T <= 100)
T dòng tiếp theo mỗi dòng gồm 4 số lần lượt là a, b, c, d, với -102 < a, b, c, d < 102.
Output:
Kết quả của hai phép tính theo định dạng trong ví dụ
Input
3
1 2 3 4
2 3 4 5
1 -2 5 -6
Output
-8 + 14i, -20 + 48i
-12 + 34i, -28 + 96i
-10 - 20i, -28 - 96i
"""

from math import *

class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc=thuc
        self.ao=ao
    def first(self, a):
        thuc=(self.thuc+a.thuc)*self.thuc-(self.ao+a.ao)*self.ao
        ao=self.thuc*(self.ao+a.ao)+(self.thuc+a.thuc)*self.ao
        c=SoPhuc(thuc,ao)
        return c
    def second(self, a):
        thuc=(self.thuc+a.thuc)**2-(self.ao+a.ao)**2
        ao=2*(self.thuc+a.thuc)*(self.ao+a.ao)
        d=SoPhuc(thuc,ao)
        return d
        
def kq(a, b):
    if a.ao<0:
        print(a.thuc," - ",abs(a.ao),"i, ",sep="",end="")
    else:
        print(a.thuc," + ",a.ao,"i, ",sep="",end="")
    if b.ao<0:
        print(b.thuc," - ",abs(b.ao),"i",sep="",end="")
    else:
        print(b.thuc," + ",b.ao,"i",sep="",end="")

if __name__ == '__main__':
    for _ in range (int(input())):
        a, b, c, d=map(int,input().split())
        A=SoPhuc(a,b)
        B=SoPhuc(c,d)
        C=A.first(B)
        D=A.second(B)
        kq(C,D)
        print()






        
        
        
        

                