l,o=map(int,input().split())
a=(input().split())[0:l]
i=0
while i<o:
  m,n=map(int,input().split())
  i+=1
  print(min(a[m:n]))
