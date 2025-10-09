"""
Khai báo lớp Matrix mô tả ma trận các số nguyên với các thuộc tính là kích thước ma trận và mảng hai chiều lưu các phần tử.
Nhập ma trận a cấp n*m. Hãy viết chương trình tính tích của a với ma trận chuyển vị của a.    
Input: Dòng đầu tiên ghi số bộ test.
Với mỗi bộ test:
Dòng đầu tiên ghi hai số n và m là bậc của ma trân a;
n dòng tiếp theo, mỗi dòng ghi m  số của một dòng trong ma trận. n và m đều nguyên dương và nhỏ hơn 50. Các giá trị trong ma trận không vượt quá 100. 
Output: Với mỗi bộ test ghi ra ma trận tích tương ứng, mỗi số cách nhau đúng một khoảng trống. 
Input
1
2 2
1 2
3 4
Output
5 11
11 25
"""

from math import *
     
if __name__ == '__main__':
    for _ in range (int(input())):
        n, m=map(int,input().split())
        a=[]
        for i in range (n):
            a.append(list(map(int,input().split())))
        b=[]
        for i in range (m):
            c=[]
            for j in range (n):
                c.append(a[j][i])
            b.append(c)
        res=[]
        for i in range (n):
            c=[]
            for j in range (n):
                sum=0
                for k in range (m):
                    sum+=a[i][k]*b[k][j]
                c.append(sum)
            res.append(c)
        for i in range (n):
            for j in range (n):
                print(res[i][j],end=" ")
            print()




        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                