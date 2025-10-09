"""
Cho một số nguyên không âm N được biểu diễn như một xâu ký tự. 
Hãy sử dụng nhiều nhất một phép đổi chỗ các chữ số trong N sao cho ta nhận được số lớn nhất nhỏ hơn N. 
Phép biến đổi có số 0 cho số đầu tiên sẽ không được chấp nhận. 
Ví dụ số N=354 thì số lớn nhất nhỏ hơn N được tạo ra là 345. 
Số 100 sẽ không có phép biến đổi vì số 010 có số 0 đứng đầu.
Input:
Dòng đầu tiên đưa vào số lượng test T (T≤100).
Những dòng kế tiếp đưa vào các test. Mỗi bộ test là một xâu ký tự bao gồm các ký tự số. Độ dài tối đa là 1000.
Output:
Với mỗi test in ra số nguyên lớn nhất tìm được trên một dòng. Nếu không tồn tại đáp án, in ra -1.
Input
4
354
999
100
11101
Output
345
-1
-1
11011
"""

from math import *

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=list(input().strip())
        n=-10**9
        m=0
        min_idx = -10**5
        for i in range(len(s)-1, 0, -1):
            n=-10**9
            for j in range(i-1,-1,-1):
                if s[j]>s[i]:
                    n=j
                    break
            if n>min_idx:
                min_idx=n
                m=i
            if n==min_idx:
                if s[i]==s[m]:
                    min_idx=n
                    m=i
        if min_idx >= 0:
            s[min_idx], s[m] = s[m], s[min_idx]
            if s[0]=='0':
                print(-1)
            else:
                print("".join(s))
        else:
            print(-1)
        