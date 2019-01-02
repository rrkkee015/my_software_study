## 2018-12-21

- ### 사람인 리쿠르팅 봇 만들어보기 !를 하기전에 어제 했던거 코드리뷰해보자

```python
@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')),methods=['POST'])
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req= request.get_json()
    chat_id = req["message"]["from"]["id"]
    msg = ''
    if(req["message"]["text"] == "안녕"):
        msg = "첫만남에는 존댓말을 써야죠!"
    elif(req["message"]["text"]=="안녕하세요"):
        msg = "인사 잘하신다 ㅋㅋㅋ"
    elif(req["message"]["text"]=="환율"):
        ext = exchange()
        print(ext)
        print("---------")
        msg=[]
        for i in ext:
            msg.append('{},{}'.format(i['name'],i['idx']))
        msg = "\n".join(msg)
    url = "https://api.hphk.io/telegram/bot{}/sendMessage".format(TELEGRAM_TOKEN)
    requests.get(url, params = {"chat_id":chat_id,"text":msg})
    return '', 200 #200은 정상적으로 처리 되었다는 코드임
```

각각이 뭐하는 역할을 하는지 알아보쟈.

```python
@app.route(/"{}".formate(token))
def telegram():
    
@app.rout("/set_wehook")
def set_webhook(): #웹훅을 URL(어제는 토큰에 등록을 했다.)에 등록하면 TELEGRAM 서버에 "야 ! TELEGRAM WEB에서 메시지 받으면 그때마다 C9으로 ALERT를 해줘"라고 하는 것이다. alert의 응답은 단지 200으로 주는거다. 근데 우리 사용자한테 200 보내는 걸 원하는게 아니니까 Sendmessage로 설정을 해야한다. "안녕", "야" 라는 응답에 요청할 수 있는 답변을 설정하면 내가 정해준 답변이 가는 것이다.
#왜 URL을 토큰으로 했을까? URL을 아무거나 해도 되는데, 남들이 알아보기 쉬운 것으로 하면 해킹을 하기 쉬우니까 알아보기 어려운 토큰으로 하는 것이다.
    
api.hhk.io/tele.../getUpdates #텔레그램 웹에서 텔레그램에 메시지를 보내고 c9에서 텔레그램에게 getupdates를 보내면 텔레그램에서 c9으로 메시지를 전달해준다. 하지만 이 짓을 일일이 하기 번거로우니 웹훅이라는 것을 하는 것이다.
```

telegram은 배열을 받아도 첫 번째 애만 뽑아낸다. 그럼 배열을 문자열로 바꿀때 어케하냐?

```PYTHON
str(list)도 되지만 잘 안먹음
'아무거나 적구'.join(list) 하면 리스트를 문자열 하나로 만들어준다.
```

1. params "chat ID" 설정을 안하면 메시지가 아예 안 감.  누가 보냈는지 파악을 해야 그 사람한테 답변을 할건데 "chat ID"가 없으면 그게 안 됨.

2. requests.get(url)이 정보를 얻어오는건데 데이터를 보내고 받아올 수 있는 애다. 주소창에 www.naver.com 주소창에 치는 것이 requests.get이라는 개념이다. 즉, 정보를 받는게 아니고 요청을 보내는거다. requests.get이 요청을 했기에 응답을 받는 것이다. 받는다는 개념은 머릿속에서 잊어버리자. requests는 기능 뭉탱이 request는 telegram url로 들어온 요청이다. 그니까 둘이 개념이 전혀 다름. 즉, requests는 요청을 보내는거다 !

   @app.route('/set_webhook')를 설정하고 주소창에 어쩌구저쩌구 /set_webhook을 치면 그 웹사이트로 날라가는데 @app.route('/set_webhook',methods=["GET"])에서 methods=["GET"]이 숨어있는거다.  아까 말한거 처럼 get이 주소창에 치는거랑 똑같은거니까 같은 개념으로 생각하면 된다. 이 방법을 달리하고 싶을 때 @app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')),methods=['POST'])처럼 달리하고 싶을 때 뒤에 따로 적어주는거다. 그니까 GET이 숨어있으니까 주소를 적을 때 항상 요청을 보내는 거지. 

