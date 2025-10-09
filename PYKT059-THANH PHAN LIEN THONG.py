"""
Cho đồ thị vô hướng G có N đỉnh, M cạnh. 
Hãy liệt kê các đỉnh không cùng thành phần liên thông với một đỉnh cho trước.
Input
Dòng đầu ghi 3 số N, M và X (0 < N < 300; 1 ≤ M ≤ N*(N-1)/2), 0 < X < N).
Tiếp theo là M dòng, mỗi dòng ghi một cạnh của đồ thị. Các cạnh được liệt kê với thứ tự bất kỳ.
Output
Ghi ra các đỉnh không liên thông với đỉnh X theo thứ tự tăng dần, mỗi dòng ghi một đỉnh. 
Nếu không có đỉnh nào thì ghi ra số 0.
Input
6 4 2
1 3
2 3
1 2
4 5
Output
4
5
6
"""

from math import *

vs=[0]*(301)
a=[[] for _ in range (301)]

def dfs(i):
    vs[i]=1
    for j in range (len(a[i])):
        if vs[a[i][j]]==0:
            dfs(a[i][j]) 
 
if __name__ == '__main__':
    mp={}
    n, k, s=map(int,input().split())
    for i in range (k):
        x, y=map(int,input().split())
        a[x].append(y)
        a[y].append(x)
    vs[s]=1
    dfs(s)
    b=[]
    for i in range (1,n+1):
        if vs[i]==0:
            b.append(i)
    b.sort()
    if len(b)==0:
        print(0)
    else:
        for i in b:
            print(i)
        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                