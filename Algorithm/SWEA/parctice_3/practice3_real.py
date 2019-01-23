li=[[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
result=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def my_sort(li):
    nums=99999
    lis=[]
    for a in range(25):
        for i in range(len(li)):
            for j in range(len(li[i])):
                if nums>li[i][j]:
                    nums=li[i][j]
                    a=i
                    b=j
        lis.append(nums)
        nums=99999
        li[a][b]=999999
    return lis

def snail(li):
    x, y = len(result)//2,len(result)//2
    n = 1
    a, b = (n, n)
    q = 1
    result[x][y] = li[-1]
    for i in li[::-1][1:]:
        if a != 0:
            y -= 1 * q
            result[x][y] = i
            a -= 1
            continue
        elif b != 0:
            x += 1 * q
            result[x][y] = i
            b -= 1
        else:
            q *= -1
            y -= 1 * q
            result[x][y] = i
            n += 1
            a, b = (n, n)
            a -= 1
    return result

li=my_sort(li)
print(snail(li))
