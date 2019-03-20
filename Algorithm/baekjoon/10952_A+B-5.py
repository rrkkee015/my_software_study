def sum_(a,b):
    print(a+b)
    return

while True:
    x,y=list(map(int,input().split()))
    if x==0 and y==0:
        break
    sum_(x,y)