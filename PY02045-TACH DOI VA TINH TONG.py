"""
Cho một số nguyên dương không quá 200 chữ số. 
Mỗi bước tách số nguyên thành hai nửa: nửa đầu là n/2 chữ số đầu tiên, nửa sau là phần còn lại (trong đó n là số chữ số của số ban đầu, nếu n lẻ thì phép chia 2 sẽ tính phần nguyên). 
Sau đó thực hiện tính tổng của hai nửa này.
Lặp lại các bước trên cho đến khi kết quả chỉ còn là số có 1 chữ số.
Hãy thực hiện tính toán và in kết quả của từng bước.
Input
Chỉ có một số nguyên dương không quá 200 chữ số.
Output
Ghi ra kết quả từng bước, mỗi bước trên một dòng. Dừng lại khi kết quả chỉ còn 1 chữ số.
Output
Ghi ra số thứ tự của người trúng cử.
Hoặc nếu không có ai trúng cử thì ghi ra NONE
Input
123456
Output
579
84
12
3
"""
from math import *

if __name__ == '__main__':
    s=input()
    a=int(s[0:(len(s)//2)])
    b=int(s[(len(s)//2):])
    sum=a+b
    while sum>=10:
        print(sum)
        s=str(sum)
        a=int(s[0:(len(s)//2)])
        b=int(s[(len(s)//2):])
        sum=a+b
    print(sum)

                