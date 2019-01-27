# 프로젝트 1 - 영화 정보 csv 만들기

> 01/18 금요일 프로젝트 1회차

### 파일 조작

- file 이란?
  - file이란 영구 저장 방법 또는 매체라고 부른다. 딕셔너리나 리스트에는 아무리 많이 넣어도 파이썬 파일이 꺼지면 사라진다. 디스크, 스토리지 라는데 들어가서 영구적으로 저장되는 것이 파일이다.
  - 컴퓨터는 계산과 저장을 하는 친구이다. CPU는 계산을, RAM은 기억과 저장을 한다. 그런데 얘는 임시적으로 저장하는 친구라 저장 파트에 DISK라는 저장소가 따로 있다. 얘는 컴퓨터가 꺼지더라도 데이터가 남아있다.

> file.py

```python
movies = ["말모이","랄프","아쿠아맨","짱구 극장판 쿵푸"]
```

이러한 데이터가 파이썬에 들어있다면 파일을 열고 닫아야 할 것이다. 그래서 파이썬 파일 조작을 검색하면 예시가 많이 나온다.

> file.py

```python
f = open("a.txt")
f.close()
```

이 파일을 콘솔에서 사용해보자. 아마 에러가 뜰 것이다.

> console

```python
$ python3 file.py
FileNotFoundError: [Errno 2] No such file or directory: 'a.txt'
```

파일 열기모드를 추가 안했기 때문이다. 따라서 아래 중 한 애를 골라서 추가를 해야한다. 참고로 a는 리스트의 append를 생각해보면 된다.

| 파일열기모드 | 설명                                                       |
| ------------ | ---------------------------------------------------------- |
| r            | 읽기모드 - 파일을 읽기만 할 때 사용                        |
| w            | 쓰기모드 - 파일에 내용을 쓸 때 사용                        |
| a            | 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용 |

> file.py

```python
movies = ["말모이","랄프","아쿠아맨","짱구 극장판 쿵푸"]

f = open("a.txt")
f.write("wow this is file!" + "\n")
f.close()
```

파이썬 파일이라는 객체가 쓸 수 있는 메소드, 기능을 확인하려면 다음과 같이 작성해보면 된다.

> file.py

```python
f = open("a.txt","a")
print(dir(f))
f.close()
```

> console

```python
$ python3 file.py
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
```

목록 중에 read를 써 보도록 하자

> file.py

```python
f = open("a.txt","a")
print(f.read())
f.close()
```

> console

```python
$ python3 file.py
io.UnsupportedOperation : not readable
```

여기서 오류 메시지가 뜨는 이유론 옵션에 'r'로 변경 안해줬기 때문이다.

> file.py

```python
f = open("a.txt","r")
print(f.read())
f.close()
```

콘솔 창에 입력을 해보자. 리눅스 명령어 cat a.txt랑 비슷하다.

> console

```python
$ python3 file.py
wow this is file!wow this is file!
$ cat a.txt
wow this is file!wow this is file!
```

우리가 원하는 내용도 적을 수 있다.

```python
content = "this is content"

f = open("b.txt","a")
f.write(content)
f.close()
```

이렇게 하면 b.txt에 해당 변수의 내용이 들어간다.

데이터를 저장할 때, 엑셀에서 열 수 있는 csv라는 친구를 쓰게 된다. 엑셀이란 파일이 무거운 편이지만 얘는 텍스트 데이터라서 파싱도 쉽고, 파일이 작아서 많은 데이터를 넣을 수도 있다.

movies 리스트에 저장해 둔 것을 file로 저장하고 싶으면 다음과 같이 쓰려고 할 것이다.

> file.py

```python
movies = ["말모이","랄프","아쿠아맨","짱구 극장판 쿵푸"]

f= open("c.txt","a")
f.write(movies)
f.close()
```

> console

```python
$ python3 file.py
TypeError : must be str, not list
```

오류가 떴다. for 문으로 안에 있는 내용을 적도록 해보자

> file.py

```python
movies = ["말모이","랄프","아쿠아맨","짱구 극장판 쿵푸"]
f = open("movies.txt","a")
for movie in moviese:
    f.write(movie)
f.close()
```

> console

```python
$ python3 file.py
```

결과물을 확인해보면 다음과 같다.

> movies.txt

```python
말모이랄프아쿠아맨짱구 극장판 쿵푸
```

띄어쓰기로 구분을 지어보자

> file.py

