"""
Cho dãy số A[] có N phần tử là các số nguyên dương không quá 1000. 
Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A[] ta tạo được dãy B[] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A[].
Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B[] thỏa mãn:
Tổng các phần tử từ B[0] đến B[i] là một số nguyên tố
Tổng các phần tử từ B[i+1] đến B[m-1] cũng là một số nguyên tố.
Input
Dòng đầu ghi số N (1 < N < 500).
Dòng tiếp theo ghi N số của dãy A[]
Output
Ghi ra vị trí i đầu tiên tìm được.
Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND
Input
10
3 6 7 3 4 7 3 6 4 4
Output
0
"""
from math import *

def nto(n):
    for i in range (2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    else:
        return n>1

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    mp={}
    ok, sum2=0, 0
    for i in a:
        mp[i]=mp.get(i,0)+1
        if mp[i]==1:
            b.append(i)
    sum1=0
    for i in b:
        sum2+=i
    for i in range (len(b)):
        sum1+=b[i]
        sum2-=b[i]
        if nto(sum1) and nto(sum2):
            print(i)
            ok=1
            break
    if ok==0:
        print("NOT FOUND")


                