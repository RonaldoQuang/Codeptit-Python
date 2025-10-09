"""
Cho hai file văn bản DATA1.in và DATA2.in.
Một từ được định nghĩa là một dãy ký tự liên tiếp không có khoảng trống, dấu tab hay dấu xuống dòng. 
Tạm thời chưa xét đến các dấu câu trong bải toán này.
Hãy viết chương trình liệt kê  tập hợp các từ có mặt trong file DATA1.in nhưng không có trong file DATA2.in và ngược lại.
Các từ được chuyển hết về dạng chữ thường trước khi so sánh. Kết quả cần liệt kê theo thứ tự từ điển.
Input
Hai file văn bản DATA1.in và DATA2.in, có không quá 200 dòng.
Output
Dòng 1 ghi các từ khác nhau có mặt trong file DATA1.in nhưng không có trong file DATA2.in.
Dòng 2 ghi các từ khác nhau có mặt trong file DATA2.in nhưng không có trong file DATA1.in.
Input
DATA1.in
lap trinh huong doi tuong

ngon ngu lap trinh C++
DATA2.in
lap trinh co ban

lap trinh huong thanh phan
Output
c++ doi ngon ngu tuong
ban co phan thanh
"""

from math import *

import sys
    
if __name__ == '__main__':
    mp={}
    a=set()
    b=set()
    sys.stdin=open("DATA1.in","r")
    for i in sys.stdin.read().split():
        w=i.lower()
        mp[w]=1
        a.add(w)
    sys.stdin=open("DATA2.in","r")
    for i in sys.stdin.read().split():
        w=i.lower()
        if w in mp:
            if mp[w]==1:
                mp[w]=3 
        else:
            mp[w]=2
        b.add(w)
    for i in sorted(a):
        if mp[i]==1:
            print(i,end=" ")
    print()
    for i in sorted(b):
        if mp[i]==2:
            print(i,end=" ")
            


        
    
    
