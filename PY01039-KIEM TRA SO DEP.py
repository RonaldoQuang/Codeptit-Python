"""
Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau và các chữ số ở cách nhau 2 vị trí đều bằng nhau. 
Ví dụ: 121, 1313131, 5656 …
Viết chương trình kiểm tra một số có phải số đẹp hay không?
Input
Dòng đầu ghi số bộ test. Mỗi bộ test ghi một số nguyên dương N (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.
Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
Input
3
12121212
343433
78789989
Output
YES
NO
NO
"""

from math import *
    
if __name__ == '__main__':
    for _ in range (int(input())):
        s=list(input())
        ok=1
        for i in range (2,len(s)):
            if i%2==0:
                if s[i]!=s[0]:
                    ok=0
                    break
            else:
                if s[i]!=s[1]:
                    ok=0
                    break
        if ok:
            print("YES")
        else:
            print("NO")
            
       
 

        

        

                
        


                
    
    
    
