t=int(input())

for _ in range (t):
    n,m=map(int, input().split())

    a=[]

    for _ in range(n):
        a+=list(map(int,input().split()))

    if n*m==1:
        print(-1)
        continue

    b= a[1:] + a[:1]

    idx = 0
    for _ in range(n):
        print(*b[idx:idx+m])
        idx +=m