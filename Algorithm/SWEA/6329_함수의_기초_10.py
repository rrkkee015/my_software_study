lis =[]
def function(x):
    while x>0:
        lis.append(x)
        x-=1
    return lis

a=int(input())
result=function(a)
print("카운트다운을 하려면 0보다 큰 입력이 필요합니다. # 0보다 작은 값을 전달했을 경우")
for i in lis:
    print("{}".format(i))
