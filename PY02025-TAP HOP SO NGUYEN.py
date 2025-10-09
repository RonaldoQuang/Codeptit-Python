"""
Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. 
Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].
Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.
Input
Dòng đầu ghi 2 số n và m (1 < n,m <100).
Dòng thứ 2 ghi n số của a[].
Dòng thứ 3 ghi m số của b[].
Các số đều dương và nhỏ hơn 1000.  
Output
Dòng đầu ghi tập giao của A và B
Dòng thứ 2 ghi tập A – B
Dòng thứ 3 ghi tập B - A
Input
5 6
1 2 3 4 5
3 4 5 6 7 8
Output
3 4 5
1 2
6 7 8
"""
from math import * 

if __name__ == '__main__': 
    n, m=map(int,input().split())
    s=list(map(int,input().split()))
    s1=list(map(int,input().split()))
    a, b=set(), set()
    for i in s:
        a.add(i)
    for i in s1:
        b.add(i)
    mp={}
    x, y, z=[], [], []
    for i in a:
        mp[i]=1
    for i in b:
        if mp.get(i,0)==1:
            mp[i]=2
        else:
            mp[i]=1
    for i in a:
        if mp[i]==1:
            x.append(i)
    for i in a:
        if mp[i]==2:
            y.append(i)
    for i in b:
        if mp[i]==1:
            z.append(i)
    x.sort()
    y.sort()
    z.sort()
    for i in y:
        print(i,end=" ")
    print()
    for i in x:
        print(i,end=" ")
    print()
    for i in z:
        print(i,end=" ")
