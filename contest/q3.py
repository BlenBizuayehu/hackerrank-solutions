password= input().strip().lower()
n=int(input())
words=[input().strip().lower() for _ in range(n)]

can_unlock=False
for word in words:
    if word ==password:
        can_unlock=True
        break

if not can_unlock:
    first_letter=password[0]
    second_letter=password[1]
    for w1 in words:
        for w2 in words:
            if w1[1] == first_letter and w2[0]==second_letter:
                can_unlock=True
                break
        if can_unlock:
            break
if can_unlock:
    print("YES")
else:
    print("NO")