from math import *
"""
Cho số nguyên dương N. Mỗi bước thực hiện các phép biến đổi N theo quy tắc sau
Nếu N chẵn thì N = N/2
Nếu N lẻ thì N = N*3 + 1
Hãy đếm xem có bao nhiêu giá trị xuất hiện cho đến khi N = 1. Tất nhiên nếu ban đầu N = 1 thì chỉ có một giá trị duy nhất.
Ví dụ: N = 3 thì sẽ có 8 giá trị xuất hiện lần lượt là: 3, 10, 5, 16, 8, 4, 2, 1
Input
Có nhiều test, mỗi test ghi trên một dòng số nguyên dương N  không quá 100.
Input kết thúc khi N = 0.
Output
Với mỗi test, ghi ra kết quả tính được trên một dòng.
Input
1
2
3
0
Output
1
2
8
"""

from math import *
     
if __name__ == '__main__':
    while True:
        n=int(input())
        if n==0:
            break
        else:
            se=set()
            se.add(n)
            while n!=1:
                if n%2==0:
                    n//=2
                else:
                    n=n*3+1
                se.add(n)
            print(len(se))

    



    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
