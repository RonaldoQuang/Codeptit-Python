"""
Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. 
Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.
Input
Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.
Output
Ghi ra kết quả phân tích theo mẫu như trong ví dụ.
Input
3
28
100
1234
Output
1 * 2^2 * 7^1
1 * 2^2 * 5^2
1 * 2^1 * 617^1
"""
from math import *

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print("1 * ",end="")
        for i in range (2,int(sqrt(n)+1)):
            cnt=0
            while n%i==0:
                cnt+=1
                n//=i
            if cnt and n!=1:
                print(i,"^",cnt," * ",sep="",end="")
            elif cnt and n==1:
                print(i,"^",cnt,sep="",end="")
        if n!=1:
            print(n,"^1",sep="",end="")
        print()

        

        

                
        


                
    
    
    
