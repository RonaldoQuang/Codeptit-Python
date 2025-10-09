from math import *
"""
Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.
Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
3
1234567
22334455667
23400300489898989
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
        cnt=0
        for i in range (len(s)):
            if int(s[i])==2 or int(s[i])==3 or int(s[i])==5 or int(s[i])==7:
                cnt+=1
        if cnt>len(s)-cnt and nto(len(s)):
            print("YES")
        else:
            print("NO")
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
