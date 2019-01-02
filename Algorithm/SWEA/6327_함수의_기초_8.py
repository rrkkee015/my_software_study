# 1. 변수를 받으면 제곱하는 친구를 만든다.
# 2. 함수를 만든다.
# 3. 출력한다.

def function(x, y):
    total1 = x*x
    total2 = y*y
    return total1,total2
a,b = input().split(', ')
a,b = [int(a),int(b)]
result = function(a,b)
print ("square({}) => {}\nsquare({}) => {}".format(a,result[0],b,result[1]))
