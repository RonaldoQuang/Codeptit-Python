"""
Bộ ba số nguyên tố được gọi là Prime- Triplet nếu nó là bộ ba số nguyên tố dưới dạng (p, p +2, p + 6) hoặc (p, p + 4, p+6), trong đó p là một số nguyên tố. 
Ví dụ các bộ ba số (5, 7, 11) hoặc (7, 11, 13) đều là các Prime-Triplet. 
Cho số tự nhiên N, nhiệm vụ của bạn là đếm số các Prime-Triplet nhỏ hơn N.      
Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
2
15
25
Output
2
5
"""

from math import *

prime=[1]*(1000005)

def sang():
    prime[0]=0
    prime[1]=0
    for i in range (2,int(sqrt(1000005))+1):
        if prime[i]:
            for j in range (i*i,1000005,i):
                prime[j]=0
                
if __name__ == '__main__':
    sang()
    for _ in range(int(input())):
        cnt=0
        n=int(input())
        for i in range (2,n-5):
            if (prime[i] and prime[i+6]) and (prime[i+2] or prime[i+4]):
                cnt+=1
        print(cnt)
        



    

    
                