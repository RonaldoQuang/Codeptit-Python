"""
Khu dân cư ABC tiến hành bầu tổ trưởng dân phố. 
Có M ứng viên và N cử tri. 
Người dân trong khu dân cư đã chán ngấy với việc các ứng viên vận động tranh cử, câu kéo phiếu bầu trong các nhiệm kỳ trước nên họ quyết định đặt ra quy định mới như sau:
Các ứng viên được đánh số từ 1 tới M. Mỗi cử tri sẽ viết ra đúng 1 số thứ tự ứng viên mình muốn chọn và bỏ vào hòm phiếu.
Người trúng cử là người có số phiếu bầu nhiều thứ hai
Nếu không có người đứng thứ hai thì kết quả bầu cử sẽ bị hủy bỏ
Nếu có nhiều hơn 1 người cùng có số phiếu nhiều thứ hai thì người nào có số thứ tự nhỏ nhất sẽ được chọn.
Viết chương trình xác định người trúng cử.
Input
Dòng đầu ghi hai số N và M (1 < M < 10, 5 < N < 500).
Dòng thứ 2 ghi N giá trị trong các phiếu bầu. Các giá trị đảm bảo hợp lệ (tức là từ 1 đến M).
Output
Ghi ra số thứ tự của người trúng cử.
Hoặc nếu không có ai trúng cử thì ghi ra NONE
Input
10 4
2 3 1 2 3 4 1 2 3 2

8 4
1 2 3 4 4 3 2 1
Output
3

NONE
"""
from math import *

if __name__ == '__main__':
    n, m=map(int,input().split())
    a=list(map(int,input().split()))
    mp={}
    for i in a:
        mp[i]=mp.get(i,0)+1
    max, max1=-1e9, -1e9
    for key, value in mp.items():
        if value>max:
            max=value
    for key, value in mp.items():
        if value>max1 and value<max:
            max1=value
            x=key
    if max1==-1e9:
        print("NONE")
    else:
        print(x)
        