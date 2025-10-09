from math import *
"""
Cho dãy số nguyên dương A[] có N phần tử. 
Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.
Các số được liệt kê theo thứ tự xuất hiện.
Input
Dòng đầu ghi số N (không quá 500).
Dòng sau ghi N số của dãy (không quá 6 chữ số).
Output
Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.
Input
10
2 4 7 5 7 8 9 3 7 2
Output
2 2
7 3
5 1
3 1
"""

from math import *

prime=[1]*(int(1e6)+1)

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(10**6))):
        if prime[i]:
            for j in range (i*i,10**6+1,i):
                prime[j]=0
     
if __name__ == '__main__':
    sang()
    n=int(input())
    b=list(map(int,input().split()))
    a={}
    for i in b:
        a[i]=a.get(i,0)+1
    for key, value in a.items():
        if prime[key]:
            print(key,value)
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
