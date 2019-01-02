def function():
    numbers_first=list(range(1,11))
    numbers_second=list(map(lambda x: x**2,numbers_first))
    return numbers_second

result=function()
print(result)
