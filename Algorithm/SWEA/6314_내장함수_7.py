def function():
    numbers = list(range(1,11))
    even = list(filter(lambda x: x%2 ==0,numbers))
    return even

result = function()
print(result)
