"""
Một câu trong văn bản được hiểu là dãy ký tự (có cả khoảng trống) cho đến khi gặp dấu ngắt câu hoặc xuống dòng (tức là đôi khi người ta quên viết dấu ngắt câu nhưng cứ xuống dòng là sang một câu mới). 
Các dấu ngắt câu trong bài toán này bao gồm: dấu chấm (.), dấu chấm cảm (!), dấu chấm hỏi (?).
Hãy viết chương trình chuẩn hóa các câu trong dữ liệu vào với các yêu cầu sau:
Ký tự đầu mỗi câu viết hoa, các ký tự khác viết thường.
Các từ cách nhau đúng một khoảng trống.
Tự động điền thêm dấu chấm (.) nếu xuống dòng mà chưa có dấu ngắt câu.
Dấu ngắt câu phải viết sát ký tự cuối cùng của câu (không tính khoảng trống)
Input
Một văn bản không quá 100 dòng.
Output
Ghi ra các câu đã chuẩn hóa, mỗi câu 1 dòng.
Input
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.

co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin

muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep

moi    CAC BAN danG ky     thaM giA !
Output
Chuong trinh dao tao clc nganh cntt duoc thiet ke theo chuan quoc te.
Co 03 chuyen nganh la: cong  nghe phan mem, tri tue nhan tao va an toan thong tin.
Muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep.
Moi cac ban dang ky tham gia!
"""

from math import *

import sys, re

if __name__ == '__main__':
    text=sys.stdin.read().strip()
    text=re.sub(r'([^\.\!\?\n])\n', r'\1.\n',text)
    cau=re.findall(r'[^.?!\n]+[.?!]?',text)
    for i in cau:
        i=i.strip()
        if i:
            s=i.split()
            line=" ".join(s).lower()
            if line[len(line)-1:len(line)] not in ".?!":
                line+="."
            w=line.split()
            j=w[len(w)-1]
            if j=="." or j=="?" or j=="!":
                line=line[:len(line)-2]+line[len(line)-1]
            print(line.capitalize())
        