"""
Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:
Nếu N>10, làm tròn đến số hàng chục gần nhất
Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
Cứ tiếp tục như vậy …
Chú ý: Giá trị 5 sẽ được làm tròn lên.
Input
Dòng đầu ghi số bộ test (không quá 100)
Mỗi bộ test ghi số N trên một dòng (N nguyên dương và không quá 9 chữ số)
Output
Với mỗi test, ghi ra kết quả làm tròn tương ứng trên một dòng.
Input
7
15
14
5
99
12345678
44444445
1445
Output
20
10
5
100
10000000
50000000
2000
"""

if __name__ == '__main__':
    t=int(input())
    for i in range (t):
        w=input()
        s=list(w)
        for j in range (len(s)-1,0,-1):
            if int(s[j])>=5:
                s[j]='0'
                s[j-1]=str(int(s[j-1])+1)
            else:
                s[j]='0'
        for j in range (len(s)):
            print(s[j],end="")
        print()
        
        
