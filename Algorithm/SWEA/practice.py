def check(lis):
    num=0
    for _ in range(len(lis)):
        print(num)
        if _ % 2 == 0 :
            num+=3*lis[_]
        else:
            num+=lis[_]
    print(num)
    if num % 10 == 0:
        return True
    else:
        return False

check([6,6,9,4,8,1,6,6])
print(sum([6,6,9,4,8,1,6,6]))