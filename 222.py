from itertools import combinations
psd,sk=input().split()
sk=int(sk)
l=[]
dd=combinations(psd,len(psd)-sk)
for i in list(dd):
  l.append("".join(i))
print(min(l))
