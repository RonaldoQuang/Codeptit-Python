"""
Cho ma trận A kích thước N*M chỉ bao gồm các số nguyên dương.
Trong trường hợp N # M, hãy biến đổi ma trận A về dạng ma trận vuông theo quy tắc sau:
Nếu N > M, hãy loại bỏ các hàng có thứ tự lẻ trong ma trận ban đầu (thứ tự hàng tính từ 1) cho đến khi N = M. 
Ví dụ N = 6, M = 4 thì cần loại bỏ hàng thứ 1 và hàng thứ 3.
Nếu M > N, hãy loại bỏ các cột có thứ tự chẵn trong ma trận ban đầu (thứ tự cột tính từ 1). 
Ví dụ: N = 4, M = 6 thì cần loại bỏ cột thứ 2 và cột thứ 4.
In ra ma trận kết quả sau khi biến đổi.
Input
Dòng đầu ghi hai số N và M (1 < N,M < 50).
N dòng tiếp theo ghi các phần tử của ma trận A, các giá trị đều nguyên dương và không quá 1000.
Output
Ghi ra ma trận vuông sau khi biến đổi.
Input
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
Output
6 3 2 6
9 9 9 8
9 6 6 3
7 7 4 9

2 7 4 3
6 2 7 2
7 2 9 1
9 9 0 7
"""
from math import *
     
if __name__ == '__main__':
    n, m=map(int,input().split())
    a=[]
    for i in range (n):
        b=list(map(int,input().split()))
        a.append(b)
    cnt=0
    if n>m:
        for i in range (n):
            if i%2==1:
                for j in range (m):
                    print(a[i][j],end=" ")
                print()
            else:
                if cnt<n-m:
                    cnt+=1
                else:
                    for j in range (m):
                        print(a[i][j],end=" ")
                    print()
    else:
        for i in range (n):
            cnt=0
            for j in range (m):
                if j%2==0:
                    print(a[i][j],end=" ")
                else:
                    if cnt<m-n:
                        cnt+=1
                    else:
                        print(a[i][j],end=" ")
            print()



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
