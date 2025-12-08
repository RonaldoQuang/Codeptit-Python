"""
Cho ma trận A kích thước N*M.
Hãy tìm số bước đi ít nhất để di chuyển từ vị trí A[1][1] đến vị trí A[N][M].
Biết rằng mỗi bước từ vị trí (i, j) ta có thể di chuyển theo một trong ba hướng:
Hướng xuống dưới với số ô di chuyển là hiệu hai giá trị A[i][j] và A[i+1][j]
Hướng sang phải với số ô di chuyển là hiệu hai giá trị A[i][j] và A[i][j+1]
Hướng chéo xuống với số ô di chuyển là hiệu của hai giá trị A[i][j] và A[i+1][j+1]
Input:
Dòng đầu tiên đưa vào số lượng test T.
Dòng tiếp theo đưa vào các bộ test. Mỗi bộ test gồm hai phần: phần thứ nhất là hai số N, M; phần thứ hai là các phần tử của ma trận A[][]; các số được viết cách nhau một vài khoảng trống.
T, N, M, A[i][j] thỏa mãn ràng buộc: 1≤T≤100; 1≤ N, M, A[i][j]≤103.
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Nếu không tìm được đường đi ghi ra -1
Input
1
3 3
2 1 2
1 2 4
1 3 2
Output
3
"""

from collections import deque

def Try(a, n, m):
    b=[[-1]*m for _ in range (n)]
    q=deque()
    b[0][0]=0
    q.append((0,0))
    while q:
        i, j=q.popleft()
        if i==n-1 and j==m-1:
            return b[i][j]
        if i<n-1:
            x=abs(a[i][j]-a[i+1][j])
            if i+x<n and b[i+x][j]==-1:
                b[i+x][j]=b[i][j]+1
                q.append((i+x,j))
        if j<m-1:
            x=abs(a[i][j]-a[i][j+1])
            if j+x<m and b[i][j+x]==-1:
                b[i][j+x]=b[i][j]+1
                q.append((i,j+x))
        if i<n-1 and j<m-1:
            x=abs(a[i][j]-a[i+1][j+1])
            if i+x<n and j+x<m and b[i+x][j+x]==-1:
                b[i+x][j+x]=b[i][j]+1
                q.append((i+x,j+x))
    return -1

if __name__=='__main__':
    for _ in range (int(input())):
        n, m=map(int,input().split())
        a=[]
        for _ in range (n):
            b=list(map(int,input().split()))
            a.append(b)
        print(Try(a,n,m))
        