n=int(input())
cards=list(map(int,input().split()))

sereja=0
dima=0

l=0
r=n=1
turn=True

while l<=r:
    if cards[l]>cards[r]:
        chosen=cards[l]
        l+=1
    else:
        chosen=cards[r]
        r-=1
    if turn:
        sereja+=chosen
    else:
        dima+=chosen
    turn= not turn

print(sereja,dima)