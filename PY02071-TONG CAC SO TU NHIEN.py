"""
Cho số nguyên dương N. Nhiệm vụ của bạn là hãy liệt kê tất cả các cách biểu diễn N thành tổng các số tự nhiên nhỏ hơn hoặc bằng N. Phép hoán vị của một cách được xem là giống nhau.
Ví dụ với N = 5 ta có kết quả là: (5), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1) .
Input:
Dòng đầu tiên đưa vào số lượng test T.
Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một số tự nhiên N được viết trên một dòng.
T, n thỏa mãn ràng buộc: 1≤T, N≤10.
Output:
Dòng đầu tiên là số lượng cách phân tích thỏa mãn.
Dòng tiếp theo liệt kê đáp án theo mẫu ví dụ đã cho.
Input
2
4
5
Output
5
(4) (3 1) (2 2) (2 1 1) (1 1 1 1)
7
(5) (4 1) (3 2) (3 1 1) (2 2 1) (2 1 1 1) (1 1 1 1 1)
"""
from math import *

a=[]

def kq(x):
    s=""
    s+="("
    for i in range (len(a)):
        if i<len(a)-1:
            s+=str(a[i])+" "
        else:
            s+=str(a[i])+")"
    x.append(s)

def Try(x,i,sum):
    for j in range (i,0,-1):
        sum+=j
        a.append(j)
        if sum==n:
            kq(x)
        elif sum<n:
            Try(x,j,sum)
        sum-=j
        a.pop()
     
if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        sum=0
        x=[]
        Try(x,n,sum)
        print(len(x))
        for i in range (len(x)):
            print(x[i],end=" ")
        print()



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
