from math import *
"""
Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. 
Tại mỗi bước, giá trị A[i] được thay thế bằng abs(A[i] - A[i+1]), riêng A[4] = abs(A[4]-A[1]).
Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.
Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.
Input
Có 4 số của dãy A[], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.
Output
Với mỗi test, ghi ra số bước cần thực hiện.
Input
1 3 5 9
4 3 2 1
0 0 0 0
Output
6
4
"""

from math import *
     
if __name__ == '__main__':
    while True:
        s=input()
        if s=="0 0 0 0":
            break
        else:
            a=list(map(int,s.split()))
            cnt=0
            while a[0]!=a[1] or a[0]!=a[2] or a[0]!=a[3]:
                x=a[0]
                a[0]=abs(a[0]-a[1])
                a[1]=abs(a[1]-a[2])
                a[2]=abs(a[2]-a[3])
                a[3]=abs(a[3]-x)
                cnt+=1
            print(cnt)


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
