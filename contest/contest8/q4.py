t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    p = [0] * n
    left = 0
    possible = True

    while left < n:
        right = left

        while right < n and s[right] == s[left]:
            right += 1

        window_size = right - left

        if window_size == 1:
            possible = False
            break

        p[left] = right
        for k in range(left + 1, right):
            p[k] = k

        left = right

    if not possible:
        print(-1)
    else:
        print(*p)