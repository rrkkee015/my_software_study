#오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

#1. x월 전까지 모든 일 수를 더한다.
#2. y만큼 또 더하고
#3. 7로 나누어서 나오는 값에 따라 월,화,수,목,금,토,일을 배정한다.
#4. 출력한다.
x,y = input('').split(' ')
x,y = int(x),int(y)
month_lis = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_day = 0
day=y
for i in range(0, x-1):
    month_day += month_lis[i]
result = month_day + day
result = result % 7
if result == 1:
    print("MON")
elif result == 2:
    print("TUE")
elif result == 3:
    print("WED")
elif result == 4:
    print("THU")
elif result == 5:
    print("FRI")
elif result == 6:
    print("SAT")
elif result == 0:
    print("SUN")
