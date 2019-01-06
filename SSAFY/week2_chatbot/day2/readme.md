복습

- python 문법

  - 저장

    - 저장할 땐 = 하나, 변수 내용엔 "글자", 숫자, True/False가 들어갈 수 있다.
    - [리스트], {딕셔너리} 형태가 있다.

  - 조건

    ```python
    #기본형
    if(비교문):
        실행문
    elif(비교문):
        실행문
    else(비교문):
        실행문
    ```

  - 반복

    -  While, for i in List, Dictionary

- 오픈소스

  - 제작자의 권리를 지키면서 누구나 열람가능한 공개된 (소스)코드

- API

  - 응용 프로그램 간의 대화 방식 (서로 정해진 규칙에 따라서 정보를 주고 받음)
  - Request URL로 정보를 보내야 걔들이 응답을 해준다.
    - Request Method가 있는데 이거는 내일 설명하겠다.

## 2018 - 12 - 18

-  **로또 번호 만들기**

  ```python
  import random
  import requests
  from bs4 import BeautifulSoup
  
  url = 'https://m.dhlottery.co.kr/common.do?method=main' 
  response = requests.get(url).text #url 주소에 요청을 넣고 그 정보의 텍스트를 응답 받음, text를 적지 않으면 그냥 응답 200 혹은 404로 온다.
  soup = BeautifulSoup(response, 'html.parser') #문서를 보기 좋게 만들어 주는 것이 BeautifulSoup이다. 뒤에 인자는 어떤 인자인지에 따라서 방향을 다르게 잡아주는 애이다. (html, xml, json 등이 있다.)
  document = soup.select('div.prizeresult')[0] #뽑아온 요소에서 첫번째만 낼름
  # print(document) # 이거 [0] 없애고 출력해보면 리스트 방식으로 나오는데 전 주, 전전 주의 로또 번호가 같이 나온다. 그 중 첫번째 정보가 우리가원하는 금주의 로또 번호다.
  # 작성시 따옴표를 잊지 맙시다.
  # div라는 이름을 가진 애한테 prizeresult라는 별명을 준거고 그 별명의 종류가 class이다. <div class="prizeresult">
  # 혹은
  # document = soup.select('.prizeresult') 해도 된다.
  # 클래스를 찾을 땐 .하고 별명을 적는다. id일 땐 #하고 별명을 적는다.
  # document = soup.select('#slick-slide01 > div.prizeresult > div:nth-child(1)')를 출력하면 빈 [] 괄호가 나온다. 걱정하지말고 사이트에서 찾아보면 됨
  numbers = document.select('span')
  # 그냥 print(numbers)를 해버리면 [<span>2</span>, <span>25</span>, <span>28</span>, <span>30</span>, <span>33</span>, <span>45</span>, <span>6</span>] 이렇게 뜬다. 그래서 각각의 인덱스를 정해줘서 그 숫자를 끄집어 내야한다. print(numbers[0].text) 이렇게
  
  a=[] # a 초기화 해주기
  for i in range(1,46):
      a.append(i)
  print(a) # 1~45 a 출력
  
  # append를 썼는데 강사님은 python long array / make number array를 사용했다.
  # python range to list라는 친구를 검색했다.
  # 검색을 할 땐 처음엔 무조건 내가 사용하는 언어를 먼저 작성하고 내가 묻고 싶은걸 적는다.
  # lotto = []
  # for i in range(45):
  # 	lotto.append(i+1)
  # print(lotto)
  # 혹은
  # lotto2 = list(range(1,46)) # 이게 더 간단하네요.
  # print(lotto2)
  
  lotto = random.sample(a,6) # a에서 비복원추출을 해서 6개 뽑는다.
  lotto.sort() # 오름차순으로 정렬
  print(lotto)
  
  # 내림차순은 reversed라는 함수를 쓰는데 얘 하고 나서 리스트로 한번 더 감싸줘야함.
  
  #c=reversed(lotto)
  #print(c) # 이러면 에러야.
  #print(list(c)) # 이러면 정답.
  
  # 로또 홈페이지에서 가져온 번호를 정렬하고 문자형이니 숫자로 바꾸자.
  ns = []
  for i in numbers:
      ns.append(int(i.text)) # .text가 없으면 [<span>2</span>, <span>25</span>, <span>28</span>, <span>30</span>, <span>33</span>, <span>45</span>, <span>6</span>] 이렇게 뜬다 
  ns.sort()
  print(ns) # 이거 어려우니까 한번 더 챙겨보자
  
  # 이제는 내가 랜덤으로 돌린 숫자와 로또 홈페이지에서 가져온 번호를 비교하고 몇개나 맞췄는지 해보자.
  # 지난 주 당첨 숫자 리스트을 한번씩 순회하면서
  # 내가 뽑아놓은 lotto 배열에서
  # 몇개가 맞았는지 카운트하기
  result = 0
  for i in ns:
    for j in lotto:
      if j == i:
        result += 1
  print(result)
  # 이렇게 해도 되고 리스트 두 개를 비교해서 각각의 정보를 맞나 다르나 할 땐 간단하게 표현이 가능하다.
  # 그 구조는 if item in my_list의 구조이다.
  # 즉,
  # for i in ns # i의 리스트 하나하나가 lotto로 데리고가서 얘랑 같은 애 있나 확인하고 계속 빙글빙글
  # 	if i in lotto: # ns 리스트의 정보가 lotto에 있으면 result를 하나 올린다.
  # 		result += 1
  # print(result)
  # 로 간단하게 표현가능하다.
  # 코딩할 때 키보드 부터 잡지말고 어떻게 알고리즘을 돌릴 지 생각을 해야한다.
  ```

  근데 이걸 내가 출력 했을 때 몇 개 맞췄는지 궁금하지 않아?

  - 우선 구글에 로또번호 확인에서 동행복권을 들어가보자
  - 거기서 F12 들어가서 로또 번호를 찾자. 



