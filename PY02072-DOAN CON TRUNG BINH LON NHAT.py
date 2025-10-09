"""
Cho dãy số A[] có N phần tử, N không quá 105, các số trong dãy đều nguyên dương và không quá 9 chữ số. 
Hãy tính độ dài của dãy con liên tiếp có trung bình cộng lớn nhất trong dãy.
Trong trường hợp có nhiều dãy con liên tiếp đều có trung bình cộng lớn nhất thì dãy nào dài hơn sẽ được chọn.
Input
Dòng đầu ghi số N.
Dòng thứ 2 ghi N số của dãy A[]
Output
Ghi ra độ dài dãy con liên tiếp có trung bình cộng lớn nhất tìm được.
Input
5
5 1 6 7 2
Output
1
"""
from math import *

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    MAX, i=0, 0
    while i<n:
        if a[i]==m:
            cnt=0
            while i<n and a[i]==m:
                i+=1
                cnt+=1
            MAX=max(MAX,cnt)
        else:
            i+=1
    print(MAX)


                