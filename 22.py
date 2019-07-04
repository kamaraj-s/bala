sk,sj=input().split()
PG=abs(len(sk)-len(sj))
for i in range(len(sk)):
  if len(sj)==1 and sj[i] in sk:
   break
  if sk[i]!=sj[i]:
   PG+=1
print(PG)