- **미세먼지**

  ```python
  import requests # requests import를 통해 기능을 불러온다.
  from bs4 import BeautifulSoup #내장, 외장이 아닌 from bs4는 사람이 만든 특수한 라이브러리에서 가져오는 것이다.
  
  url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&ServiceKey={}&ver=1.3&pageNo=3'.format(key)
  # 정보의 주소를 url이란 변수에 담았다.
  
  response = requests.get(url).text # requests라는 기능에서 get이라는 기능을 끄집어내서 씀. get은 url에다가 요청을 보내는 것. .text는 내용물을 보여달라는 뜻. 즉, requests 기능 중에 요청을 보내는 get 기능을 씀. 갔으니 응답이 오는데 응답을 .text를 통해 내용물만 response에 담았다. 이 형태는 계속 쓸거니 기억해두기
  
  soup = BeautifulSoup(response, 'xml') # BeautifulSoup(문서,문서 종류)는 함수를 실행하는 형태. 앞에서 정의된 response를 매개변수로 씀. xml은 어떤 형태를 나타낸다. html도 있고 xml도 있는데 별로 의미없다. xml 문서를 받았으니 xml 쓴거고 html 문서를 받으면 html을 쓴다. 자세한건 밑에 사진 참고. BeautifulSoup 함수는 문서 찾을 때 ctrl + F 하는 거처럼 그 역할을 한다. 즉, 이 함수는 어떤 xml 문서를 검색하기 쉽게 만들어주는 함수이다.
  
  gn = soup('item')[7] # 문서에서 ctrl + F로 item으로 검색하여 파일 찾음. 그 중에 7번째 애를 찾음.
  
  location = gn.stationName.text # 7번째 아이템에서 stationName에서 필요한 value를 뽑아내고 location에 담은거입니다.
  time = gn.dataTime.text
  dust = int(gn.pm10Value.text)
  
  print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))
  
  # 조건문
  condition = ""
  if dust > 150:
    condition="매우 나쁨"
  elif 80 < dust <= 150: # elif (dust > 80 and dust <= 150):  
    condition="나쁨"
  elif 30 < dust <= 80: # elif (dust > 50 and dust <= 80):
    condition="보통"
  else:
    condition="좋음"
  
  print("오늘의 미세먼지 농도는 %s 입니다."%condition)
  print("오늘의 미세먼지 농도는 "+ condition +" 입니다.")
  ```

  위에 response print 해봤을 때 결과 

  ![위에 response print](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음.png)

  잘 보면 <mangName>으로 열었고 </mangName>으로 닫았다. 다른 것도 마찬가지로 열고 닫고 한것이 같다. xml은 태그를 마음대로 정할 수 있고, html은 정해진 태그를 사용한다.

  위에 soup('item')를 프린트 한 결과

  ![](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음2.png)

  item으로 시작하고 item으로 닫은 자료가 리스트 형식으로 나와있다.