- ### 사람인하지말고 방탈출카페를 긁어보자

1. 마스터키가 어느 지점을 가지고 있는지 알아보도록 하자. 우선 마스터키 사이트에 들어가서 예약하기 들어가서 지점 리스트를 보도록하자 그리고 오른쪽 클릭 후 페이지 소스보기를 통해 들어가서 ctrl + f로 원하는 지점을 찾도록 하자.

![](/image/2.png)

![](/image/1.png)

2. 그럼 여기서 escape_list안에서 escape_view를 긁으면 될거 같다. 별명이 다 있으니까.

![](/image/3.png)

​	요청에 대한 응답이 html로 오니까 beautifulSoup를 쓰자. 서울 이스케이프는 json 이다.

3. master_key.py를 day5 폴더에 만들어주고 master_key.py 파일의 기본 틀을 잡아주도록 하자.

   url은 변수는 veiw-source에서 찾은 정보를 지니고 있는 애를 network에서 찾아서 그 request 	URL을 찾도록하자.

![](/image/4.png)

![](/image/5.png)

​	이렇게 기본틀을 잡아주자

![](/image/6.png)

4. escape list라는 애를 먼저 뽑도록 하자. 별명이 class니까 .클래스이름이고 id인 경우엔 #id 이름을 해주면 된다.

![](/image/7.png)

5. 여기서 잠깐 많이 실수하는게 있는데 **escape_list**를 뽑게되면 **ul** 태그 시작부터 **ul** 끝날 때까지의 요소 한개를 뽑는다. **escape_view**까지 해줘야 li 태그부터 li 태그까지 하나 그리고 그 다음 **li** 태그부터 **li** 태그까지 하나해서 모두 다 뽑아준다.

![](/image/8.png)

![](/image/9.png)

​	여기서 lis가 배열이 된다는것을 기억하고 lis를 for문으로 순회를 하면서 원하는 정보를 솎아내는 작업을 하도록하자.

6. 잠깐 근데 li 태그 안에 p 태그는 부천점 하나밖에 없네? 그럼 p태그를 바로 뽑으면 부천점이 나온다.

![](/image/10.png)

​	그러면 밑에 처럼하면

```python
for li in lis:
    print(li.select('p'))
```

​	결과가 지점 이름으로 쫙 나온다.

![](/image/11.png)

​	근데 좀 이상하게 나오네? 뒤에 .text를 붙여주면 해결된다. **근데 여기서 중요한 점 ! 우리가 하나만 뽑는데도 select_one 혹은 select('p')[0].text을 해줘야 값이 먹힌다.**

![](/image/15.png)

7. 또 우리가 원하는건 주소랑 연락처를 뽑도록하자

![](/image/12.png)

![](/image/13.png)

8. NEW 근데 거슬리네 ? NEW 빼보자

![](/image/14.png)

​	어차피 문자열이니까 배열일테고 그 뒤에 NEW의 3가지 배열을 제거해주면 된다.

```PYTHON
title=li.select_one('p').text #부천점NEW라고 생각하자.
    if(title.endswith('NEW')):
        title = title[:-3]
```

9.  그렇다면 다 정리가 되었으니 변수선언을 하도록하자.

![](/image/16.png)

​	여기서 link 자세히 보자

![](/image/18.png)

​	우리가 원하는건 a 안에 herf 값이다. 그럴 땐 a 태그 0번째 href value값을 찾으면 된다. 즉 dict value 값 찾듯이 찾으면된다.

​	그리고 링크에는 항상 'http://www.master-key.co.kr'을 붙여줘야한다.

![](/image/20.png)

10. 이제 코드를 완성시켜주자

![](/image/21.png)

​	이걸 출력해보면?

![](/image/22.png)

11. 이제 예약하기를 크롤링해보자

    우선 필요한 정보가 태그가 되어 있을텐데 그 바깥 쪽부터 좁혀들어오도록 하자.

    다른거 없이 ul태그안에 li태그 있고 li 태그 하나하나가 새로운 테마 정보가 있는거다.

    일단 reserve라는애가 가장 바깥쪽이고 escape_view가 내가 원하는 정보를 가진 애다.

![](/image/23.png)

12. 자 그러면 Request URL을 가져와야하는데 예약 날짜가 안적혀있네? 

