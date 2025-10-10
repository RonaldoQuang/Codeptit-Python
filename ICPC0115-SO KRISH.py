"""
Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó. Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. 
Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không? Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.
Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤108;
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
2
145
235
Output
YES
NO
"""

from math import *

def gt(n):
    if n==0 or n==1:
        return 1
    else:
        return n*gt(n-1)   
    
if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        m=n
        sum=0
        while n!=0:
            sum+=gt(n%10)
            n//=10
        if sum==m:
            print("Yes")
        else:
            print("No")
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
