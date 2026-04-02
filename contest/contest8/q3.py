n = int(input())
s = input()

if n == 1:
    print("Yes")
    exit()

s_sorted = sorted(s)

duplicate = False

for i in range(n - 1):
    if s_sorted[i] == s_sorted[i+1]:
        duplicate = True
        break

if duplicate:
    print("Yes")
else:
    print("No")
