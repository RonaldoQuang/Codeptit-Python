"""
Cho dãy số A[] có N phần tử là các số nguyên dương.
Mỗi bước bạn được phép thay đổi 1 giá trị trong dãy bằng cách tăng lên 1 hoặc giảm đi 1.
Hãy tính xem cần ít nhất bao nhiêu bước để biến đổi dãy về giá trị bằng nhau, với điều kiện giá trị của dãy bằng nhau đó phải là một trong các giá trị ban đầu của dãy.
Input
Dòng đầu ghi số N là số phần tử của dãy (không quá 200).
Dòng thứ 2 ghi N phần tử của dãy, các phần tử đều nguyên dương và không quá 10000.
Output
Ghi ra tổng số bước ít nhất tìm được và giá trị bằng nhau được chọn.
Trong trường hợp có nhiều giá trị có thể chọn thì chọn số đầu tiên theo thứ tự xuất hiện trong dãy ban đầu.
Input
8
13 5 8 7 9 15 26 34
Output
59 13
"""
from math import *
     
if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    x=[]
    for i in range (n):
        sum=0
        for j in range (n):
            sum+=abs(a[i]-a[j])
        x.append(sum)
    min=1e18
    for i in range (n):
        if x[i]<min:
            min=x[i]
            so=a[i]
    print(min,so)


        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
