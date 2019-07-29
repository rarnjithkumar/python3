l,m=map(int,input().split())
for i in range(l,m):
  o=0
  temp=i
  while temp>0:
    g=temp%10
    o+=g**3
    temp//=10
  if i==o:
    print(i,"",end="")
