"""
Mới đây, Sở Giao thông Vận tải TP Hà Nội đã thông tin chính thức về Đề án "Thu phí phương tiện cơ giới đường bộ đi vào một số khu vực nhằm giảm ùn tắc giao thông" để trình UBND thành phố Hà Nội.
Theo Sở GTVT, phí giảm ùn tắc giao thông là một loại phí mà người điều khiển phương tiện giao thông cơ giới đường bộ (ô tô) phải trả khi đi vào khu vực có nguy cơ ùn tắc giao thông. 
Nhằm giảm lưu lượng xe ô tô đi vào góp phần giảm ùn tắc giao thông.
Dữ liệu xe ra vào thành phố được lưu trữ đầy đủ trên hệ thống. Thông tin về phương tiện bao gồm.
Loại xe, biển số, số ghế ngồi.
Mức giá áp dụng cho các phương tiện được thực hiện theo bảng giá sau:
Loại xe         Số ghế          Đơn giá
Xe_con            5              10000
Xe_con            7              15000
Xe_tai            2              20000
Xe_khach          29             50000
Xe_khach          45             70000
Chiều di chuyển có hai hướng là Vào và Ra thành phố (IN và OUT). 
Khi xe đi vào thành phố thì phải trả phí, xe đi ra khỏi thành phố sẽ không phải trả phí.
Để thống kê lượng phương tiện ra vào thành phố thuận lợi cho quá trình vận hành và khai thác. 
Bạn hãy viết chương trình thực hiện thống kê theo ngày tổng số tiền thu được.
Input:
Dòng đầu tiên cho số N là tổng số bản ghi.
N dòng tiếp theo mỗi dòng ghi lại thông tin về lượt di chuyển của xe lần lượt là biển số, loại xe, số ghế ngồi, hướng di chuyển, ngày di chuyển.
Output:
In ra kết quả thống kê theo ngày, thứ tự ngày theo thứ tự xuất hiện trong input.
Input
5
30F-123.15 Xe_con 5 OUT 06/11/2021
30F-123.15 Xe_con 5 IN 06/11/2021
30H-123.15 Xe_con 7 IN 06/11/2021
29H-222.68 Xe_tai 2 IN 07/11/2021
30G-511.15 Xe_con 5 IN 07/11/2021
Output
06/11/2021: 25000
07/11/2021: 30000
"""

from math import *
 
if __name__ == '__main__':
    n=int(input())
    mp={}
    dic={
        "xe_con5": 10000,
        "xe_con7": 15000,
        "xe_tai2": 20000,
        "xe_khach29": 50000,
        "xe_khach45": 70000,
    }
    for _ in range (n):
        a=list(input().split())
        if a[3].lower()=="in":
            if mp.get(a[4],0)==0:
                mp[a[4]]=dic[a[1].lower()+a[2]]
            else:
                mp[a[4]]+=dic[a[1].lower()+a[2]]
    for x, y in mp.items():
        print(x,": ",y,sep="")



        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                