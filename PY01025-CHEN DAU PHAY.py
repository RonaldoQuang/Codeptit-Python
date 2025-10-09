from math import *
"""
Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). 
Ví dụ số 153920529 được viết lại thành 153,920,529.
Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.
Input
Chỉ có 1 số N
Output
Kết quả sau khi đã chèn dầu phẩy
Input
123456789
Output
123,456,789
"""

if __name__ == '__main__':
    s=list(input()[::-1])
    a=""
    for i in range (len(s)):
        a+=s[i]
        if i%3==2 and i!=len(s)-1:
            a+=","
    print(a[::-1])    
        


                
    
    
    
