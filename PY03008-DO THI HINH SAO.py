"""
Một đơn đồ thị vô hướng được gọi là Hình Sao nếu có một đỉnh có thể nối đến tất cả các đỉnh còn lại, còn các đỉnh khác thì không có cạnh nối với nhau.
Cho mô tả một đơn đồ thị vô hướng N đỉnh với đúng N-1 cạnh. Hãy kiểm tra xem đồ thị đó có phải dạng Hình Sao hay không.
Dữ liệu vào
Dòng đầu tiên ghi số N là số đỉnh của đồ thị (1 ≤ N ≤ 105).
N-1 dòng tiếp theo, mỗi dòng ghi ra một cặp (u,v) là cạnh của đồ thị. Dữ liệu đảm bảo u ≠ v.
Kết quả
Ghi ra trên một dòng chữ “Yes” nếu đồ thị là Hình Sao; chữ “No” trong trường hợp ngược lại.
Input
5
1 2
1 3
1 4
1 5
Output
Yes
"""

from math import *
 
if __name__ == '__main__':
    n=int(input())
    x, y=map(int,input().split())
    cnt, cnt1=0, 0
    for _ in range (n-2):
        a, b=map(int,input().split())
        if a==x or b==x:
            cnt+=1
        elif a==y or b==y:
            cnt1+=1
    if cnt==n-2 or cnt1==n-2:
        print("Yes")
    else:
        print("No")


        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                