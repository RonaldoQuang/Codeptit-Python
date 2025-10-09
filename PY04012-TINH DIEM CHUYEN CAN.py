"""
Lớp học phần môn XYZ của trường ABC có không quá 100 sinh viên. 
Danh sách sinh viên gồm các thông tin: mã sinh viên, họ tên, lớp. 
Môn học có 10 buổi. Dữ liệu điểm danh với mỗi sinh viên được cho bởi một xâu ki tự gồm 10 ký tự trong đó: x là có mặt, m là đến muộn, v là vắng.
Với điểm chuyên cần tối đa là 10. Giả sử mỗi buổi vắng bị trừ 2 điểm, mỗi buổi đến muộn bị trừ 1 điểm. 
Hãy tính điểm chuyên cần cho mỗi sinh viên (tất nhiên nếu tính ra điểm âm thì ghi vào bảng điểm vẫn là 0).
Nếu điểm bằng 0 thì in thêm ghi chú KDDK (tức là không đủ điều kiện dự thi hết môn).
Input
Dòng đầu ghi số n là số sinh viên. Mỗi sinh viên ghi trên 3 dòng lần lượt là mã sinh viên, họ tên, lớp.
Tiếp theo là n dòng ghi dữ liệu điểm danh. Mỗi dòng gồm mã sinh viên, sau đó là một khoảng trống rồi đến xâu ký tự điểm danh có đúng 10 chữ cái.
Output
Ghi ra danh sách điểm chuyên cần (theo đúng thứ tự ban đầu) gồm các thông tin:
Mã sinh viên
Họ và tên
Lớp
Điểm chuyên cần
Ghi chú (nếu có)
Mỗi thông tin cách nhau một khoảng trống.
Input
3
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
Output
B19DCCN999 Le Cong Minh D19CQAT02-B 0 KDDK
B19DCCN998 Tran Truong Giang D19CQAT02-B 4
B19DCCN997 Nguyen Tuan Anh D19CQCN04-B 6
"""

from math import *

class part:
    def __init__(self, ma, ten, lop):
        self.ma=ma
        self.ten=ten
        self.lop=lop

class sv:
    x=part
    def __init__(self, x, diem):
        self.x=x
        self.diem=diem
    def kq(self):
        if self.diem==0:
            print(self.x.ma,self.x.ten,self.x.lop,self.diem,"KDDK")
        else:
            print(self.x.ma,self.x.ten,self.x.lop,self.diem)
    
if __name__ == '__main__':
    b=[]
    mp={}
    mp1={}
    n=int(input())
    for _ in range (n):
        ma=input()
        ten=input()
        lop=input()
        mp[ma]=part(ma,ten,lop)
        b.append(ma)
    for _ in range (n):
        ma, tt=input().split()
        tong=10
        for i in tt:
            if i=='v':
                tong-=2
            elif i=='m':
                tong-=1
        if tong>0:
            mp1[ma]=sv(mp[ma],tong)
        else:
            mp1[ma]=sv(mp[ma],0)
    for i in b:
        mp1[i].kq()
    
    




        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                