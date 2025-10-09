"""
Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. 
Các giá trị đều nguyên dương và không quá 18 chữ số.
nhập vào hai phân số p và q. Tính tổng p + q, rút gọn và in ra kết quả.
Input
Có bốn số nguyên dương lần lượt là tử số và mẫu số của p rồi đến q.
Output
Ghi ra phân số tổng p + q ở dạng tối giản như trong ví dụ
Output
Ghi ra phân số tối giản như trong ví dụ
Input
123 456 12 34
Output
1609/2584
"""

from math import *

class PhanSo:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def rutgon(self):
        m=gcd(self.x,self.y)
        self.x//=m
        self.y//=m
    def cong(self, a):
        mc=self.y*a.y//gcd(self.y,a.y)
        c=PhanSo(mc//self.y*self.x+mc//a.y*a.x,mc)
        return c
    def kq(self):
        print(self.x,"/",self.y,sep="")



if __name__ == '__main__':
    tu, mau, tu1, mau1=map(int,input().split())
    a=PhanSo(tu, mau)
    b=PhanSo(tu1, mau1)
    c=a.cong(b)
    c.rutgon()
    c.kq()






        
        
        
        

                