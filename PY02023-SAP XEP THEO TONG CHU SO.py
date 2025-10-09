from math import *
"""
Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.
Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.
Input
Dòng đầu ghi số bộ test (không quá 10)
Mỗi bộ test gồm 2 dòng:
Dòng đầu là số N (N < 100)
Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.
Output
Với mỗi bộ test, ghi trên một dòng dãy số kết quả.
Input
1
8
143 43 22 99 7 9 1111 10000000
Output
10000000 22 1111 7 43 143 9 99
"""

from math import *

def tong(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
     
if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort(key=lambda x:(tong(x),x))
        for i in a:
            print(i,end=" ")
        print()
        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
