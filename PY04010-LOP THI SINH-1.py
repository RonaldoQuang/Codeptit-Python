"""
Viết chương trình khai báo lớp Thí Sinh gồm các thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3 và Tổng điểm.
Đọc thông tin 1 thí sinh từ bàn phím và in ra màn hình 3 thông tin: Họ tên, Ngày sinh, Tổng điểm.
Input
Gồm 5 dòng lần lượt, mỗi dòng ghi 1 thông tin: Họ tên, Ngày sinh, Điểm môn 1, Điểm môn 2, Điểm môn 3. 
Họ tên không quá 50 chữ cái, Ngày sinh viết đúng chuẩn dd/mm/yyyy. Các giá trị điểm là số thực (float).
Output
Ghi ra Họ tên, Ngày sinh và Tổng điểm. Mỗi thông tin cách nhau một khoảng trống. Điểm được ghi ra với 1 số sau dấu phẩy.
Input
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
Output
Nguyen Hoang Ha 11/10/2001 20.0
"""

from math import *

class Sinhvien:
    def __init__(self, ten, dob, d1, d2, d3):
        self.ten=ten
        self.dob=dob
        self.d1=d1
        self.d2=d2
        self.d3=d3
    def kq(self):
        print(self.ten,self.dob,"{:.1f}".format(self.d1+self.d2+self.d3))
        
     
if __name__ == '__main__':
    ten=input()
    dob=input()
    d1=float(input())
    d2=float(input())
    d3=float(input())
    a=Sinhvien(ten,dob,d1,d2,d3)
    a.kq()

            



    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                