"""
Một số được gọi là xen kẽ nếu thỏa mãn cả ba tính chất sau:
Số chữ số là số lẻ
Chữ số đầu tiên khác chữ số thứ hai.
Các số ở vị trí đầu tiên, vị trí thứ 3, vị trí thứ 5…  và vị trí cuối cùng có giá trị bằng nhau
Viết chương trình kiểm tra một số có phải xen kẽ hay không.
Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi bộ test viết trên một dòng số cần kiểm tra, không quá 500 chữ số.
Output
Với mỗi bộ test viết ra YES hoặc NO tùy thuộc kết quả kiểm tra 
Input
2
2324272921262
13141516
Output
YES
NO
"""

from math import *
        
if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        ok=1
        for i in range (2,len(s),2):
            if s[i]!=s[0]:
                ok=0
                break
        if len(s)%2==1 and s[0]!=s[1] and ok==1:
            print("YES")
        else:
            print("NO")
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
