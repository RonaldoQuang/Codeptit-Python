from math import *
"""
Cho dãy số A có 10 phần tử là các số nguyên dương. 
Hãy đếm xem sẽ có bao nhiêu số khác nhau trong dãy nếu tất cả các phần tử đều được chia dư cho 42.
Input
Gồm 10 số nguyên dương, viết trên một hoặc nhiều dòng.
Output
Ghi ra các số khác nhau tìm được sau khi đã chia dư cho 42.
Input
39 40 41 42 43 44 82
83 84 85
Output
6
"""

from math import *
     
if __name__ == '__main__':
    dd = [0] * 42
    cnt, res = 10, 0
    while cnt != 0:
        a = [int(i) for i in input().split()]
        cnt -= len(a)
        for i in a:
            if dd[i % 42] == 0:
                dd[i % 42] = 1
                res += 1
    print(res)



    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
