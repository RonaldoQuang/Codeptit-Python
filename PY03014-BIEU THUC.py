"""
Cho một biểu thức đúng, tức là các dấu ngoặc đơn đều đầy đủ mở và đóng, đảm bảo đúng thứ tự. 
Hãy viết chương trình đánh số các cặp dấu ngoặc theo thứ tự xuất hiện, tính từ 1.
Ví dụ với biểu thức                                              (a + (b *c) ) + (d/e)
ta có thứ tự của các cặp ‘(‘, ‘)’ là                         1  2  2  1  3  3
Input:
Dòng đầu tiên đưa vào số lượng bộ test T (không quá 100).
Những dòng kế tiếp đưa vào các bộ test. Mỗi bộ test là một biểu thức số học được đưa vào trên một dòng, độ dài không quá 106.
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
2
(a + (b *c) ) + (d/e)
( ( () ) ( () ) )
Output
1  2  2  1  3  3
1 2  3  3  2  4  5  5  4  1
"""

from math import *
    
if __name__ == '__main__':
    for _ in range (int(input())):
        a=[]
        s=input()
        cnt=1
        for i in range (len(s)):
            if s[i]=='(':
                print(cnt,end=" ")
                a.append(cnt)
                cnt+=1
            elif s[i]==')':
                print(a[len(a)-1],end=" ")
                a.pop()
        print()






        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                