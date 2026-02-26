t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    total=sum(arr)

    if total%n !=0:
        print("-1")
    else:
        average=total//n

        k=0
        for j in arr:
            if j>average:
                k+=1

        print(k)


