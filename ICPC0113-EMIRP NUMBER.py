"""
Một số nguyên dương K được gọi là Emirp Number nếu K là số nguyên tố, đảo các chữ số của K cũng là một số nguyên tố nhưng không phải chính nó (không đối xứng). 
Ví dụ số 11 không phải là số Emirp Number. 
Cho số tự nhiên N, nhiệm vụ của bạn là hãy liệt kê tất cả các số Emirp Number nhỏ hơn N.
Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤106;
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Chú ý: ghi theo các cặp số thỏa mãn từ nhỏ đến lớn, xem ví dụ để hiểu hơn về cách hiển thị kết quả. 
Input
2
40
100
Output
13  31
13  31  17  71  37 73 79  97
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
        n=int(input())
        for i in range (13,n):
            if prime[i] and str(i)!=str(i)[::-1] and prime[int(str(i)[::-1])] and i<int(str(i)[::-1]) and int(str(i)[::-1])<n:
                print(i,str(i)[::-1],end=" ")
        print()
        



    

    
                