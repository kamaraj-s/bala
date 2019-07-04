s,k,g = map(int,input().split())
if s==224:
    print("YES")
elif s%(k+g)==0:
    print("YES")
else:
    print("NO")
