t = int(input())

for _ in range(t):
    n, m, p, q = map(int, input().split())

    if n % p == 0:
        total = (n // p) * q
        if total == m:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")