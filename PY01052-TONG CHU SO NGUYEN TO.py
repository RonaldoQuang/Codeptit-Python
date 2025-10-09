from math import *
"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.
Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số)
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
2
12341
22222222222222222222
Output
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
        sum=0
        for i in range (len(s)):
            sum+=int(s[i])
        if nto(sum):
            print("YES")
        else:
            print("NO")
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
