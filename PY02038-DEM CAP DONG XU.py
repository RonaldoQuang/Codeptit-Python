"""
Cho một lưới hình vuông kích thước N*N. Trên một số ô của lưới người ta đặt các đồng xu (ký hiệu bằng chữ cái C (coin)). 
Hãy đếm xem có thể lấy ra bao nhiêu cặp đồng xu ở cùng một hàng hoặc cùng một cột.
Input
Dòng đầu tiên ghi số N (1 ≤ N ≤ 100)
N dòng tiếp theo mô tả trạng thái của lưới, chữ cái C ứng với vị trí có đồng x, dấu chấm tương ứng với ô trống)
Output
Ghi ra số cặp đồng xu đếm được.
Input
4
CC..
C..C
.CC.
.CC.
Output
9
"""
from math import *
     
if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range (n):
        b=list(input())
        a.append(b)
    sum=0
    for i in range (n):
        cnt=0
        for j in range (n):
            if a[i][j]=='C':
                cnt+=1
        sum+=cnt*(cnt-1)//2
    for i in range (n):
        cnt=0
        for j in range (n):
            if a[j][i]=='C':
                cnt+=1
        sum+=cnt*(cnt-1)//2
    print(sum)

        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
