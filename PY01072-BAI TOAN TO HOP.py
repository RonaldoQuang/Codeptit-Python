from math import *
"""
Cho dãy số A[] có N phần tử. Hãy liệt kê tất cả các tổ hợp chập K của tập các phần tử khác nhau trong A[]. 
Các tổ hợp cần liệt kê theo thứ tự từ điển (tức là trong mỗi tổ hợp thì giá trị từ nhỏ đến lớn, và tổ hợp sau lớn hơn tổ hợp trước).
Input
Dòng đầu ghi hai số N và K.
Dòng thứ 2 ghi N số của mảng A[]. Các giá trị không quá 1000.
Dữ liệu đảm bảo số phần tử khác nhau của A[] không quá 20 và K không quá 10.
Output
Ghi ra lần lượt các tổ hợp tìm được, mỗi tổ hợp trên một dòng.
Input
8 3
2 4 4 3 5 1 3 4
Output
1 2 3
1 2 4
1 2 5
1 3 4
1 3 5
1 4 5
2 3 4
2 3 5
2 4 5
3 4 5
"""

from math import *

a=[]
c=[1e9]

def kq(k):
    for i in range (1,k+1):
        print(c[i],end=" ")
    print()

def Try(i, x, k):
    for j in range (x+1,len(a)):
        c.append(a[j])
        if i==k:
            kq(k)
        else:
            Try(i+1,j,k)
        c.pop()

     
if __name__ == '__main__':
    n, k=map(int,input().split())
    se=set()
    b=list(map(int,input().split()))
    for i in b:
        se.add(i)
    for x in sorted(se):
        a.append(x)
    for i in range (len(a)-k+1):
        c.append(a[i])
        Try(2,i,k)
        c.pop()
        
    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
