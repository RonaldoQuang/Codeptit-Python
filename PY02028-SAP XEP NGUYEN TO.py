"""
Cho dãy số nguyên dương A[] có N phần tử. Các giá trị trong dãy không quá 1000.
Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.
Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.
Input
Dòng đầu ghi số N (1 < N < 100), dòng thứ 2 ghi N số của dãy A[].
Output
Ghi ra dãy số kết quả trên một dòng.
Input
8
4 6 3 8 7 2 5 9
Output
4 6 2 8 3 5 7 9
"""
from math import *

def nto(n):
    for i in range (2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return n>1
     
if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in a:
        if(nto(i)):
            b.append(i)
    b.sort()
    cnt=0
    for i in a:
        if nto(i):
            print(b[cnt],end=" ")
            cnt+=1
        else:
            print(i,end=" ")


    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
