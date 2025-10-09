"""
Cho danh sách các email trong file CONTACT.in, hãy loại bỏ các email trùng nhau và sắp xếp các email còn lại theo thứ tự từ điển.
Chú ý: địa chỉ email thì không phân biệt chữ hoa, chữ thường. Kết quả in ra cần đưa tất cả về dạng chữ thường.
Input - file văn bản CONTACT.in
Gồm không quá 300 dòng, mỗi dòng ghi một địa chỉ email.
Độ dài mỗi email không quá 100 ký tự.
Chú ý: Dữ liệu vào không có số dòng nên cần đọc đến hết file.
Output
Ghi ra danh sách các email đã loại bỏ trùng nhau và sắp xếp theo thứ tự từ điển.
Input
nguyenmanhson@gmail.com
sonnm@ptit.edu.vn
NGUYENMANHSON@gmail.com
SonNM@ptit.edu.vn
NguyenManhSon@GMAIL.com
Output
nguyenmanhson@gmail.com
sonnm@ptit.edu.vn
"""

from math import *

import sys
    
if __name__ == '__main__':
    sys.stdin=open("CONTACT.in")
    a=[]
    se=set()
    s=sys.stdin.read().split()
    for i in s:
        se.add(i.lower())
    for i in se:
        a.append(i)
    a.sort()
    for i in a:
        print(i)
