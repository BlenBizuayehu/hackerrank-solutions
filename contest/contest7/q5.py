t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()
    b = input().split()
    
    pos = {}
    for i in range(n):
        pos[a[i]] = i
        
    offline = 1
    for i in range(n - 2, -1, -1):
        if pos[b[i]] < pos[b[i+1]]:
            offline += 1
        else:
            break
            
    print(n - offline)