def function():
	number = int(input(''))
	good = number + (number*10+number) + (number*100+number*10+number) + (number*1000+number*100+number*10+number)
	return good

result = function()
print(result)
