"""
Trong toán học, cặp số (a,b) được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của a và b bằng 1.

Cho số nguyên dương N không quá 9 chữ số. 
Hãy kiểm tra xem N và số đảo của N có phải là một cặp số nguyên tố cùng nhau hay không.
Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi trên một dòng số nguyên dương N, không quá 9 chữ số.
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
2
123
997
Output
NO
YES
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

        

        

                
        


                
    
    
    
