# 다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로 구분하는 프로그램을 작성하십시오.
# 입력 : http://www.example.com/test?p=1&q=2
# 출력 : protocol : http
#        host : www.example.com
#        others : test?p=1&q2

# 1. input을 받는 변수를 만든다.
# 2. w를 처음 만나면 host가 출력되도록 하자.
# 3. 그 뒤에 /를 만나면 others를 출력되도록하자.

URL = input('')
protocol = URL.find(':')
host = URL.find('w')
others = URL.find('/',host)
if host != -1:
    print("protocol: {}\nhost: {}\nothers: {}".format(URL[0:protocol],URL[host:others],URL[others+1:]))

