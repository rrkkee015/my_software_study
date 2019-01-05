# Datetime

- 파이썬에서 날짜와 시간을 다루는 라이브러리가 있는데 그 것이 Datetime이다.

  ```python
  import datetime
  
  datetime.datetime.now() #datetime 안에는 똑같은 이름의 datetime 클래스가 있다. now()라는 메소드는 현재 년 월 일 시 분 초 마이크로초를 알려준다.
  
  start_time = datetime.datetime.now()
  type(start_time)
  #결과
  <class 'datetime.datetime'>
  
  #datetime에는 replace라는 메소드가 있는데 가지고 있는 날짜와 시간을 바꿀 수 있는 메소드이다. start_time은 datetime 클래스이기 때문에 메소드를 바로 써보자
  start_time = start_time.replace(year=2017,month=2,day=1)
  #결과
  2017, 2, 1, 14,31 #원래 2016년도였음
  
  #replace는 이미 만들어진 datetime 클래스에 변경을 하기 위해 있는 것 처음부터 내가 원하는 날짜와 시간으로 만들기 위해서는 다른 방법이 필요하다.
  
  start_time = datetime.datetime(2012,2,1)
  start_time
  #결과
  2012, 2, 1, 0, 0
  ```

- datetime은 뺄셈 연산을 지원한다. datetime끼리 빼보도록 하자.

  ```python
  import datetime
  start_time = datetime.datetime(2020,2,1)
  how_long = start_time - datetime.datetime.now()
  #2020년 2월 1일까지 얼마나 남았는지 보여줌
  
  
  how_long.days
  #결과
  9
  how_long.seconds
  #결과
  2012305
  
  print("2020년 2월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days,how_long.seconds//3600))
  
  #이런식으로 표현이 가능하다.
  ```



## 연습문제

```python
#코드의 5번째 줄을 수정해서 days_until_christmas 함수가 오늘부터 2030년 12월 25일 사이에 몇일이 있는지를 리턴하도록 만들어 보세요. (단, 시간단위는 고려하지 마세요.)
import datetime

def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = (christmas_2030'''얘가 더 큰수임''' - datetime.datetime.now()).days # 몇 '일'만 물어봤으니 일만 쏙 빼자.
    return days


print("{}일".format(days_until_christmas()))
```





# Timedelta

- timedelta : 시간의 연산을 가능하게 해주는 클래스

```python
import datetime
#오늘부터 100일은 언제인지 알아보기 위한 것을 만들자
hundred = datetime.timedelta(days = 100)
datetime.datetime.now() + hundred
#결과
2019.03.20

#오늘부터 100일 전은 언제인지 알아보자
hundred_befor = datetime.timedelta(days = -100)
datetime.datetime.now() + hundred_before
#결과
100일 전 나옴

#굳이 hundred 자체를 그냥 빼도 된다. (before 선언을 할 필요가 없다.)
datetime.datetime.now() - hundred

tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0)+datetime.timedelta(days=1)
#오늘 9시부터 하루 뒤의 날짜와 시간을 구할 수가 있다. replace로 지금 시간을 바꾸고 하루럴 더 했으니까.
```

