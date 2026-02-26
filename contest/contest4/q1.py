t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))

    unique=set(arr)
    k=len(unique)

    if k==0:
        print(0)
    else:
        result=2*k-1
        print (result)