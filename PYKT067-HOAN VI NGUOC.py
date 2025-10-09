"""
Cho số nguyên dương N. 
Nhiệm vụ của bạn là hãy liệt kê tất cả các hoán vị của 1, 2, .., N theo thứ tự ngược. 
Ví dụ với N = 3 ta có kết quả: 321, 312, 231, 213, 132, 123.
Input:
Dòng đầu tiên đưa vào số lượng test T.
Những dòng kế tiếp đưa vào các bộ test. 
Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
T, n thỏa mãn ràng buộc: 1≤T, N≤10.
Output:
Với mỗi test, dòng đầu tiên đưa ra số lượng hoán vị. 
Dòng thứ hai liệt kê các hoán vị ngược tìm được.
Input
2
2
3
Output
2
21 12 
6
321 312 231 213 132 123
"""

from math import *

vs=[0]*(11)
a=[]

def kq(b):
    s=""
    for i in a:
        s+=str(i)
    b.append(s)

def Try(b, i, n):
    for j in range (n,0,-1):
        if vs[j]==0:
            a.append(j)
            vs[j]=1
            if i==n-1:
                kq(b)
            else:
                Try(b,i+1,n)
            a.pop()
            vs[j]=0
    
if __name__ == '__main__':
    for _ in range (int(input())):
        b=[]
        n=int(input())
        Try(b,0,n)
        print(len(b))
        for i in b:
            print(i,end=" ")
        print()






        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                