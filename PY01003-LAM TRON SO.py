
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
        
        