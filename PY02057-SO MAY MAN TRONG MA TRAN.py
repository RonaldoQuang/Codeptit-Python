"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
Một số được coi là số may mắn nếu giá trị của nó đúng bằng khoảng cạch giữa số lớn nhất và số nhỏ nhất của ma trận.
Trong test ví dụ dưới đây, số lớn nhất là 77, số nhỏ nhất là 10. Giá trị may mắn là 67.
Hãy tìm xem trong ma trận có tồn tại số may mắn hay không. Nếu có thì ở các vị trí nào?
Ví dụ: 99, 121, 1331
Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.
Input
Dòng đầu ghi hai số N và M (1 < N, M < 50)
Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.
Output
Ghi ra giá trị bằng số may mắn nếu tìm được. Sau đó lần lượt là các vị trí tìm thấy, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). 
Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
Nếu không tìm thấy giá trị bằng số may mắn nào thì ghi ra NOT FOUND
Output
Ghi ra ma trận vuông sau khi biến đổi.
Input
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
Output
67
Vi tri [2][1]
Vi tri [3][3]
"""
from math import *
     
if __name__ == '__main__':
    n, m=map(int,input().split())
    a=[]
    for i in range (n):
        b=list(map(int,input().split()))
        a.append(b)
    max, min=-1e9, 1e9
    for i in range (n):
        for j in range (m):
            if a[i][j]<min:
                min=a[i][j]
            if a[i][j]>max:
                max=a[i][j]
    so=max-min
    ok=0
    for i in range (n):
        for j in range (m):
            if a[i][j]==so:
                ok=1
                break
    if ok==0:
        print("NOT FOUND")
    else:
        print(so)
        for i in range (n):
            for j in range (m):
                if a[i][j]==so:
                    ok=1
                    print("Vi tri ","[",i,"]","[",j,"]",sep="")



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
