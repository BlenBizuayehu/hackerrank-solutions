t= int(input())

for _ in range(t):
    n=int(input())

    arr = list(map(int, input().split()))

    if n<3:
        print(0)
        continue

    arr.sort()
    min_operations = float('inf')

    for i in range(n-2):
        cost = (arr[i+1]-arr[i]) + (arr[i+2]-arr[i+1])
        min_operations = min(min_operations, cost)

    print(min_operations)