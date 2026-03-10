n, t = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_time = 0
max_books = 0

for r in range(n):
    current_time += a[r]

    while current_time > t:
        current_time -= a[l]
        l += 1

    max_books = max(max_books, r - l + 1)

print(max_books)