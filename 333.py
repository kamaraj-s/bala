sk,jit1=map(str,input().split())
sat=0
if len(sk)>len(jit1):
  sk,jit1=jit1,sou
i=0
while i<len(sk):
  sat+=(ord(jit1[i])-ord(sk[i]))
  i+=1
for i in range(i,len(jit1)):
  sat+=ord(jit1[i])-ord('a')+1
print(sat)
