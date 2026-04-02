t=int(input())

for _ in range(t):
    n,k= map(int, input().split())

    brand = [0] * (k+1)

    for _ in range(k):
        b,c=map(int, input().split())
        brand[b]=brand[b]+c

    vals = sorted(brand, reverse=True)

    print(sum(vals[:n]))