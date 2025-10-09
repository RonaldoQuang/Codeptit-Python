from math import *
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

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print("1 * ",end="")
        for i in range (2,int(sqrt(n)+1)):
            cnt=0
            while n%i==0:
                cnt+=1
                n//=i
            if cnt and n!=1:
                print(i,"^",cnt," * ",sep="",end="")
            elif cnt and n==1:
                print(i,"^",cnt,sep="",end="")
        if n!=1:
            print(n,"^1",sep="",end="")
        print()

        

        

                
        


                
    
    
    