![](/image/24.png)



​	그러면 어떻게 알 수있을까? get 방식에서는 원하는 날짜 정보와 파라미터가 URL에 다 붙어있어서 ?찍고 파라미터 명, 파라미터 값 넣데 POST에는 파라미터 정보가 숨겨져 있다.

맨 밑에 Form Data에 있다.

![](/image/26.png)

​	params 변수를 따로 만들어주고 date랑 store를 넘겨주도록하자.

​	그런 다음에 response 변수에 담으면 된다.

![](/image/25.png)

13. 자 그러면 정보를 다 받았는데 이 정보를 솎아내보자. 일단, bs로 'html parser'를 써서 html 형식으로 받아오고 document에 담자.

```python
document=bs(response,'html.parser')
```

​	그 다음 여기서 아까처럼 ul 에 select를 이용해서 document에 있는 정보를 거르자. 

```python
ul=documet.select('.reserver') 
```

​	근데 이러면 요소하나가 나온다. 따라서 escape_view를 써서 범위를 좁혀주자

```python
ul=documet.select('.reserver .escape_view')
```

​	이제 요소 하나를 for 문으로 돌면서 title를 뽑고 예약 정보를 뽑도록하자. col 이라는 애가 예약정보를 가지고 있다.

![](/image/27.png)

​	 그리고 p 태그로 뽑아보면 p태그 첫번째가 테마명이고 2번째가 잡다한 정보 3번째가 예약관련이다.

![](/image/28.png)

​	그렇다면 첫번째 p태그만 솎아내면 title을 모을 수 있다.

```python
for li in ul:
    title = li.select_one('p').text
```

​	그런 다음 예약 정보는 col 안에 있고 p태그 안에 time, state가 물고있다. 이걸 어떻게 속아낼까?

​	join이라는 함수를 써서 한 줄에다가 한 타임의 정보씩 넣어보도록 하자.

​	우선 col이라는 애를 출력을해보자

```python
for li in ul:
    title = li.select_one('p').text
    print(li.select('.col')) # 클래스니까 .이 붙는다.
```

​	보면 리스트 형식으로 되어있다. 그러니 리스트를 순회를 하면서 class 타입인 time과 state를 골라내어 출력을 하면 되겠다 !

![](/image/29.png)

```python
for col in li.select('.col'):
    print(col.select_one('.time').text) # 시간을 다 솎아냈다.
    print(col.select_one('.state').text) # 예약가능 상황을 솎아냈다.
```

14. 여기까지 했으면 저 정보는 info라는 변수를 만들어서 담기로 하고 title도 솎아내서 이것을 한번에 출력해주는 친구를 만들어보자

```python
for li in ul:
    title = li.select_one('p').text
    info = ''
    for col in li.select('.col'):
        info = info + '{} {}\n'.format(col.select_one('.time').text,col.select_one('.state').text) #이러면 시간이 붙는다.
    theme = {
        'title' : title,
        'info' : info
    }
    theme_list.append(theme)
    print(theme_list)
```

​	**여기서 잠깐!!!!!**

```python
파이썬 3.0 이후부터 i.keys()로 출력을하면 dict_keys 타입으로 출력된다 그러기 때문에 이걸 편하게 사용하려면 list를 만들어야 하는데

list(i.keys())로 출력을 하면 list 형식으로 깔끔하게 출력된다.

a=[]
a={'b':1,'c':2,'d':3}
print(a)
print(a.keys())
print(a.values())
print(list(a.keys()))

결과값
{'b': 1, 'c': 2, 'd': 3}
dict_keys(['b', 'c', 'd'])
dict_values([1, 2, 3])
['b', 'c', 'd']
```

​	여기까지 했으면 함수 지정을 해주자

```python
def master_key_info(cd):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    requests.post(url)
    params = {
        'date' : '2018-12-22',
        'store' : cd # 어디지점인지 알려준다
    }
    response = requests.post(url, params).text
    document=bs(response,'html.parser')
    ul=document.select('.reserve .escape_view')
    theme_list = []
    for li in ul:
        title = li.select_one('p').text
        info = ''
        for col in li.select('.col'):
            info = info + '{} {}\n'.format(col.select_one('.time').text,col.select_one('.state').text) #이러면 시간이 붙는다.
        theme = {
            'title' : title,
            'info' : info
        }
        theme_list.append(theme)
    return(theme_list)
```

