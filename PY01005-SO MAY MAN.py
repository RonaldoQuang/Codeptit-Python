
if __name__ == '__main__':
    s=list(input())
    cnt=0
    dem=0
    for i in range (len(s)):
        if s[i]=='4':
            cnt+=1
        elif s[i]=='7':
            dem+=1
    if cnt+dem==4 or cnt+dem==7:
        print("YES")
    else:
        print("NO")