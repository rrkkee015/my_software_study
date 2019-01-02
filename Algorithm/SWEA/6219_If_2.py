x=int(input(""))
result=0
for i in range(1,x+1):
    if x%i==0:
        print("%d is %d"%(i,x))
        result +=1
if result ==2:
    print("%d is sosu"%x)
