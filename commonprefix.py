l=int(input())
o=[]
for i in range(0,l):
  log=input()
  o.append(log)
g=[]
for i in zip(*o):
  if(i.count(i[0])==len(i)):
    g.append(i[0])
  else:
    break
print(''.join(g))
