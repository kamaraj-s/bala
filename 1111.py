def check(q,l):
    a=l[0]
    s = []
    for i in range(len(q)):
        for j in range(1,len(l)):
            y=l[j]
            if j==(len(l)-1) and a[i] == y[i]:
                s.append(a[i])
            elif a[i] == y[i]:
                continue
            else:
                return s
    return s
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
q=min(l)
print("".join(check(q,l)))
