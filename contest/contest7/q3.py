t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    
    first_a = -1
    last_b = -1
    
    for j in range(n):
        if s[j] == 'A':
            first_a = j
            break
            
    for j in range(n):
        if s[j] == 'B':
            last_b = j
            
    if first_a == -1:
        print(0)
    elif last_b == -1:
        print(0)
    elif first_a > last_b:
        print(0)
    else:
        ans = last_b - first_a
        print(ans)