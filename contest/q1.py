username=input().strip()
unique=set(username)
if len(unique)%2==1:
    print ("IGNORE HIM!")
else:
    print ("CHAT WITH HER!")
