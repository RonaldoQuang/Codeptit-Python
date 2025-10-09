from math import *
"""
Cho số nguyên dương N có không quá 500 chữ số.
Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.
Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận
Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.
Output
Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
3
12234323130097
3443354654654654461123
43543543434554659999
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
        n=0
        for i in range (len(s)-4,len(s)):
            n=n*10+int(s[i])
        if nto(n):
            print("YES")
        else:
            print("NO")
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
