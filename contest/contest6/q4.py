n,k=map(int,input().split())
a=list(map(int,input().split()))

for _ in range(k):
    minimum=float('inf')
    for x in a:
        if x>0:
            minimum=min(minimum, x)

    if minimum == float('inf'):
        print(0)
    else:
        print(minimum)

        for i in range(n):
            if a[i]>0:
                a[i] -=minimum




