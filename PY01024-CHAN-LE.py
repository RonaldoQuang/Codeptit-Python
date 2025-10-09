from math import *
"""
Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?
Tổng chữ số của N chia hết cho 10
Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.
Output
Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
Input
2
246864
1353
Output
YES
NO
"""
def tong(s):
    sum=0
    for i in range (len(s)):
        sum+=int(s[i])
    return sum

def check(s):
    ok=1
    for i in range (1,len(s)):
        if abs(int(s[i])-int(s[i-1]))!=2:
            ok=0
            break
    if ok and tong(s)%10==0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        check(s)
        
        


                
    
    
    
