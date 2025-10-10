"""
Chữ số 4 và chữ số 7được xem là các chữ số may mắn.
Cho số nguyên dương N có không quá 18 chữ số. 
Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.
Input
Chỉ có số N
Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
Input
40047
7747774
Output
NO
YES
"""

if __name__ == '__main__':
    s=list(input())
    cnt=0
    dem=0
    for i in range (len(s)):
        if s[i]=='4':
            cnt+=1
        elif s[i]=='7':
            dem+=1
    if cnt+dem==4 or cnt+dem==7:
        print("YES")
    else:
        print("NO")
