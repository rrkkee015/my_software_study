# 함수

> Background

- 조건문 및 반복문
- 함수

> Goal

- 조건문 및 반복문에 대한 이해
- 함수에 대한 이해

> Problem

1. Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서 'a' 'nan' '토마토' 모두 palindrome에 해당합니다.
2. 따라서, 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요옷

```python
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
a = palindrome('토마토')
b = palindrome('멋쟁이토마토')
c = palindrome('바밤바바밤바봐')
print(a)
print(b)
print(c)

#선생님 version
def is_palindrome(word):
    list_word = list(word)
    for i in range(len(list_word) // 2):
        if list_word[i] != list_word[-i-1]:
            return False
        else:
            return True

print(is_palindrome('level'))
print(is_palindrome('apple'))
```

