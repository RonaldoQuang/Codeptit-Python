from math import *
"""
Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. 
Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.
Input
Dòng đầu ghi số N (1 <= N <= 30000).
Dòng tiếp theo ghi N số của dãy A (1 <= A[i] <= 30000).
Output
Ghi ra số nhỏ nhất còn thiếu nếu có.
(khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).
Input
3
1 2 4
Output
3
"""

from math import *
     
if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    min=1
    a.sort()
    for i in range (n):
        if a[i]==min:
            min=a[i]+1
    print(min)


    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
