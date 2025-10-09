from math import *

def nto(n):
    for i in range (2,int(sqrt(n)+1)):
        if n%i==0:
            return 0
    return n>1

if __name__ == '__main__':
    for _ in range (int(input())):
        a, b=map(int,input().split())
        s=str(gcd(a,b))
        sum=0
        for i in s:
            sum+=int(i)
        if nto(sum):
            print("YES")
        else:
            print("NO")

                
    
    
    
