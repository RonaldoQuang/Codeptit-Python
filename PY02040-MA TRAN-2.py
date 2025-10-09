from math import *
"""
Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.
Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).
Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy tổng giá trị các phần tử ở nửa trên trừ đi tổng giá trị các phần tử ở nửa dưới.
Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  
Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.
Hãy xác định độ chênh lệch và tính cân đối của ma trận.
Input
Dòng đầu ghi số N (2 < N < 50)
N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.
Dòng cuối ghi số K (0 < K <100)
Output
Dòng đầu ghi chữ YES hoặc NO
Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận
Input
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
Output
NO
11
"""

from math import *
     
if __name__ == '__main__':
    n=int(input())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    k=int(input())
    sum, sum1=0, 0
    for i in range (n-1):
        for j in range (n-i-1):
            sum+=a[i][j]
    for i in range (1,n):
        for j in range (n-i,n):
            sum1+=a[i][j]
    if abs(sum-sum1)<=k:
        print("YES")
    else:
        print("NO")
    print(abs(sum-sum1))

        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
