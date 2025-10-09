"""
Có một cuốn sổ tay ghi ghép tên liên lạc và số điện thoại của bạn bè, người thân.
Do quá trình ghi chép, thứ tự được ghi lại dựa vào ngày ghi chép nên chưa được sắp xếp theo họ tên.
Để thuận lợi trong quá trình lưu trữ và sử dụng, người ta đã chuyển toàn bộ thông tin từ sổ tay lên lưu trữ trên điện thoại.
Dữ liệu trên điện thoại khi hiển thị đã được sắp xếp theo tên liên lạc. Lưu ý, nếu tên trùng nhau thì sắp xếp theo họ đệm.
Cho thông tin danh sách liên lạc được ghi chép như mẫu từ tập tin SOTAY.txt, hãy đưa ra dữ liệu hiển thị trên điện thoại vào tập tin DIENTHOAI.txt
Input: Lịch sử ghi chép theo ngày, mỗi ngày có thể ghi chép nhiều thông tin liên lạc. Họ tên tối đa 100 ký tự, số điện thoại có 10 chữ số.
Input
SOTAY.txt
Ngay 15/11/2021
Nguyen Van A
0914141581
Nguyen Van B
0921241515
Ngay 16/11/2021
Tran Van C
0935141141
Output
DIENTHOAI.txt
Nguyen Van A: 0914141581 15/11/2021
Nguyen Van B: 0921241515 15/11/2021
Tran Van C: 0935141141 16/11/2021
"""

from math import *

class thong_tin:
    def __init__(self, ngay, ten, sdt):
        self.ngay=ngay
        self.ten=ten+":"
        self.sdt=sdt
    def kq(self, f):
        print(self.ten,self.sdt,self.ngay,file=f)

def sx(ten):
    a=ten.split()
    return (a[-1],a[:-1])

if __name__ == '__main__':
    a=[]
    with open("SOTAY.txt", "r", encoding="utf-8") as f:
        lis=[]
        for line in f:
            if line.strip():
                lis.append(line.strip())
        i=0
        while i<len(lis):
            if "Ngay" in lis[i]:
                b=lis[i].split()
                ngay=b[1]
                i+=1
            else:
                ten=lis[i]
                sdt=lis[i+1]
                a.append(thong_tin(ngay,ten,sdt))
                i+=2
    a.sort(key=lambda x: sx(x.ten))
    with open("DIENTHOAI.txt", "w", encoding="utf-8") as f:
        for i in a:
            i.kq(f)
    

    
                