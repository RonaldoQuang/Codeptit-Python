"""
Bội số chung nhỏ nhất của hai số nguyên x và y (viết tắt LCM(x, y)) là số nguyên dương nhỏ nhất chia hết cho cả x và y.  
Cho hai số nguyên dương a và b (a ≤ b). Hãy đếm xem có bao nhiêu cặp số nguyên (x, y) sao cho
LCM(x,y) = a * (a+1) * …. * b
Dữ liệu vào:  Dòng đầu ghi số bộ test (không quá 10).  
Mỗi test ghi trên một dòng hai số a và b (a ≤ b ≤ 106)
Kết quả:
Với mỗi bộ test, ghi ra số lượng cặp (x, y)  thỏa mãn điều kiện đề bài. 
Vì kết quả có thể rất lớn nên hãy ghi kết quả theo modulo 109 + 7.
Input
2
2 3
5 5
Output
9
3
"""

from math import *

prime=[1]*(1000005)
mod=10**9+7

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(1000005))+1):
        if prime[i]:
            for j in range (i*i,1000005,i):
                prime[j]=0
            
def tinh(n, p):
    cnt=0
    while n:
        n//=p
        cnt+=n
    return cnt

if __name__ == '__main__':
    sang()
    x=[]
    for i in range (2,10**6+1):
        if prime[i]:
            x.append(i)
    for _ in range (int(input())):
        a, b=map(int,input().split())
        tich=1
        for i in x:
            if i>b:
                break
            e=tinh(b,i)-tinh(a-1,i)
            if e>0:
                tich=tich*(2*e+1)%mod
        print(tich)
    


        


        
    




