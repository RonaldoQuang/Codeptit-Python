from math import *
"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.
Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có. 
Input
Dòng đầu ghi số bộ test (không quá 20).
Mỗi test ghi số N (không quá 500 chữ số).
Output
Với mỗi bộ test, ghi ra kết quả tính được.
Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.  
Input
2
123410
123456789123456789
Output
24
131681894400
"""

from math import *
        
if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        sum=1
        for i in range (len(s)):
            if int(s[i])!=0:
                sum*=int(s[i])
        print(sum)
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
