"""
Cho một xâu ký tự độ dài không quá 100 chỉ bao gồm các chữ cái in hoa. 
Người ta thực hiện mã hóa bằng cách đếm các ký tự cạnh nhau giống nhau và viết số lượng phía sau các chữ cái đó.
Ví dụ xâu AAECCCCGGGD thì được mã hóa thành A2E1C4G3D1
Với giả thiết không có ký tự nào xuất hiện nhiều hơn 9 lần liên tiếp.
Cho trước xâu kết quả mã hóa. Hãy khôi phục xâu ký tự ban đầu tương ứng.
Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi xâu mã hóa.
Output
Với mỗi test ghi ra xâu ký tự ban đầu.
Input
2
A8
A2E1C4G3D1
Output
AAAAAAAA
AAECCCCGGGD
"""
from math import *

if __name__ == '__main__':
    for _ in range (int(input())):
        w=input()
        s=list(w)
        for i in range (0,len(s),2):
            for j in range (int(s[i+1])):
                print(s[i],end="")
        print()
        


                
    
    
    
