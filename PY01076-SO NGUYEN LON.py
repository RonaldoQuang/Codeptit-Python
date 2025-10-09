from math import *
"""
Cho hai số a và b trong đó a≤10^12, b≤10^250. 
Nhiệm vụ của bạn là tìm ước số chung lớn nhất của hai số a, b.
Input
1
1221
1234567891011121314151617181920212223242526272829
Output
3
"""

from math import *
     
if __name__ == '__main__':
    for _ in range (int(input())):
        a=input()
        s=input()
        a=int(a)
        sum=0
        for i in range (len(s)):
            sum=sum*10+int(s[i])
            sum%=a
        print(gcd(a,sum))



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
