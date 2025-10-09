"""
Trong lập trình cơ bản, một từ được hiểu là một dãy ký tự liên tiếp không chứa khoảng trống, dấu tab hoặc dấu xuống dòng.
Viết chương trình nhập hai dòng ký tự và hiển thị hợp và giao của hai tập từ tương ứng. 
Các từ trong tập từ không được phép trùng nhau, mỗi từ chỉ liệt kê một lần và theo đúng thứ tự từ điển. Các từ đều được chuyển hết về chữ viết thường. 
Input
Chỉ có 2 dòng, mỗi dòng có độ dài không quá 1000 ký tự.
Output
Dòng 1 ghi hợp của 2 tập từ theo thứ tự từ điển
Dòng 2 ghi giao của 2 tập từ theo thứ tự từ điển.
Input
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
Output
224225
c++ doi huong lap ngon ngu trinh tuong
lap trinh
"""
from math import *
     
if __name__ == '__main__':
    a=list(input().split())
    b=list(input().split())
    se=set()
    s=set()
    mp={}
    for i in a:
        i=i.lower()
        mp[i.lower()]=1
        se.add(i)
    for i in b:
        i=i.lower()
        if mp.get(i,0)==1:
            s.add(i)
        se.add(i)
        x, y=[], []
    for i in se:
        x.append(i)
    for i in s:
        y.append(i)
    x.sort()
    y.sort()
    for i in x:
        print(i,end=" ")
    print()
    for i in y:
        print(i,end=" ")


    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
