x,y=map(int,input().split(' '))
d=[31,28,31,30,31,30,31,31,30,31,30,31]
w=["MON","TUE","WED","THU","FRI","SAT","SUN"]
print(w[(sum(d[i] for i in range(0,x-1))+y)%7 -1])