15. 우리 근데 store에 숫자 있잖아. 근데 그거 우리가 일일이 하기 싫으니까 숫자를 가져다가 자동으로 뽑을 수 있게 만들어주자. 그 숫자는 링크에 붙어있다. 그럼 그 숫자를 어떻게 솎아낼까??

![](/image/30.png)

```python
#파이썬의 스플릿을 사용하자. join의 반대되는 경운데 split은 문자열을 리스트로 솎아낼 수 있다.
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> a = "a:b:c:d"
>>> a.split(':')
['a', 'b', 'c', 'd']

#짠
#join은 이거임
>>> a= ","
>>> a.join('abcd')
'a,b,c,d'
>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'
```

​	리스트 개념을 알겠으면 이제 솎아내보자 지금 이 master_key_list 자체가 리스트로 되어있으니 for문을 돌려서 숫자를 솎아낼 수 있게 해보자. 밑에 얘는 우리가 쓸건 아니고 그냥 솎아내는 방법을 적어놓은거다.

![](/image/31.png)

그럼 이제 솎아낸 숫자를 어떻게 넣을까??? 함수 매개변수를 이용해서 넣으면 된다. 저 괄호 안에 숫자를 넣으면 그  cd가 스토어 변수에 들어가게 된다.

![](/image/32.png)

마지막에 print에서 return으로 봐꿨다. 이렇게 하면 master_key_list()를 실행하면 이 함수 값을 돌려준다. print(master_key_list())을 하면 함수 값을 볼 수 있다.

```python
def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document=bs(response,'html.parser')
    lis = document.select('.escape_list .escape_view') #lis는 배열이다.
    cafe_list=[]
    for li in lis:
        title=li.select_one('p').text
        tel = li.select('dd span')[1].text
        address = li.select('dd span')[0].text
        link = 'http://www.master-key.co.kr' + li.select('a')[0]["href"]
        if(title.endswith('NEW')):
            title = title[:-3]
        cafe = {
            'title': title,
            'tel' : tel,
            'address': address,
            'link': link
        }
        cafe_list.append(cafe)
    return cafe_list # master_key_list() 함수에요청을 했으니 반환해야하잖아. return이 그 뜻이다.
```



16. 이제 챗봇을 설정해보자.

```python
# 사용자로부터 '마스터키 ***점'이라는 메시지를 받으면
# 해당 지점에 대한 정보를 요청하고(크롤링)
# 메시지(예약정보)를 보내준다.
```

우선 만든 마스터키 함수들을 전부 telegram app.py에 넣어주자. 그런 다음 내가 챗봇에 마스터키라고 치면 지점을 솎아낼 수 있도록 만들어주자.

![](/image/35.png)

저기 밑에 주석으로 설명한 부분 잘 읽어보자

아 ! 그리고 그 카페리스트도 복사해서 넣어주도록 하자. 제일 위에 "전체도 적어주도록하자"

![](/image/36.png)

