# 1월 7일 숙제

> Background 

```
> 기초 문법
> 변수 및 자료형
```

> Goal

```python
> Python programming 언어의 기본 문법 이해
> 변수 및 자료형에 대한 이해
```

> Problem

- 두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태로 출력해보세요.

  ```python
  n, m = 5, 9
  s="*"*n
  print(s+('\n'+s)*(m-1))
  ```

- 다음 딕셔너리에서 평균 점수를 출력하시오.

  ```python
  #문제
  student = {'python':80, 'algorith':99, 'django':89, 'flask':83}
  total = 0
  for i in student.values():
      total += i
  result=total/len(student)
  print(result)
  ```

- 다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형별 학생수의 합계를 구하시오.

  ```python
  #문제
  blood_types=['A','B','A','O','AB','AB','O','A','B','O','B','AB']
  count_A = 0
  count_B = 0
  count_O = 0
  count_AB = 0
  for i in blood_types:
      if i == 'A':
          count_A += 1
      elif i == 'B':
          count_B += 1
      elif i == 'O':
          count_O += 1
      else:
          count_AB += 1
  print("{}\n{}\n{}\n{}".format(count_A,count_B,count_O,count_AB))
  ```
