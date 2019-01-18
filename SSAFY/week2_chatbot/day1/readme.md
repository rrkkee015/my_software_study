# 2018 - 12 - 17

## Python 기초

Python은 저장, 조건, 반복만 알면된다. + 함수

- 저장 (변수, 리스트, 딕셔너리)

  - 박스를 떠올려보자 그 안에 숫자를 집어넣고 스티커로 dust라고 붙히면?

    ```python
    dust = 60 #dust라는 변수에 60이라는 숫자를 저장한다.
    dust == 60 #dust는 60과 같다. (우리가 원래아는 개념은 2개 !!)
    ```

  - 박스에는 숫자, 문자, 참/거짓을 저장가능하다.

    ```python
    Hi="안녕하세요"
    for i in range(5):
        print(hi)
    ```

    ```python
    print(hello) # hello 변수에 담긴 내용을 출력해라
    print("hello") # hello 문자를 출력하라
    ```

  - 그렇다면 각 박스마다 변수선언을 전부 다 해야하나??? ㄴㄴ 쉬운 방법이 있다. 그 방법이 **list**

    - 배열에 문자열과 숫자형 둘 다 넣을 수 있다.

    ```python
    dust = [58, 40, 70]
    print(dust[1])
    ```

    ```python
    location = ["강남구","서초구","용산구"]
    value = [58,40,30]
    ```

    - 아니 근데 나는 위에거 보다 더 편하게 쓰고 싶어 이거 많아지면 내가 몇 열에 있는지 일일이 세야하잖아 ㅠ

  - 그래서 있는 것이  **dictionary**

    - 박스에다가 이름표를 붙혔다고 생각하면 편함

      ```python
      dust ={"강남구":58,"서초구":40,"용산구":30}
      print(dust["강남구"])
      print(변수명[key])
      ```

    - 예시

      ```python
      menu=["순남시레기","멀캠 20층","양자강","강남목장"]
      menu_detail={"순남시레기":"시레기국","멀캠 20층":"오늘의 메뉴","양자강":"차돌짬뽕","강남목장":"뚝배기 불고기"}
      lunch = menu[1]
      print(lunch + "에서는" + menu_detail[lunch] + "를 먹는 것이 좋습니다")
      ```

- 조건 (if 문)

  - 상황에 맞는 결과값을 True와 False로 이용해서 만들어 냄.

    ```python
    #기본형
    if (True):
        print("조건문입니다.")
    ```

    - 예시

      ```python
      if dust >50:
          print("50 초과")
      else:
          print("50 이하")
      ```

  - if, elif, else로 다양한 조건문을 만들 수 있다.

    - 예시

      ```python
      dust=int(input(""))
      condition=""
      if dust >150:
          condition ="매우 나쁨"
      elif 80 < dust <= 150:
          condition ="나쁨"
      elif 50 < dust <= 80:
          condition ="보통"
      else:
          condition ="좋음"
          
      print("오늘의 미세먼지 상태는 %s 입니다."%condition)
      #print("오늘의 미세먼지 상태는 +condition+ 입니다.)도 된다.
      ```

- 반복문 (while, for 문)

  - while

    - 반드시 참에서 거짓이거나, 항상 거짓에서 참만 찾는 루팅을 해야한다. 안 그러면 무한 반복임. 즉, 직접 종료되는 조건을 정해야한다.

      ```python
      n=0
      while n<3:
          print("출력")
          n=n+1 #n=n+1은 수학적으로 말도 안되지만 여기선 n+1를 n에 넣어준다는 뜻이다.
      ```

  - for 문

    - for i in List: 구조를 기본으로 하는데 i는 가변수라고 불리고, 여기서만 쓰이고 버려진다.

      ```python
      dust=[59,24,42]
      for i in dust:
          print(i)
      ```

  - 반복문 예시

    ```python
    dish = ["삼겹살","꽃등심","파스타","짬뽕","피자"]
    #1. for문을 이용해서 dish에 담긴 모든 음식을 나열하는 코드를 작성해보시오.
    for i in dish:
        print(i)
        
    #2. for문과 while문을 동시에 이용해서 dish에 담긴 모든 음식을 연속 두 번씩 나열하는 코드를 작성해보시오.
    n=0 #이렇게 n=0이 밖으로 나와있으면 삼겹살만 2번 돌고 끝난다.
    for i in dish:
        while n<2:
            print(i)
            n=n+1
            
    for i in dish: #이게 맞는 정답
        n=0
        while n<2:
            print(i)
            n=n+1
       
    #3. while과 for문의 위치를 바꿔서 풀어보자
    n=0 #이렇게 적으면 삼겹살과 꽃등심만 나온다.
    while n<5:
        a=[0,1]
        for i in a:
            print(dish[i])
            n=n+1
    
    n=0 #이게 맞는 정답
    a=[0,1]
    while n<5:
        for i in a:
            print(dish[n])
        n=n+1 
    ```

