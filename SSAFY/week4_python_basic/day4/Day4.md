# Week4 - Day 4

- python에서 webbrowser를 다룰 수 있다.

```python
import webbrowser

webbrowser.open("https://www.daum.net")

# 모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드

webbrowser.open("https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EC%97%B0%EC%9A%B0") #모모랜드 연우 검색결과
webbrowser.open("https://search.daum.net/search?nil_suggest=sugsch&w=tot&DA=GIQ&sq=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EB%82%B8%EC%8B%9C&o=1&sugo=15&q=%EB%AA%A8%EB%AA%A8%EB%9E%9C%EB%93%9C+%EB%82%B8%EC%8B%9C") #모모랜드 낸시 검색결과
```

위 코드는 너무 무식해

```python
import webbrowser

webbrowser.open(url)

#webbrowser.open("https://search.daum.net/search?q=검색어") #다음 기존 검색 url
url = "https://search.daum.net/search?q=" + "연우"
```

근데 우리 input 배웠잖아

``` python
import webbrowser

keyword = "연우"
url = "https://search.daum.net/search?q="

webbrowser.open(url + keyword)
```

이러면 키워드 맨날 바꿔야 함. input 넣자

```python
import webbrowser

keyword = input("검색어를 입력해주세요: ")
url = "https://search.daum.net/search?q="

webbrowser.open(url + keyword)
```

모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드를 만들어보쟈, **반복문을 사용**

```python
import webbrowser

url = "https://search.daum.net/search?q="

momo = ["나윤","혜빈","낸시","연우","아인","주이","제인","데이지","태하"]
# momo라고 하는 리스트를 한 번씩 돌면서, 웹 브라우저를 연다.
for keyword in momo:
    webbrowser.open(url + keyword)
```



- 앞서 짠 파이썬 파일을 github에 올리는 법

1. gitbash에서 git init을 한다.
2. git add .browser.py (위에 짠 파일을 browser.py라고 만들었었다)
3. git commit -m "아무거나"
4. 레포지토리에서 주소 복사해서 넣자
5. git push하자
   - 여기까지는 동일하다.
6. 



- .gitignore라고 파일을 만들고 파일 안에서 .vscode/라고 하면 .vscode/ 하위 폴더들은 git에 안 올라간다. git에서 관리 안한다는 뜻



- **Git Bash 글씨 깨지는 거 고치는 법** 

1. git bash 킨다.
2. 상태 표시줄을 우클릭한다.
3. Options 들어가서 Text로 들어간다.
4. 거기서 Locale은 ko_KR, Character set은 eucKR로 바꾸고 Apply => Save !