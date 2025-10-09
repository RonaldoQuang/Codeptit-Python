from math import *
"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:
Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0.
Tổng các chữ số ở vị trí lẻ
Input
Dòng đầu ghi số bộ test (không quá 20)
Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)
Output
Với mỗi bộ test, viết trên một dòng hai giá trị: tích chữ số và tổng chữ số tính được.
Input
3
12345678
20000
22334455667788
Output
105 20
2 0
40320 35
"""

if __name__ == '__main__':
    for _ in range(int(input())):
        s=list(input())
        ok=0
        tong=0
        tich=1
        for i in range (len(s)):
            if i%2==1:
                tong+=int(s[i])
            else:
                if int(s[i])!=0:
                    ok=1
                    tich*=int(s[i])
        if ok:
            print(tich,tong)
        else:
            print(0,tong)

        

        

                
        


                
    
    
    
