# 함수

> Background

- 조건문 및 반복문
- 함수

> Goal

- 함수에 대한 이해

> Problem

- 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.
- sqrt() 사용 금지

![](image/1.png)

```python
def function(x):
    count = 0
    b = 1
    while b**2<x:
        b+=1
    a=b-1
    while count != 10:
        if ((a+b)/2)**2>x:
            b=(a+b)/2
        else:
            a=(a+b)/2
        count+=1
    return a,b
print(function(10))
```

