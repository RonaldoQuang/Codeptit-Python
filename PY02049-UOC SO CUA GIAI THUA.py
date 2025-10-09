"""
Cho số tự nhiên N và số nguyên tố P. 
Nhiệm vụ của bạn là tìm số x lớn nhất để N! chia hết cho px. Ví dụ với N=7, p=3 thì x=2 là số lớn nhất để 7! Chia hết cho 32. 
Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là cặp số N, p được viết cách nhau một vài khoảng trống.
T, N, p thỏa mãn ràng buộc : 1≤T≤100; 1≤N≤105; 2≤p≤5000;
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
3
32 7
76 2
3 5
Output
9
73
0
"""

from math import *

def mod(n, p):
    dem=0
    while n%p==0:
        dem+=1
        n//=p
    return dem
     
if __name__ == '__main__':
    for _ in range (int(input())):
        n, p=map(int,input().split())
        dem=0
        for i in range (p,n+1,p):
            dem+=mod(i,p)
        print(dem)
            



    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                