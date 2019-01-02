def function():
    keys=['a','b','c','d','e','f']
    values=[0,1,2,3,4,5]
    return dict(zip(keys,values))

result = function()
    
for i in result:
    print("{}: {}".format(i,result[i]))
