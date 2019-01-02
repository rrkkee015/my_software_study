lis_str=input()
lis_int=[int(x) for x in lis_str.split(' ')]

def function():
    return max(lis_int)

result=function()
print("max{} => {}".format(tuple(lis_int),result))
