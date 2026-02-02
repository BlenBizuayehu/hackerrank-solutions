
word=input().strip().lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
exists="YES"
for i in alphabet:
    if i not in word:
        exists="NO"
        break
print(exists)
