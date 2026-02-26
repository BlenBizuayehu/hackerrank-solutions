t=int(input())

for _ in range(t):
    n,p= map(int, input().split())

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    hubs=[]

    for i in range(n):
        if b[i]<p:
            hubs.append([b[i], a[i]])

    hubs.sort()

    total_cost=p
    hubs_reached=1

    for cost,capacity in hubs:
        needed=n-hubs_reached

        can_share=min(capacity,needed)

        total_cost+=(can_share* cost)
        hubs_reached+=can_share

    if hubs_reached< n:
        total_cost+= (n- hubs_reached)*p

    print(total_cost)
