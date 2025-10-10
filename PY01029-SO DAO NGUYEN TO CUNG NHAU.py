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

def dao(n):
    rev=0
    while n!=0:
        rev=rev*10+n%10
        n//=10
    return rev

if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        if gcd(n,dao(n))==1:
            print("YES")
        else:
            print("NO")
    

        

        

                
        


                
    
    
    
