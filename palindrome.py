l=int(input())
temp=l
rev=0
while(l>0):
    dig=l%10
    rev=rev*10+dig
    l=l//10
if temp==rev:
    print("yes")
else:
    print("no")