- 함수 (Function)

  - 내장함수

    - import를 하지 않아도 쓸 수 있는 함수 ex) print(), abs(), len()

  - 외장함수

    - 외부 기능을 미리 선언해야하는 함수 ex) import requests, import random

    - 예제 (점심 메뉴 골라주기)

      ```python
      import random
      #List
      menu =["순남시레기","멀티 캠퍼스 20층","양자강","강남목장","시골집"]
      #Dictionary
      menu_detail={"순남시레기":"시레기국","멀티 캠퍼스 20층":"오늘의 메뉴","양자강":"차돌박이 짬뽕","강남목장":"뚝배기 불고기","시골집":"쌈밥정식"}
      
      lunch=random.choice(menu)
      print("%s 에서는 %s 를 먹는 것이 좋습니다"%(lunch,menu_detail[lunch]))
      ```

      - 참고로 random.sample(리스트,갯 수)는 로또 뽑기처럼 비 복원 추출이다.

    - 여기서 문제 !

      ```python
      dust = {"강남구":40,"용산구":35,"성산구":60}
      for i in dust:
          print(i)
      #위의 코딩은 과연 key값이 나올까요? value값이 나올까요?
      
      #정답은 key 값 입니다 !
      for i in dust:
          print(dust[i])
      #위의 코딩 처럼 key 값만 알면 간단히 value 값을 구할 수 있기 때문에 key 값을 반환해 줍니다
      ```


## 실습

### 1. 카카오톡 챗봇 이용

- 카카오톡 챗봇 친구 추가하기
  - @ssp-003 검색하기
  - 친구 추가히기
    - 다른 반과 섞이지 않도록 주의할 것
  - "안녕" 메세지 보내서 인증 번호 받기
  - 인증 번호 받아서 채팅창에 입력하기
  - 인증 완료
  - s3.py.hphk.io에 접속
    - 이 안에서 많은 Input, Output을 직접 짤 수가 있고, 저장을 한다면 바로 카카오톡으로 적용이 된다.
  - "미세먼지"를 입력하면 강남구의 미세먼지 농도를 알 수 있다.
    - "미세먼지"는 미세먼지, "날씨"는 날씨를 알 수 있다.


### 2. Typora 이용

- 글씨크기 조절
  - #의 갯수에 따라 글씨 크기가 달라진다.
- `hi!`  '' 작은 따옴표로 표현 가능하다.
- -로 옆에 동그라미 가능하구
  - tab으로 들여쓰기 가능하구
    - 한번 더 가능하다
      - 계속 가능함.
  - 들여쓰기에서 엔터 치면 밖으로 나갈 수 있다.
- 이렇게

뿅

- *app.py* <-- ** 표시로 기울일 수도 있다.

```python
#app.py
def cal():
    print("Hello world")
    return a+b
```

- **볼드 처리 하기 위해서는 *두개로 감싼다.**

  - ##### #5개도 볼드 처리이다. 단 한 줄 전체가 볼드 처리 됨

