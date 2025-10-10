"""
Cho hai số nguyên dương a và b. 
Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.
Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. 
Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.
Input
Dòng đầu ghi số bộ test. Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)
Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
Input
3
28 42
123 18
550 55
Output
YES
YES
NO
"""

from math import *

def nto(n):
    for i in range (2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return n>1

if __name__ == '__main__':
    for _ in range (int(input())):
        a, b=map(int,input().split())
        s=str(gcd(a,b))
        sum=0
        for i in s:
            sum+=int(i)
        if nto(sum):
            print("YES")
        else:
            print("NO")

                
    
    
    
