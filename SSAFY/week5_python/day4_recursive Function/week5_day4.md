# Week5 day4

### 재귀 함수

- 함수 내에서 반환을 했을 때 다시 자기 자신을 부르는 함수

> 예시

n ! = f(n) = n x (n-1) x .... x 2 x 1

n ! = n x f(n-1)

n ! = n x n-1 x f(n-2)

n ! = n x n-1 x n-2 x f(n-3)

...

n! = n x n-1 x n-2 x ... x  f(1)

```python
def f(n)
if n == 0:
    return 1:
else:
    return n x f (n-1)
```

> 5가 들어왔다고 치면 5 x f(4) ==> 5 x 4 x f(3) ==> 5 x 4 x 3 x f(2) ==> 5 x 4 x 3 x 2 x f(1) ==> 5 x 4 x 3 x 2 x 1 x f(0) ==> 5 x 4 x 3 x 2 x 1 x 1

- 함수 내에서 **자기 자신(함수)를 부르는 것**이 재귀적 함수에 핵심이다.

- 근데 그 함수 부르는게 너무 깊어지면(많으면) 컴퓨터가 stack overflow라는 에러를 퉷 뱉어버린다. 

