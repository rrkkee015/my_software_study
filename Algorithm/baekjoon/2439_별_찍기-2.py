N=int(input(''))
i=N
count = 1
while i>0:
    print(" "* (i-1) + "*" * count)
    i -= 1
    count += 1
