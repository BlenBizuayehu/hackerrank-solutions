t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    b.sort()
    
    discount = 0
    current_sum = 0
    
    for x in b:
        current_sum += x
        
        if current_sum <= n:
            discount += a[current_sum - 1]
        else:
            break
            
    total_cost = sum(a) - discount
    print(total_cost)