```python
from flask import Flask, request
from bs4 import BeautifulSoup as bs
import requests
import json
import time
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_URL = 'https://api.hphk.io/telegram' #바로 텔레그램으로 신호를 주는게 아니고 우회하는 코드

CAFE_LIST = {
"전체" : -1,
"부천점":15,
"안양점":13,
"대구동성로2호점":14,
"대구동성로점":9,
"궁동직영점":1,
"은행직영점":2,
"부산서면점":19,
"홍대상수점":20,
"강남점":16,
"건대점":10,
"홍대점":11,
"신촌점":6,
"잠실점":21,
"부평점":17,
"익산점":12,
"전주고사점":8,
"천안신부점":18,
"천안점":3,
"천안두정점":7,
"청주점":4
}


def exchange():
    url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
    response = requests.get(url).text
    soup = bs(response,'html.parser')
    li = soup.select('tbody tr')
    prices = []
    count = 0
    for item in li:
        price = {
            "name" : item.select('td a')[0].text,
            "idx" : item.select('td')[1].text
            }
        prices.append(price)
    for i in prices:
        print(i['name'])
        print(i['idx'])
        count += 1
    return prices
    
def master_key_info(cd):
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    requests.post(url)
    params = {
        'date' : time.strftime("%Y-%m-%d"), #매일매일 업그레이드과 되야하니까 time 함수를 쓸거다 !!!
        'store' : cd # 어디지점인지 알려준다
    }
    response = requests.post(url, params).text
    document=bs(response,'html.parser')
    ul=document.select('.reserve .escape_view')
    theme_list = []
    for li in ul:
        title = li.select_one('p').text
        info = ''
        for col in li.select('.col'):
            info = info + '{} {}\n'.format(col.select_one('.time').text,col.select_one('.state').text) #이러면 시간이 붙는다.
        theme = {
            'title' : title,
            'info' : info
        }
        theme_list.append(theme)
    return(theme_list)
            
def master_key_list():
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document=bs(response,'html.parser')
    lis = document.select('.escape_list .escape_view') #lis는 배열이다.
    cafe_list=[]
    for li in lis:
        title=li.select_one('p').text
        tel = li.select('dd span')[1].text
        address = li.select('dd span')[0].text
        link = 'http://www.master-key.co.kr' + li.select('a')[0]["href"]
        if(title.endswith('NEW')):
            title = title[:-3]
        cafe = {
            'title': title,
            'tel' : tel,
            'address': address,
            'link': link
        }
        cafe_list.append(cafe)
    return cafe_list # master_key_list() 함수에요청을 했으니 반환해야하잖아. return이 그 뜻이다.

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')),methods=['POST'])
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    req= request.get_json()
    chat_id = req["message"]["from"]["id"]
    msg = ''
    txt = req["message"]["text"]
#    if(req["message"]["text"] == "안녕"):
#        msg = "첫만남에는 존댓말을 써야죠!"
#    elif(req["message"]["text"]=="안녕하세요"):
#        msg = "인사 잘하신다 ㅋㅋㅋ"
#    elif(req["message"]["text"]=="환율"):
#        ext = exchange()
#        print(ext)
#        print("---------")
#        msg=[]
#        for i in ext:
#            msg.append('{},{}'.format(i['name'],i['idx']))
#        msg = "\n".join(msg)
    if(txt.startswith('마스터키')): # startwith은 txt 문자열에 마스터키로 시작하는 문자열이 있나 없나 확인하는거
        if txt.split(' ')[1] in CAFE_LIST.keys(): # dict_kyes 형식도 리스트 인식이 되는가보다
                
            cafe_name = txt.split(' ')[1] # 마스터키로 시작하는 문자열이 있다면 지점만 뽑아낸다. 왜냐 내가 (마스터키 부천점)을 검색하면 빈칸 뒤에 부천점이 뽑혀지니까.
            cd = CAFE_LIST[cafe_name]
            if (cd>0):
                data = master_key_info(cd)   
            else:
                data = master_key_list()
            msg=[]
            for d in data:
                    msg.append('\n'.join(d.values()))
            msg ='\n'.join(msg)
        else:
            msg = txt.split(' ')[1] + "은 사랑입니다."
    else:
        msg = "?"
        #마스터키 전체
        #마스터키 ****점
        
    url = "https://api.hphk.io/telegram/bot{}/sendMessage".format(TELEGRAM_TOKEN)
    requests.get(url, params = {"chat_id":chat_id,"text":msg})
    return '', 200 #200은 정상적으로 처리 되었다는 코드임

@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL +'/bot' + TELEGRAM_TOKEN + '/setWebhook'
    params = {
        'url' : 'https://week2-rrkkee015.c9users.io/{}'.format(TELEGRAM_TOKEN)
        }
    response = requests.get(url, params = params).text
    return response
```

이렇게 하면은 내가 텔레그램에서 마스터키 부천점을 치면 시간을 알려준다.

![](/image/37.png)



- 서울 이스케이프도 한번 해보도록 하자

1. url 복사했어 근데 파라미터 빼고 복사했어 우리가 파라미터를 넣어보쟈, 그리고 하던대로 틀 잡아주자

![](/image/38.png)

2. 이 이상은 내가 기가막히게 정리했지만 공간이 부족해서 적지 않겠다.

