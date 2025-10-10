"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. 
Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.
Cho hai số nguyên dương L và R (10 < L < R < 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].
Input
Chỉ có 2 số L và R
Output
Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.
Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.
Input
15 20
Output
(15, 16, 17)
(15, 16, 19)
(15, 17, 19)
(16, 17, 19)
(17, 18, 19)
(17, 19, 20)
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

        

        

                
        


                
    
    
    
