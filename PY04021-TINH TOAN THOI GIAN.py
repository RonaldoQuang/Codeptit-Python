"""
Quán Game mùa này vắng khách nên chủ quán quyết định tính tiền chi tiết đến từng phút. 
Dựa trên dữ liệu giờ vào và giờ ra, hãy tính thời gian chơi game của các Game thủ nhé.
Input
Dòng đầu của dữ liệu vào ghi số lượng game thủ trong ngày (không quá 20).
Thông tin về một game thủ đến chơi game được ghi lại trên 4 dòng lần lượt là:
Mã người chơi (xâu ký tự độ dài không quá 10, không có khoảng trống)
Tên người chơi (xâu ký tự độ dài không quá 100, có thể có khoảng trống).
Giờ vào (định dạng hh:mm)
Giờ ra (định dạng hh:mm)
Ouput
Ghi ra danh sách game thủ đã được sắp xếp theo thời gian chơi game giảm dần.
Input
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
Output
06T  Hoang Van Nam 2 gio 30 phut
01T  Nguyen Van An 1 gio 30 phut
02I  Tran Hoa Binh 0 gio 55 phut
"""

from math import *

class kh:
    def __init__(self, ma, ten, gio, phut):
        self.ma=ma
        self.ten=ten
        self.gio=gio
        self.phut=phut
    def kq(self):
        print(self.ma,self.ten,self.gio,"gio",self.phut,"phut")
 
if __name__ == '__main__':
    a=[]
    for _ in range (int(input())):
        s=input()
        ten=input()
        bd=input()
        kt=input()
        x=(int(kt[0:2])-int(bd[0:2]))*60+int(kt[3:5])-int(bd[3:5])
        gio=x//60
        phut=x%60
        b=kh(s,ten,gio,phut)
        a.append(b)
    a.sort(key=lambda x:(-x.gio,-x.phut))
    for i in a:
        i.kq()

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                