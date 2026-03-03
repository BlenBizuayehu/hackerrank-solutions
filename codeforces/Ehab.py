n = int(input())
arr = list(map(int, input().split()))

has_odd = False
has_even = False

for num in arr:
    if num % 2 == 0:
        has_even = True
    else:
        has_odd = True

if has_odd and has_even:
    arr.sort()

print(*arr)