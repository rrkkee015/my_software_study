a=[]
for i in range(1,101):
    if i % 2 !=0:
        a.append(i)
        if i == 99:
            print(i)
        else:
            print(i, end=', ')
