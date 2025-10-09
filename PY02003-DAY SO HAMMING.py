"""
Dãy số nguyên dương tăng dần trong đó ước số nguyên tố lớn nhất của các số trong dãy đều không vượt quá 5 được gọi là dãy số Hamming. 
Ví dụ 10 = 2x5 thuộc dãy Hamming còn 26 = 2x13 không thuộc dãy Hamming.
Số 1 được coi là số đầu tiên của dãy Hamming.
Cho số nguyên dương N.  Hãy xác định xem N có thuộc dãy Hamming hay không và nếu có thì thứ tự của N trong dãy Hamming là bao nhiêu.
Input:
Dòng đầu tiên ghi số bộ test (không quá 105).
Mỗi test ghi một số N (1 ≤ N ≤ 1018).
Output:
Nếu giá trị N thuộc dãy Hamming thì ghi ra thứ tự của N (tính từ 1).
Nếu không thì ghi ra “Not in sequence”
Input
11
1
2
6
7
8
9
10
11
12
13
14
Output
1
2
6
Not in sequence
7
8
9
Not in sequence
10
Not in sequence
Not in sequence
"""

from math import *

from collections import deque

se=set()
q=deque()
mp={}

def hamming():
    q.append(1)
    se.add(1)
    while q:
        x=q.popleft()
        for i in [2,3,5]:
            so=x*i
            if so<=10**18 and so not in se:
                se.add(so)
                q.append(so)
    a=sorted(list(se))
    for i in range (len(a)):
        mp[a[i]]=i+1

if __name__ == '__main__':
    hamming()
    for _ in range (int(input())):
        n=int(input())
        if n in mp:
            print(mp[n])
        else:
            print("Not in sequence")




        

        
            

            





        
    


    



        


    


        
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    







        
        
        
        

                