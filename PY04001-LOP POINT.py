"""
Khai báo lớp Point (điểm trong không gian hai chiều) với hai thuộc tính là tọa độ x và tọa độ y (số thực).
nhập vào hai điểm p1, p2 và tính khoảng cách hai điểm đó. 
Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test có 4 số thực lần lượt là tọa độ của 2 điểm A và B, giá trị tuyệt đối không quá 1000.            
Ouput
Với mỗi bộ test, viết ra khoảng cách giữa 2 điểm với 4 chữ số phần thập phân. 
Input
2
0 0 0 5
0 199 5 6
Output
5.0000
193.0648
"""
from math import *

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def distance(self, a):
        d=sqrt((self.x - a.x) ** 2 + (self.y - a.y) ** 2)
        return "{:.4f}".format(d)

def Decimal(n):
    return float(n)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1




        
        
        
        

                