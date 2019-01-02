# 1. list를 받을 친구를 만든다.
# 2. list를 순회하면서 각 친구와 임의의 숫자가 일치하는 게 있는지 확인한다.
# 3. 전체 다 돌아보고 없으면 False
# 4. 있으면 True

strnumbers = input().split(' ')
numbers=[]
for num in strnumbers:
    numbers.append(int(num))
#######################
def function(a):
    count = 0
    for i in numbers:
        if i == a:
            count +=1
    if count == 1:
        return "{} => True".format(a)
    else:
        return "{} => False".format(a)

x = function(5)
y = function(10)

print("{}\n{}\n{}".format(numbers,x,y))
