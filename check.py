a=int(input())
b=int(input())

for i in range(a,b+1):
    c=0
    for j in range(1,i):
        if i%j==0:
            c+=j
    if c==i:
        print(i,end=" ")