```python
f = open("movies.txt", "w")
for movie in movies:
    f.write(movie+",")
f.close()
```

> movies.txt

```python
말모이,랄프,아쿠아맨,짱구 극장판 쿵푸,
```

저장한 데이터를 이제 하나하나 읽어와서 다시 리스트를 만들도록 해볼 것이다. print(type(f.read()))를 해보면 str타입이라고 나온다.

> file.py

```python
f = open('movies.txt','r')
print(f.read().split(","))
f.close()
```

> console

```python
$ python3 file.py
['말모이', '랄프', '아쿠아맨', '짱구 극장판 쿵푸', '']
```

txt파일은 불편한게 많기에 우리는 csv 파일을 많이 사용하게 될 것이다.

> csv_practice.py

```python
lunch = {
    '김밥카페' : '02-1234-5678',
    '양자강' : '02-2345-6789',
    '순남시래기' : '02-9876-5432'
}

f = open("lunch.csv",'w')
for name in lunch:
    f.write("{},{}\n".format(name, lunch[name]))
f.close()
```

> lunch.csv

```python
김밥카페, 02-1234-5678
양자강, 02-2345-6789
순남시래기, 02-9876-5432
```

f열고 닫는 걸 한 줄로 줄이는 with 이라는 컨텍스트를 활용할 것이다. (f.close()를 신경 쓰지 않아도 된다)

> csv_practice.py

```python
lunch = {
    '김밥카페':'02-1234-5678',
    '양자강':'02-2345-6789',
    '순남시래기':'02-9876-5432'
}

with open('lunch.csv','w') as f:
    for name in lunch:
        f.write("{}, {}\n".format(name,lunch[name]))
#		  f.write(",".join([name,lunch[name]) + "\n")
```

csv를 쉽게 쓰고 읽기 위해서 편안하게 조작할 수 있다. csv 모듈을 불러와서 편리하게 쓸 것이다.

csv.writer의 인자로 file을 넣어준다. 이렇게 리스트형 자료형도 그대로 받아서 넣기만 하면 돼서 csv 파일들을 쓰게 되는 것이다.



### 리스트를 가지고 csv를 만들 때 (writer.writerow -> 리스트를 인자)

> csv_practice.py

```python
import csv
menu = ['김밥','탕수육','시래기']
with open('lunch.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(menu)
```

> lunch.csv

```python
김밥,탕수육,시래기
```

딕셔너리도 넣고 싶다면 dict_wirte를 쓰면된다. 대신 filed를 정해주어야한다.

> csv_practice.py

```python
import csv
lunch2 = {
    '상호명':'양자강'
    '전화번호':'02-2345-6789'
}
with open('lunch.csv','w') as f:
    filed = ('상호명','전화번호')
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheeader()
    writer.writerow(lunch2)
```

> lunch.csv

```python
상호명, 전화번호
양자강, 02-2345-6789
```

실제로 우리가 사용하는 데이터는 이런 식으로 여러 개가 담기게 될 것이다.



### 딕셔너리를 가지고 csv를 만들 때 (DictWriter.writerow -> dict를 인자)

> csv_practice.py

```python
import csv
lunch2 = [
    {
        '상호명':'양자강',
        '전화번호':'02-2345-6789'
    },
    {
        '상호명':'김밥카페',
        '전화번호':'02-1234-5678'
    },
    {
        '상호명':'순남시래기',
        '전화번호':'02-9876-5432'
    }
]

with open('lunch.csv','w') as f:
    field = ('상호명','전화번호')
    writer = csv.DictWriter(f, fieldnames = field)
    writer.writeheader()
    for l in lunch2:
        writer.writerow(l)
```

> lunch.csv

```python
상호명,전화번호
양자강,02-2345-6789
김밥카페,02-1234-5678
순남시래기,02-9876-5432
```

읽는 건 더 쉽게 조작ㅎㄹ 수 있다.

csv 읽을 때, 똑같이 with로 open을 한다. 그리고 명령어로 newline을 명시적으로 없애줄 수 있다. 실제 구현은 객체라서 리스트가 아닌데 리스트처럼 읽어올 수 있다.

> csv_practicee.py

```python
import csv
with open('lunch.csv',newline='')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

> console

```python
$ python3 csv_practice.py
['상호명', '전화번호']
['양자강', '02-2345-6789']
['김밥카페', '02-1234-5678']
['순남시래기', '02-9876-5432']
```





















































