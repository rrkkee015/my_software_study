# List

- 파이썬에서는 쉽게 원하는 구성요소를 가지는 리스트를 갖는 방법을 제공한다. 한 번 익숙하면 되게 좋음

- 1부터 10까지의 변을 가지는 정사각형의 변을 가지는 코드를 만들자

  ```python
  areas =[]
  for i in range(1, 11):
      areas = areas + [i*i]
  print(areas)
  
  #얘도 되지만 한 줄로 해결 가능
  
  areas2=[i*i for i in range(1,11)] #끝
  ```

- 나머지 0 일 때만 계산하는 코드

  ```python
  areas =[]
  for i in range(1, 11):
      if i%2 ==0:
      	areas = areas + [i*i]
  print(areas)
  
  #얘도 되지만 한 줄로 해결 가능
  
  areas2=[i*i for i in range(1,11) if i%2 == 0] #끝
  ```

- 그리고 for 문을 중첩해서 만들 수 있다.

  ```python
  [(x,y) for x in range(15) for y in range(15)]
  #이러면 둘 다 출력됨
  [(0,0),(0,1),(0,2)......(0,14)....(14,14)]
  ```



#