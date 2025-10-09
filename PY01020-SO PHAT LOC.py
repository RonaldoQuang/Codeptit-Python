"""
Một số kết thúc bởi hai chữ số 86 được gọi là số phát lộc. 
Cho một số nguyên dương không quá 500 chữ số, hãy kiểm tra số đó có phải số phát lộc hay không.
Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi số nguyên dương cần kiểm tra (không quá 500 chữ số)
Output
Ghi ra kết quả kiểm tra tương ứng (YES hoặc NO)
Input
3
1539786
1234789
8686
Output
YES
NO
YES
"""
if __name__ == '__main__':
    for _ in range (int(input())):
        s=input()
        a=""
        a+=s[len(s)-2:len(s)]
        if a=="86":
            print("YES")
        else:
            print("NO")