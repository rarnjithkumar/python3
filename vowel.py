ll=input()
if (ll=='a' or ll=='e' or ll=='i' or ll=='o'or ll=='u' or ll=='A' or ll=='E' or ll=='I' or ll=='O' or ll=='U'):
    print("VOWEL")
elif ((ll>="a" and ll<='z') or (ll>='A' and ll<='Z')):
    print("Consonant")
else:
    print('invalid')
