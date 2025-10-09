from math import *
"""
Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.
Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:
Ba chữ số đầu ghép lại được một số nguyên tố
Ba chữ số cuối ghép lại được một số nguyên tố
Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?
Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi bộ test viết trên một dòng số N, ít nhất 4 chữ số và không quá 500 chữ số.
Output
Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
3
12743
7337
12345678901234
Output
YES
YES
NO
"""

from math import *

def nto(n):
    for i in range (2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return n>1
        
if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        n, m=0, 0
        for i in range (len(s)-3,len(s)):
            n=n*10+int(s[i])
        for i in range (3):
            m=m*10+int(s[i])
        if nto(n) and nto(m):
            print("YES")
        else:
            print("NO")
        
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
