"""
Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. 
Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.
Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤107;
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
3
13
753
757
Output
No
No
Yes
"""

from math import *

def nto(n):
    for i in range (2,isqrt(n)+1):
      if n%i==0:
        return False
    return n>1

def tong(s):
    sum=0
    ok=1
    for i in s:
        if int(i)!=2 and int(i)!=3 and int(i)!=5 and int(i)!=7:
            ok=0
            break
        sum+=int(i)
    if nto(sum) and ok:
        return 1
    else:
        return 0
     
if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())
        if nto(n) and tong(str(n)):
            print("Yes")
        else:
            print("No")
        



    

    
                