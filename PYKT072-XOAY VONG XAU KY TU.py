"""
Cho N xâu S[1], S[2], …, S[N] có độ dài bằng nhau. 
Mỗi bước, với xâu T, bạn được phép xoay vòng 1 kí tự, tức lấy kí tự đầu tiên của T rồi chuyển xuống cuối. 
Ví dụ xâu “cool” sẽ chuyển thành “oolc”.
Bạn cần phải xoay N xâu sao cho tất cả chúng đều giống nhau. 
Hãy xác định số bước ít nhất để hoàn thành được công việc này?
Input:
Mỗi test bắt đầu bởi số nguyên N (1 ≤ N ≤ 50).
N dòng tiếp theo, mỗi dòng gồm xâu S[i] có độ dài không quá 50.
Output: 
Với mỗi test, in ra số bước ít nhất tìm được, nếu không thể biến đổi, hãy in ra “-1”.
Input
4
xzzwo
zwoxz
zzwox
xzzwo

3
aa
aa
ab
Output
5

-1
"""

from math import *

se=set()
a=[]
min1=1e9

def check():
    for i in a:
        if i not in se:
            return False
    return True

def tinh(a, b):
    cnt=0
    while a!=b:
        cnt+=1
        a=a[1:]+a[:1]
    return cnt

def tim():
    global min1
    for j in se:
        sum=0
        for i in a:
            sum+=tinh(i,j)
        min1=min(min1,sum)
                
if __name__ == '__main__':
    n=int(input())
    for i in range (n):
        s=input()
        a.append(s)
    s, i=a[0], 0
    se.add(a[0])
    while i<len(s):
        se.add(s[1:]+s[:1])
        i+=1
        s=s[1:]+s[:1]
    if check():
        tim()
        print(min1)
    else:
        print(-1)




