"""
Con số duyên nợ là con số có chữ số đầu và chữ số cuối giống nhau.
Viết chương trình kiểm tra xem một số nguyên dương n ghi trong hệ thập phân có chữ số đầu và chữ số cuối giống nhau không?
Input
Gồm nhiều dòng, mỗi dòng chứa một số nguyên dương n ghi ở hệ thập phân.
Giới hạn:
1≤n≤10^100
Output
Ứng với mỗi số nguyên dương n, ghi ra trên một dòng là YES nếu số ntương ứng có chữ số đầu và chữ số cuối giống nhau, NO nếu ngược lại.
Input
2
12345
123451
Output
NO
YES
"""

from math import *

if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        if s[0]==s[len(s)-1]:
            print("YES")
        else:
            print("NO")
                
        


                
    
    
    