- **다음 코스피 (미세먼지 참고해서 작성 중)**

  ```python
  import requests as req # 이제 requests 풀 네임 안써도 req 써도 됨
  from bs4 import BeautifulSoup as bs # 이제 BeautifulSoup를 bs로 써도 됨
  
  url = 'http://finance.daum.net/' # 요청을 보낼 홈페이지
  response = requests.get(url).text # url을 요청하고 내용물 낼름 훔쳐왔다.
  soup = BeautifulSoup(response, 'html.parser') # bs로 해도됨, xml이 아니고 html로 하고 특이하게 parser를 붙혀준다.
  kospi = soup.select('#boxIndexes') # soup에서 찾아야하는데 다음 금융 들어가서 F12 눌러서 복사해오자 사진참고, select를
  ```

  다음 금융에서 kospi 정보를 가져옴

  ![](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음3.png)

  근데 다음 이 시키들 곱게 정보를 주질 않는다. 우리가 보는 홈페이지는 정보를 보여주는 틀이고 정보를 보내는 곳은 따로 있다.

  여기임 저기에 2071.3 적힌게 정보다.![](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음4.png)


- 집에서 멀티캠퍼스까지 오는 가장 빠른 길 (알고리즘 예시)

  1. 지하철

     1-1. 집에서 가장 가까운 역으로 간다.

     1-2. 멀티캠퍼스 방향으로 가는 플랫폼에 선다.

     1-3. 가장 먼저오는 지하철을 탄다.

     1-4. 역삼역에 도착한다.

  2. 버스

     2-1. 가는 버스가 어디있는지 검색한다.

     2-2. 버스 정류장에서 212번 버스를 기다린다.


  - 자 보듯이 알고리즘 짜는게 어려운 것이 아니고, 생각을 정리한 다음 그 생각을 코딩을 하는 것이 어려운거다. 그니까 문제를 받으면 바로 키보드로 옮기지 말고 A4 용지에 어떻게 문제를 풀어갈지 단계를 적어야한다.

- 네이버 웹툰

  ```python
  #링크를 따오는 애를 만들어 보겠다 ! (어플 필요없고, 내가 원하는 거만 모아모아 볼 수 있다.)
  
  import requests
  import time # 타임이라는 외장함수를 불러와서 오늘이 무슨 요일인지 파악한다.
  from bs4 import BeautifulSoup
  
  # 1. 네이버 웹툰을 가져올 수 있는 주소를 파악하고 url에 저장한다.
  # 2. 해당 주소로 요청을 보내어 응답을 가져온다.
  # 3. 받은 정보를 BeautifulSoup를 통해 검색하기 좋게 만든다.
  # 4. 네이버 웹툰 페이지로 가서 내가 원하는 정보가 어디 있는지 파악한다.
  # 5. 내가 원하는 정보는 만화 링크이다.
  # 6. 3번에서 저장한 무너를 이용해 번에서 파악한 위치를 뽑아내는 코드를 작성한다.
  # 7. 출력한다.
  today = time.strftime("%a").lower() # 매일 컴퓨터 시간 읽고 그 날의 요일에 맞는 today 값을 가져온다.
  # 1. 네이버 웹툰을 가져올 수 있는 주소를 파악하고 url에 저장한다.
  url = "https://comic.naver.com/webtoon/weekdayList.nhn?week={}".format(today)
  # 2. 해당 주소로 요청을 보내 응답을 가져온다.
  response = requests.get(naver_url).text #.text를 하지 않으면 200만 온다.
  # 3. 받은 정보를 BeautifulSoup를 통해 검색하기 좋게 만든다.
  soup = BeautifulSoup(response,'html.parser')
  # 4. 네이버 웹툰 페이지로 가서 내가 원하는 정보가 어디 있는지 파악한다.
  toons = [] # class 혹은 id로 찾거나 <>로 찾는다. 이름 이미지 주소가 다 필요하니까 딕셔너리로 정의한다.
  #li = soup.select('.img_list') #밑에 스크린샷을 참고해보면 li 하나마다 각각의 만화를 담고있다. 이렇게 print(li) 실행하면 ,가 나오지 않아서 배열로 정리되지 않는다.
  li = soup.select('.img_list li') #이렇게 실행하면 ,가 출력되면서 배열로 정리된다.
  for item in li:
      toon = {
          "title":item.select('dt a')[0].text, #클래스 id 같이 별명 없으면 그냥 dt 태그 a 태그 적으면 됨 #여기까지가 title 구하기 위한 것임.
          "url": item.select('dt a')[0]["href"], # 속성을 뽑아내는건 딕셔너리 뽑 듯이 뽑으면 된다.
          "img_url": item.select('.thumb img')[0]["src"] # select는 리스트로 출력하기 때문에 [0]이 꼭 필요하다.
      }
      toons.append(toons)
  print(toons)
  
  ```

  li가 만화 하나 하나를 각자 담고 있다.

  ![](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음6.png)

  왜 dl dt a를 안하는지 설명해주는 스크린샷

  ![](C:\Users\student\Desktop\동훈\스크린샷\week2_day2\제목 없음7.png)					

