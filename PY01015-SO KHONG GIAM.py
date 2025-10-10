"""
Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.
Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.
Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi dòng ghi một số nguyên dương (không quá 500 chữ số).
Output
Ghi ra YES nếu đó là số không giảm. NO nếu ngược lại
Input
2
12345678888888888888889
65645645465754765876857685846
Output
YES
NO
"""

from math import *

def check(s):
    ok=1
    for i in range (len(s)-1):
        if int(s[i])>int(s[i+1]):
            ok=0
            break
    if ok==1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    for _ in range (int(input())):
        w=input()
        s=list(w)
        print(check(s))


                
    
    
    
