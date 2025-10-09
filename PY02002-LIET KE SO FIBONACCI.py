from math import *
"""
Dãy số Fibonacci được định nghĩa theo công thức như sau:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 với n>2
Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.
Input
Dòng đầu ghi số bộ test, không quá 10.
Mỗi bộ test viết trên một dòng hai số a và b.
Output
Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống
Input
1
1 10
Output
1 1 2 3 5 8 13 21 34 55
"""

from math import *
     
if __name__ == '__main__':
    for _ in range (int(input())):
        x, y=map(int,input().split())
        fi=[]
        cnt=2
        a, b=1, 1
        fi.append(a)
        fi.append(b)
        while cnt<=y:
            c=a+b
            a=b
            b=c
            cnt+=1
            fi.append(c)
        for i in range (x-1,y):
            print(fi[i],end=" ")
        print()



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
