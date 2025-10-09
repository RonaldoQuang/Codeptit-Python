from math import *
"""
Cho hai số nguyên dương X1, X2. 
Ta chỉ được phép thay đổi chữ số p thành chữ số q và ngược lại chữ. 
Hãy đưa ra tổng nhỏ nhất và tổng lớn nhất các số X1 và X2 được tạo ra theo nguyên tắc kể trên.
Input:
Dòng đầu tiên đưa vào số lượng bộ test T.
Những dòng kế tiếp đưa vào T bộ test. 
Mỗi bộ test gồm 3 dòng: dòng đầu tiên ghi lại chữ số p và chữ số q; hai dòng kế tiếp ghi lại các số X1 và X2 theo thứ tự.
T, X1, X2 thỏa mãn ràng buộc: 1≤ T ≤100; 0≤ X1, X2 ≤101000.
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
1
5 6
645 
666
Output
1100 1312
"""

from math import *
     
if __name__ == '__main__':
    for _ in range(int(input())):
        p, q=input().split()
        str=input().split()
        if len(str)==1:
            x1=str[0]
            x2=input()
        else:
            x1, x2=str
        so1=int(x1.replace(p,q))+int(x2.replace(p,q))
        so2=int(x1.replace(q,p))+int(x2.replace(q,p))
        print(min(so1,so2),max(so1,so2))


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
