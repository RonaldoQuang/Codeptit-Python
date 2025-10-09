"""
Doanh nghiệp X cần tuyển một số nhân viên mới. 
Bài thi tuyển có hai phần: lý thuyết và thực hành. 
Sau khi tính điểm trung bình, các thí sinh sẽ được xếp thành 4 loại:
Nếu điểm dưới 5 -> TRUOT
Nếu điểm lớn hơn hoặc bằng 5 nhưng nhỏ hơn 8 -> CAN NHAC
Nếu điểm từ 8 đến 9.5 -> DAT
Nếu điểm lớn hơn 9.5 -> XUAT SAC
Điểm các bài thi lý thuyết và thực hành đều là số thực trong phạm vi từ 0 đến 10. 
Tuy nhiên, khi nhập điểm các bài thi, cán bộ tuyển dụng có thể quên mất dấu . phân cách phần nguyên và phần thập phân. 
Do đó nếu điểm ghi là 78 thì cần được hiểu là 7.8
Hãy sắp xếp danh sách thí sinh đã được xếp loại theo điểm trung bình giảm dần.
Input
Dòng đầu ghi số thí sinh. Mỗi thí sinh ghi trên 3 dòng lần lượt là:
Họ và tên (xâu ký tự độ dài không quá 100)
Điểm lý thuyết
Điểm thực hành
Mã thí sinh cần được tự động gán theo mẫu TS + số thứ tự (tính từ 01).
Output
Ghi ra danh sách thí sinh đã sắp xếp, mỗi thí sinh gồm 4 thông tin: mã thí sinh, họ tên, điểm trung bình (với 2 số phần thập phân) và xếp loại. 
Mỗi thông tin cách nhau một khoảng trống.
Input
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
Output
TS01 Nguyen Thai Binh 6.00 CAN NHAC
TS03 Phan Van Duc 5.60 CAN NHAC
TS02 Le Cong Hoa 4.25 TRUOT
"""

from math import *

class nv:
    def __init__(self, ma, ten, diem, tt):
        self.ma=ma
        self.ten=ten
        self.diem=diem
        self.tt=tt
    def kq(self):
        print(self.ma,self.ten,"{:.2f}".format(self.diem),self.tt)
 
if __name__ == '__main__':
    a=[]
    for t in range (1,int(input())+1):
        s=input()
        lt=float(input())
        if lt>10:
            lt=lt/10
        th=float(input())
        if th>10:
            th=th/10
        diem=(lt+th)/2
        if diem<5:
            b=nv("TS0"+str(t),s,diem,"TRUOT")
            a.append(b)
        elif diem>=5 and diem<8:
            b=nv("TS0"+str(t),s,diem,"CAN NHAC")
            a.append(b)
        elif diem>=8 and diem<=9.5:
            b=nv("TS0"+str(t),s,diem,"DAT")
            a.append(b)
        else:
            b=nv("TS0"+str(t),s,diem,"XUAT SAC")
            a.append(b)
    a.sort(key=lambda x:(-x.diem))
    for i in a:
        i.kq()

        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                