from math import *
"""
Cho dãy số A[] gồm có N phần tử. 
Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.
Input:
Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu.
Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).
Output: 
Với mỗi test in ra đáp án của bài toán trên một dòng. 
Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.
Nếu không tìm được đáp án, in ra “NO”.
Input
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
Output
4
NO
"""

from math import *
     
if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        b=list(map(int,input().split()))
        a={}
        for i in b:
            a[i]=a.get(i,0)+1
        sorted(a.items())
        ok=0
        MAX=-1e9
        for key, value in a.items():
            if value>MAX:
                MAX=value
                x=key
        if MAX>(n//2):
            print(x)
        else:
            print("NO")
    




    

        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
            
       
 
        
        
            
       
 
        
        
            
       
 
        
            
       
 
        
            
       
 
            
       
 

        

        

                
        


                
    
    
    
