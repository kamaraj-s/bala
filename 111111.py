sh=int(input())
sk=list(map(int,input().split()))
st=0
for i in range(len(sk)-2):
   for j in range(i+1,len(sk)-1):
         for e in range(j+1,len(sk)):
            if sk[i]<sk[j]<sk[e] and i<j<e:
                st+=1
print(st)