- [이것은 링크입니다.](http://image.tvdaily.co.kr/upimages/gisaimg/201802/1518647565_1325024.jpg) 링크는 []()으로 표현한다. [] 안에는 내가 넣은 제목 () 안에는 연우 링크 ♥ 

  - **링크를 클릭할 땐 ctrl + 클릭으로**

- 이미지 URL은 ![]() 로 삽입한다. 

![모모랜드 연우](http://image.tvdaily.co.kr/upimages/gisaimg/201802/1518647565_1325024.jpg)

- 이것은 문서입니다.  밑에처럼 예외사항을 추가할 땐 >를 쓴다.

> 하지만 문서가 아닐 수도 있습니다.
>
> > 하지만 일수도 있지요.
> >
> > > 그렇답니다.

- 표

  | 본문에서 | 표 들어가고 | 간단하게 삽입 |
  | -------- | ----------- | ------------- |
  |          |             |               |
  |          |             |               |
  |          |             |               |

### 3. API

- API란?
  - Interface는 정해진 곳에 정해진 형태로 요청을 보내면 정해진 정보가 온다는 뜻이다. (마치 우편 보내는 것과 같음)
  - 우리가 직접 습도를 잴 필요 없이 이미 측정된 데이터를 기상청에서 받아서 쓰면된다.
  - 참고로 응답없음 404와 같이 에러가 떠도 결국은 응답이 온 것이다.

### 4. 크롤링

- s3.py.hphk.iod의 날씨 부분에서 미리 짜여져 있는 코드를 들고 와보자

```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID="+key
#print(url)

data = requests.get(url).json() # json()처럼 안에 인자가 없을 수도 있다. json()의 인자는 앞에 있는거임 때에 따라 다르다.
#requests는 주소창에 주소를 입력하는 것과 같은 기능이다. 
#get은 requests의 기능 안에서 get의 기능을 쓰기 위해서 .을 붙임 . 뒤에 붙어있는 애들은 하나의 기능으로서 전부 method 이다.
# requests => 기능 뭉탱이
# .get => requests가 가진 기능 중 하나 => 또 하나의 기능 뭉탱이을 뱉어낸다.
# .json => 위에서 나온 기능 뭉탱이의 기능 중 하나를 사용해서 또 하나의 기능 뭉탱이를 뱉어낸다.
#print(data) #요청을 보냈으니 응답이 온다. json은 응답으로 온 친구를 json 형태로 보여주세요의 뜻이다.
#print(type(data)) #data의 타입을 확인했다. 즉 .json()이 뱉어낸 결과가 딕셔너리이다.
#print(data["weather"])#이런식으로 또 method를 붙여나갈 수 있는데 이것을 method 체이닝이라고 함.
#원래라면 json 형식이 되어야하는데 파이썬은 json은 읽지 못한다. 따라서 딕셔너리 형태로 뱉어낸 것이고
#혹여나 루비, 자바 스크립트 등 다른 언어에서는 다른 형태로 나올 것이다. 자바는 그대로 json
#print(data["weather"][0])#리스트를 벗겨냈다. 어머 ㅎ
#print(data["weather"][0]["description"])#내가 원하는 놈 찾음

#한번 더 해보자
#print(data["main"])
#print(data["main"]["temp"])

#print(data["wind"]["speed"])
#print(data["visibility"])
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15 #float은 문자에서 숫자로 float 형태를 바꾸는 거다.
wind = data["wind"]["speed"]
visibility = data["visibility"]
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
현재 풍속은 {:.1f} m/s 이며 가시거리는 {}m 입니다.
""".format(weather, temp, temp_min, temp_max, wind, visibility) #"""는 줄 바꿈이 가능하다.
)

#이미 걸레짝이 된 이유는 내가 수업시간에 계속해서 만졌기 때문이다.
```

위의 예를 하나하나 뜯어보도록 하자

1.  url ="http://api.openweathermap.org 어쩌구 저쩌구" 요게 바로 내가 요청을 보낸 주소이다. 얘를 print(url)로 육안으로 보면 딕셔너리 타입의 자료가 나온다.
2.  requests가 요청을 보내는 코드이다. 또한 requests의 기능안의 get을 쓰고 get 기능안의 json이라는 기능을 반복해서 쓴다.
3. 분명 json으로 요청을 보내고 json 형태로 받기러 했지만 python은 json을 읽지 못하기에 dict 형태로 자동으로 바뀐 것이다. 다른 언어에서는 또 바뀔 수 있다.

요청을 해서 응답을 받은 정보들이 밑에 나와있다.

이 중 연무는 value이고 description은 key이다. 얘는 지금 하나의 리스트에 있고 또 그 속에서 weather라는 키의 value이다. 따라서 value이자 list이자 또 누군가의 value이다. 바람둥이다.

이 중에서 우리가 원하는 건 날씨를 끄집어서 날씨만 볼 것이다. 그 밑은 온도를 끄집어 내는 과정이다.

```json
{'coord': {'lon': 126.98, 'lat': 37.57}, 
'weather': [{'id': 721, 'main': 'Haze', 'description': '연무', 'icon': '50d'}],
'base': 'stations', 
'main': {'temp': 279.11, 'pressure': 1018, 'humidity': 30, 'temp_min': 278.15, 'temp_max': 279.95},
'visibility': 10000, 
'wind': {'speed': 3.1, 'deg': 280},
'clouds': {'all': 0}, 'dt': 1545026400, 'sys': {'type': 1, 'id': 8105, 'message': 0.0065, 'country': 'KR', 'sunrise': 1545000046, 'sunset': 1545034526}, 'id': 1835848, 'name': 'Seoul', 'cod': 200}
```

```python
print(data["weather"]) #weather 머리 끄덩이 잡고 나옴
print(data["weather"][0]) # weather를 둘러 싼 리스트 벗겨버림,[0] 없으면 오류난다.
print(data["weather"][0]["description"])# weather의 첫 번째 리스트에 있는 디스크립션 value 값을 머리 끄덩이 잡고 끌고 나옴

print(data["main"]) #main 머리 끄덩이 잡고 나왔음
print(data["main"]["temp"]) #main에 숨고있는 temp 값을 또 끄집고 나옴
```

## GIT 사용

- GUI는 인간이 보다 편리하게 컴퓨터를 사용하기 위해서 만든 화면 중심? 화면이다. 하지만 우리는 이제 CLI (Command Line Interface)를 사용할 것이다. 그 검은 화면에서 제작자들이 사용하는 간지나는 프로그램을 CLI라고 한다

  - CLI 종류
    1. 유닉스 shell (sh, zsh, bash 등) : 서버 개발자는 무조건 리눅스 쓴다. 윈도우 안 씀
    2. CP/M
    3. DOS의 command.com (cmd 말하는 듯)
    4. etc...

  ### GIT 설치

- GIT bash로 GITHUB에 자료 올리기

  - 구글에 git for windows를 쳐서 다운
  - 다운 받으면 git bash를 쓸 수 있는데 리눅스 명령어를 사용할 수 있는 공간이다.
    - GIT bash에서 cd를 한 번 쳐준다 (홈으로 돌아가는 것)
    - Documents 엔터 (Documents 이동)
    - mkdir week2 (week2의 폴더 생성)하고 cd week2 (week2의 폴더로 들어감)
    - mkdir day1 (day1의 폴더 생성)하고 cd day1 (day1의 폴더로 들어감)
    - touch readme.md(마크다운 파일을 생성한다.)
    - 배웠던 과정을 readme 파일에 복사 붙혀넣기 !
  - 위 과정을 잘 따라 했다면 github 사이트를 들어가서 Repository로 들어가자
    - 참고로 GIT의 좋은 점은 수정이 계속해서 가능하단 건데 그 수정이 마음에 안 들면 다시 되돌아갈 수 있다.
    - 하나의 파일을 최종, 진짜 최종, 진짜 진짜 최종 이런 식으로 만들면 관리도 힘들고 용량도 불어나니까 GIT은 이 점을 방지하기 위해서 버전별로 나누었다.
  - GIT bash에서 pwd를 사용해서 현재 디렉토리가 week2의 디렉토리를 가리키고 있는지 확인하고 아니면 cd/Documents/week2/day1/ 까지 억지로 데리고 온다. 또한, ls를 쳐서 readme.md 파일이 있는지도 확인하면 좋고
  - 그리고 github에서 이름을 작성하고, Public으로 지정한 후 create repository를 하면?
  - GIT bash에 입력하라고 많은 문구들이 뜬다 !
    - 여기서 맨 위에 echo 어쩌구 이거 작성하면 작성한 자료 다 날라간다.
    - 그 밑에 줄 git init부터 써주도록 하자. 별 탈 없으면 git add README.md도
    - 아마 git commit -m "first commit"에서 오류가 날 것이다. 왜냐 로그인을 안했거든 오류에 뜬거대로 git config --global user. email(아니면 name)을 모두 써주도록 하자. 만약 작성 후 아무것도 안뜨면 성공 !
    - 마지막으로 git remote를 작성하고 아무것도 뜨지 않는다면, git push 어쩌구를 작성하는데 여기서 github창이 뜨면서 로그인해라고 한다. 로그인 하도록하자. 그렇게 하면 나의 git hub에는 내가 공부한 자료가 업로딩 된다.

- GITHUB에 올린 자료 수정하기

  - 내가 만약 readme.md 파일을 수정하면 git은 이 변화를 파악하고 나한테 알려준다. 따라서 이 버전을 달리하고 다시 github에 올려야하는데 그 버전을 처음과 달리 "second commit"을 주도록 하자.
    - 즉, git add . (엔터) git commit -m "second commit" (엔터) 여기까지
  - 그 후 git push를 하면 수정된 버전의 자료를 github에 푸시푸시







https://github.com/sspy2/install_python