"""
Cuộc đua xe đạp bắt đầu từ 6h00 với độ dài quãng đường đua là 120 Km. 
Các cua-rơ sẽ được ghi nhận thành tích dựa trên thời điểm đến đích. 
Hãy xếp hạng theo thứ tự thành tích giảm dần.
Input
Dòng đầu ghi số cua-rơ tham gia cuộc đua.
Mỗi cua-rơ ghi trên 3 dòng:
Họ tên (xâu ký tự độ dài không quá 50)
Đơn vị (xâu ký tự độ dài không quá 20)
Thời điểm đến đích theo định dạng h:mm
Output
Ghi ra danh sách đã sắp xêp theo thành tích, tốt hơn xếp trước, kém hơn xếp sau.
Thông tin mỗi cua-rơ bao gồm:
Mã (là chữ cái đầu tiên của các từ trong tên đơn vị ghép với chữ cái đầu tiên các từ trong họ tên – xem ví dụ để hiểu rõ hơn)
Họ tên
Đơn vị
Vận tốc trung bình (đã làm tròn ra giá trị nguyên)
Input
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
Output
HBVNH Vu Ngoc Hoang Hoa Binh 51 Km/h
HNTVM Tran Vu Minh Ha Noi 48 Km/h
AGPDT Pham Dinh Tan An Giang 44 Km/h
"""

from math import *

class vdv:
    def __init__(self, ma, ten, tinh, v):
        self.ma=ma
        self.ten=ten
        self.tinh=tinh
        self.v=v
    def kq(self):
        print(self.ma,self.ten,self.tinh,round(self.v),"Km/h")
    
if __name__ == '__main__':
    a=[]
    for _ in range (int(input())):
        ten=input()
        tinh=input()
        kt=input()
        gio, phut=map(int,kt.split(":"))
        tg=(gio-6)+phut/60
        vt=float(120)/tg
        s=""
        for i in tinh.split():
            s+=i[0].upper()
        for i in ten.split():
            s+=i[0].upper()
        tt=vdv(s,ten,tinh,vt)
        a.append(tt)
    a.sort(key=lambda x:-x.v)
    for i in a:
        i.kq()
    






        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                