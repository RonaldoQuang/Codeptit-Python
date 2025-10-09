"""
Cho dãy số A[] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.
In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.
Input
Dòng đầu ghi số n (1 < n ≤ 1000)
Các dòng tiếp theo ghi đủ n số của dãy A[], các số đều nguyên dương và không quá 1000.
Output
Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.
Input
10
1 2 3 4 5 6 7 7 9 6
Output
9 2 7 4 7 6 5 3 1 6
"""
from math import *
     
if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    if len(a)<n:
        while len(a)<n:
            k=map(int,input().split())
            for i in k:
                a.append(i)
    b=[]
    c=[]
    cnt, dem=0, 0
    for i in a:
        if i%2==0:
            b.append(i)
        else:
            c.append(i)
    b.sort()
    c.sort(reverse=True)
    for i in a:
        if i%2==0:
            print(b[cnt],end=" ")
            cnt+=1
        else:
            print(c[dem],end=" ")
            dem+=1

        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
