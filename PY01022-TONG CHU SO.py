"""
Cho một số nguyên (có thể âm) không quá 100.000 chữ số. 
Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó. 
Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.
Input
Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)
Output
Ghi ra số bước cần thực hiện.
Input
10
919
6
Output
1
3
1
"""
from math import *

def tong(s):
    sum=0
    for i in s:
        sum+=ord(i)-ord('0')
    return str(sum)
     
if __name__ == '__main__':
    s=input()
    cnt=0
    while len(s)>1:
        s=tong(s)
        cnt+=1
    print(cnt)

    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
