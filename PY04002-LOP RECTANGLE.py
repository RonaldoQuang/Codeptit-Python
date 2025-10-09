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

class Rectangle:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
    def area(self):
        return self.x*self.y
    def perimeter(self):
        return (self.x+self.y)*2
    def color(self):
        return self.z[0].upper()+self.z[1:].lower()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')




        
        
        
        

                