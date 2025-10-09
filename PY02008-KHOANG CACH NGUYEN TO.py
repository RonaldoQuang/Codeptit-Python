from math import *
"""
Cho hai số nguyên N và X.
Bắt đầu từ số X, hãy liệt kê N +1 số liên tiếp sao cho khoảng cách giữa số trước và số sau lần lượt là các số trong dãy N số nguyên tố đầu tiên.
Ví dụ N=5 và X=4. Vì 5 số nguyên tố đầu tiên là 2 3 5 7 11 nên ta có 6 số trong dãy cần liệt kê là: 4 6 9 14 21 32
Input
Chỉ có 1 dòng ghi 2 số N và X. (2 ≤ N ≤ 1000; 1 ≤ X ≤ 100)
Output
Ghi ra trên một dòng lần lượt N+1 số của dãy kết quả.
Input
5 4
Output
4 6 9 14 21 32
"""

from math import *

prime=[1]*(int(1e5)+1)
a=[]

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(10**5))):
        if prime[i]:
            for j in range (i*i,10**5+1,i):
                prime[j]=0
    for i in range (2,10**5+1):
        if prime[i]:
            a.append(i)
     
if __name__ == '__main__':
    sang()
    n, x=map(int,input().split())
    cnt=0
    while cnt<=n:
        print(x,end=" ")
        x=x+a[cnt]
        cnt+=1



    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
