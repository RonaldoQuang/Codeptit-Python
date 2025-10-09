from math import *
"""
Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000. 
Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1, không phải thì thay thế bằng số 0.
Input
Dòng đầu ghi 2 số N và M là kích thước ma trận (1 < N,M < 20)
N dòng tiếp theo mỗi dòng có M số mô tả ma trận
Output
Ghi ra ma trận kết quả
Input
3 3
1 2 3
4 5 6
7 8 9
Output
0 1 1
0 1 0
1 0 0
"""

from math import *

prime=[1]*(int(1e3)+1)

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(10**3))):
        if prime[i]:
            for j in range (i*i,10**3+1,i):
                prime[j]=0
     
if __name__ == '__main__':
    sang()
    n, m=map(int,input().split())
    a=[]
    for i in range (n):
        b=list(map(int,input().split()))
        a.append(b)
    for i in range (n):
        for j in range (m):
            if prime[a[i][j]]:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()
    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
