l,o=map(int,input().split())
for g in  range(l+1,o):
  if(g>1):
    for i in range(2,g):
      if(g%i)==0:
        break
    else:
      print(g,'',end="")
