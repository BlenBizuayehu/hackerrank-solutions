from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    m = k // 2
    available = n - m
    cnt = Counter(a)
    
    cost = 1
    while available > 0:
        if cnt[cost] > 0:
            take = min(cnt[cost], available)
            available -= take
            cost += 1
        else:
            break
    
    print(cost)