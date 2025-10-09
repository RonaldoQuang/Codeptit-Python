from math import *
"""
Cho một số nguyên dương N. 
Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. 
Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.
Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.
Input:
Dòng đầu ghi số bộ test (không quá 1000).
Mỗi test ghi số N (1 ≤ N ≤ 1018)
Output:
Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. 
Hoặc số -1 nếu không thể tìm được đáp án.
Input
5
1
2
3
4
999999
Output
77
77
9447438
77
999999
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

        

        

                
        


                
    
    
    
