"""
Cho đồ thị vô hướng G có N đỉnh và M cạnh. 
Hãy tìm đỉnh u sao cho nếu loại bỏ đỉnh u ra khỏi đồ thị thì đồ thị bị chia cắt thành nhiều thành phần liên thông nhất.
Input
Dòng đầu ghi số bộ test, mỗi bộ test gồm:
Dòng đầu ghi số N là số đỉnh (1 < N < 100) và số M là số cạnh (M < N*(N-1)/2).
M dòng tiếp theo ghi các cạnh của đồ thị.
Output
Ghi ra thứ tự đỉnh (tính từ 1) thỏa mãn nếu loại bỏ đỉnh đó ra khỏi đồ thị thì sẽ chia cắt ra nhiều thành phần liên thông nhất.
Nếu có nhiều hơn 1 đỉnh thỏa mãn thì in ra thứ tự đỉnh nhỏ nhất.
Nếu không thể chia cắt được đồ thị thì ghi ra 0.
Input
2
5 5
1 2
1 3
2 3
3 4
3 5
5 7
1 2
1 3
2 3
2 5
3 4
3 5
4 5 
Output
3
0
"""

from collections import deque

def bfs(a, i, vs):
    q=deque()
    vs[i]=1
    q.append(i)
    while q:
        j=q.popleft()
        for x in a[j]:
            if vs[x]==0:
                vs[x]=1
                q.append(x)

if __name__=='__main__':
    for _ in range (int(input())):
        n, m=map(int,input().split())
        a=[[] for _ in range (n+1)]
        for _ in range (m):
            x, y=map(int,input().split())
            a[x].append(y)
            a[y].append(x)
        vs=[0]*(n+1)
        max, x=1, 0
        for i in range (1,n+1):
            vs[i]=1
            cnt=0
            for j in range (1,n+1):
                if vs[j]==0:
                    cnt+=1
                    bfs(a, j, vs)
            if cnt>max:
                max=cnt
                x=i
            vs=[0]*(n+1)  
        print(x)