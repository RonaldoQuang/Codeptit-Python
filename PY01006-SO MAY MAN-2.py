"""
Một số được xem là số may mắn nếu chỉ có các chữ số 4 và 7. 
Cho số nguyên dương N không quá 200 chữ số. Hãy kiểm tra xem N có phải số may mắn hay không.
Input
Dòng đầu ghi số bộ test (không quá 10).
Mỗi test ghi số nguyên dương N không quá 200 chữ số.
Output
Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
Input
3
4477
444487777
47474747777777
Ouput
YES
NO
YES
"""

if __name__ == '__main__':
    t=int(input())
    while t>0:
        s=list(input())
        cnt=0
        dem=0
        for i in range (len(s)):
            if s[i]=='4':
                cnt+=1
            elif s[i]=='7':
                dem+=1
        if cnt+dem==len(s):
            print("YES")
        else:
            print("NO")
        t-=1