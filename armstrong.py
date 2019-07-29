l=int(input())
o=0
temp=l
while temp>0:
  g=temp%10
  o+=g**3
  temp//=10
if l==o:
  print("yes")
else:
  print("no")
