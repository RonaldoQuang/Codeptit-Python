from math import *
"""
Cho xâu ký tự có độ dài n bao gồm các ký tự từ a, b, …, z và các số từ 0 đến 9. 
Nhiệm vụ của bạn là tìm số nhỏ nhất xuất hiện trong xâu. Ví dụ với xâu X[]=”12ab29cd19” ta có kết quả là 12.
Input:
Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào T test. Mỗi test là một xâu ký tự thỏa mãn yêu cầu bài toán.
T, n thỏa mãn ràng buộc : 1≤T≤100; 1≤ n≤105;
Dữ liệu vào đảm bảo số lớn nhất cũng không quá 18 chữ số
Output:
Đưa ra kết quả mỗi test theo từng dòng.
Input
2
12ab29cd19
ab123gh456cd
Output
29
456
"""

if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        i=0
        MAX=-(1e18+1)
        while i<len(s):
            if i<len(s) and s[i].isdigit():
                sum=0
                while i<len(s) and s[i].isdigit():
                    sum=sum*10+int(s[i])
                    i+=1
                MAX=max(MAX,sum)
            else:
                i+=1
        print(MAX)
                
        


                
    
    
    
