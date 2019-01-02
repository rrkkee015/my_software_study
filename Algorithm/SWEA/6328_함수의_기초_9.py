
def function():
    a, b = input().split(', ')
    if len(a) < len(b):
        return b
    elif len(a) > len(b):
        return a
    else:
        return draw

result=function()
print(result)
