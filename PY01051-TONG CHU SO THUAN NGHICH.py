"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.
Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.
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
        
if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        sum=0
        for i in range (len(s)):
            sum+=int(s[i])
        if sum>=10 and str(sum)==str(sum)[::-1]:
            print("YES")
        else:
            print("NO")
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