- 다음 웹툰

  ```python
  import requests
  import time
  import json
  from bs4 import BeautifulSoup as bs # json의 자료는 BeautifulSoup로 읽을 수 없다.
  
  # 내가 원하는 정보를 얻을 수 있는 주소를 url의 변수에 담는다.
  url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/tue'
  	# http://webtoon.daum.net/data/pc/webtoon/list_serialized/tue?timeStamp=1545117074222 여기서 timeStamp는 필요없다.
      # F12에서 Network 그리고 tue?에서 Request URL을 복사 붙여넣기 한다.
      # 속도를 Slow 3G를 놓고 새로고침을 해보면 중요한 애들부터 뜨게 되어있다. 그 중에 내가 원하는 정보를 쏙쏙 들고있는 애의 URL을 복사하는 것이 관건이다.
  
  # 해당 url에 요청을 보내 응답을 받아 저장한다.
  response = requests.get(url).text # 문자열임
  
  # 구글에게 python으로 어떻게 json을 파싱(딕셔너리 형으로 변환)하는지 물어본다.
  # 파싱한다. (변환한다.)
  document = json.loads(response) # 문장열을 json.loads로 하면 딕셔너리로 됨
  
  # 내가 원하는 데이터를 꺼내서 조합한다.
  data = document["data"] #dat는 배열이되고 "data" 한거는 딕셔너리에 있는 애를 끄집어 내는거니까.
  
  toon = []
  for toon in data:
      print(toon["title"])
  	print(toon["pcThumbnailImage"]["url"])
      	print("http://webtoon.daum.net/webtoon/view/{}".format(toon["nickname"]))
  ```

- **여기서 잠깐**

  XML은 지 맘대로 태그명을 바꿀 수 있지만, HTML은 정해진 태그명을 사용하기에 앞에 div, dl, dd 이런 애들이 따라온다. 그리고 json 같은 경우는 dictionary 구조를 가지기 때문에 구분이 가능하다.

- **예습**

  https://www.codecademy.com 에서 HTML 태그 설명을 볼 수 있는 4시간짜리 강의 ㅎㅎ.. ㅠㅠ

  여기서 Introduction to html을 듣자.

- **GIT day2 넣기**

  cd /document/week2/day2 에서 git init을 하면 숨김 폴더가 하나 생긴다.

  git add . = 변화 감지된 파일을 정리함

  git commit -m "first commit" = 버전을 나타낸다.

  git remote add origin https://github.com/rrkkee015/week2_day2.git = GIT과 GIT HUB는 다른거다. 따라서 원격으로 저장하기 위해서 이 타이핑을 한다.

  git push = 파일을 github로 푸시푸시베이베

  touch = 파일을 만든다