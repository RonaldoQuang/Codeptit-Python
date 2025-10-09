"""
Cho ma trận A cỡ N*M chỉ bao gồm các số nguyên dương.
Một số được coi là thuận nghịch nếu có từ 2 chữ số trở lên và nếu viết theo thứ tự ngược lại giá trị vẫn không thay đổi so với giá trị ban đầu. 
Ví dụ: 99, 121, 1331
Hãy tìm số thuận nghịch lớn nhất trong ma trận và các vị trí có giá trị bằng số thuận nghịch lớn nhất đó.
Input
Dòng đầu ghi hai số N và M (1 < N, M < 50)
Tiếp theo là N dòng ghi các giá trị của ma trận, không có số nào lớn hơn 1000.
Output
Ghi ra giá trị của số nguyên tố lớn nhất. Sau đó lần lượt là các vị trí của số nguyên tố lớn nhất, mỗi vị trí trên một dòng (chỉ số hàng và cột tính từ 0). 
Các vị trí được liệt kê theo thứ tự từ trái qua phải, từ trên xuống dưới.
Nếu không tìm thấy số nguyên tố nào thì ghi ra NOT FOUND
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
77
Vi tri [0][2]
Vi tri [3][1]
Vi tri [5][2]
Vi tri [5][3]
"""
from math import *
     
if __name__ == '__main__':
    n, m=map(int,input().split())
    a=[]
    for i in range (n):
        b=list(map(int,input().split()))
        a.append(b)
    max=-1e9
    for i in range (n):
        for j in range (m):
            s=str(a[i][j])
            if len(s)>=2 and s==s[::-1] and a[i][j]>max:
                max=a[i][j]
    if max==-1e9:
        print("NOT FOUND")
    else:
        print(max)
        for i in range (n):
            for j in range (m):
                if a[i][j]==max:
                    print("Vi tri ","[",i,"]","[",j,"]",sep="")



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
