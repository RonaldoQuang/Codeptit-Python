"""
Cho dãy số A[] có N phần tử. Với mỗi vị trí thứ i trong dãy, hãy tính độ dài của đoạn liên tiếp tính từ i trở về phía trước mà các giá trị đều nhỏ hơn hoặc bằng A[i].
Input: Dòng đầu ghi số bộ test (không quá 10). Mỗi test có 2 dòng.
Dòng đầu tiên gồm 1 số nguyên N (1 ≤ N ≤ 105).
Dòng tiếp theo gồm N số nguyên A1, A2, …, AN (1 ≤ A[i] ≤ 106).
Output
Với mỗi bộ test, in ra dãy kết quả trên một dòng.
Input
1
7
100 80 60 70 60 75 85
Output
1 1 1 2 1 4 6
"""
from math import * 

if __name__ == '__main__':
    for _ in range (int(input())):
        n=int(input())
        a=[0]+list(map(int,input().split()))
        st=[]
        for i in range (1,n+1):
            while len(st)>0 and a[i]>=a[st[len(st)-1]]:
                st.pop()
            if len(st)==0:
                print(i,end=" ")
            else:
                print(i-st[len(st)-1],end=" ")
            st.append(i)
        print()