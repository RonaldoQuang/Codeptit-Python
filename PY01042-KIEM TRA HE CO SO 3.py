"""
Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.
Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.
Input
Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.
Output
Nếu đúng in ra YES, nếu sai in ra NO.
Input
3
1214AB
10210221
22222222
Output
NO
YES
YES
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        s=input()
        ok=1
        for i in s:
            if i!='0' and i!='1' and i!='2':
                ok=0
                break
        if ok:
            print("YES")
        else:
            print("NO")

        

        

                
        


                
    
    
    
