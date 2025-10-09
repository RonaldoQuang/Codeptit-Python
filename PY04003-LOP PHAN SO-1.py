"""
Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. 
Các giá trị đều nguyên dương và không quá 18 chữ số.
Nhập vào một phân số và in ra phân số đó ở dạng tối giản.
Input
Có hai số nguyên dương lần lượt là tử số và mẫu số.
Output
Ghi ra phân số tối giản như trong ví dụ
Input
123 456
Output
41/152
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
    def kq(self):
        print(self.x,"/",self.y,sep="")



if __name__ == '__main__':
    tu, mau=map(int,input().split())
    a=PhanSo(tu, mau)
    a.rutgon()
    a.kq()






        
        
        
        

                