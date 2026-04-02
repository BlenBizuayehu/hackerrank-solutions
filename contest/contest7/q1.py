n=int(input())
a=list(map(int, input().split()))

l=0
r=n-1

s=0
d=0

turn=0

while(l<=r):
    if a[l]>a[r]:
        picked= a[l]
        l+=1
    else:
        picked=a[r]
        r-=1

    if turn==0:
        s+=picked
        turn=1
    else:
        d+=picked
        turn=0

print(s,d)