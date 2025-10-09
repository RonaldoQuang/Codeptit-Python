from math import *

def check(s):
    ok=1
    for i in range (len(s)-1):
        if int(s[i])>int(s[i+1]):
            ok=0
            break
    if ok==1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    for _ in range (int(input())):
        w=input()
        s=list(w)
        print(check(s))


                
    
    
    
