def function():
    numbers_first=list(range(1,11))
    numbers_second=list(filter(lambda x: x%2==0,numbers_first))
    numbers_third=list(map(lambda x: x**2,numbers_second))
    return numbers_third

result=function()
print(result)
