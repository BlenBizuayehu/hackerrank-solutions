t=int(input())

for _ in range(t):
    n=int(input())
    arr= list(map(int,input().split()))
    possible=False
    
    can_go_left=False
    for i in range(n):
        if arr[i]>2*i:
            can_go_left=True
            break

    can_go_right=False

    for i in range(n):
        right_dist= (n-1)-i
        if arr[i]>2*right_dist:
            can_go_right=True
            break

    if can_go_left and can_go_right:
        print("YES")
    else:
        print("NO")