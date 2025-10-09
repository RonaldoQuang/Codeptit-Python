"""
Cho đồ thị có hướng liên thông G có N đỉnh và M cạnh. 
Với một cặp đỉnh (u,v), đỉnh thắt của cặp đỉnh này được định nghĩa là một đỉnh mà tất cả đường đi từ u tới v đều đi qua nó.
Hãy đếm số đỉnh thắt với cặp đỉnh (u,v).
Input
Dòng đầu ghi số bộ test, không quá 100.
Mỗi bộ test bắt đầu với một dòng ghi 4 số N, M, u, v (0< N <= 100; 1 < M <=1000; 1 <= u,v <= N).
Tiếp theo là M dòng ghi các cạnh của đồ thị
Output
Với mỗi bộ test, ghi ra số đỉnh thắt của cặp đỉnh (u,v)
Input
2
5 7 1 3
1 2
2 4
2 5
3 1
3 2
4 3
5 4
4 5 1 4
1 2
1 3
2 3
2 4
3 4
Output
2
0
"""

from math import *

def dfs(i,v,ve,lis,vs):
    for j in a[i]:
        if j==v:
            ve.append(v)
            lis.append(ve[:])
            ve.pop()
            return
        elif vs[j]==0:
            vs[j]=1
            ve.append(j)
            dfs(j,v,ve,lis,vs)
            vs[j]=0
            ve.pop()

if __name__ == '__main__':
    for _ in range (int(input())):
        cnt=0
        mp={}
        vs=[0]*(101)
        ve=[]
        lis=[]
        a=[[] for _ in range (101)]
        n, m, u, v=map(int,input().split())
        for _ in range (m):
            x, y=map(int,input().split())
            a[x].append(y)
        ve.append(u)
        vs[u]=1
        dfs(u,v,ve,lis,vs)
        for i in range (len(lis)):
            for j in range (1,len(lis[i])-1):
                mp[lis[i][j]]=mp.get(lis[i][j],0)+1
        for i in range (1,n+1):
            if mp.get(i,0)==len(lis):
                cnt+=1
        print(cnt)