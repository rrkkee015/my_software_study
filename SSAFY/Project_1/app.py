import requests
import json
import os
import bs4
import csv
from pprint import pprint as pp
import datetime
import urllib.request

token = os.getenv('MOVIE_TOKEN')

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
Movie_boxoffice_data = [] #영화 주간/주말 박스오피스 데이터
fixed_crds=[] #영화 상세정보를 위한 코드 담는 곳
movie_names=[] #중복된 영화 이름 확인하기위한 장소
for h in range(10):
    d=datetime.date(2019,1,13)
    dd=d+datetime.timedelta(-7*h)
    dd=dd.strftime('%Y%m%d')
    params = {
    'key':token,
    'targetDt':dd,
    'weekGb':'0' #주간(월~일)까지 기간의 데이터를 조회합니다.
    }
    response = json.loads(requests.get(url,params=params).text)

    Movie_cords=[]
    Movie_names=[]
    Movie_audiAcc=[]
    Movie_yearWeekTime = response['boxOfficeResult']['yearWeekTime'] #해당일 몇 주인지 알려주는 코드

    
    for i in range(10): #영화 대표코드
        Movie_cords.append(response['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'])
    
    for j in range(10): #영화명
        Movie_names.append(response['boxOfficeResult']['weeklyBoxOfficeList'][j]['movieNm'])
    
    for k in range(10): #해당일 누적관객수
        Movie_audiAcc.append(response['boxOfficeResult']['weeklyBoxOfficeList'][k]['audiAcc'])
        
    for z in range(10):
        if Movie_names[z] in movie_names:
            continue
        else:
            movie_names.append(Movie_names[z])
            fixed_crds.append(Movie_cords[z])
            Movie_boxoffice = {
            'movie_code':Movie_cords[z],
            'title':Movie_names[z],
            'audience':Movie_audiAcc[z],
            'recorded_at':params['targetDt']
        }
            Movie_boxoffice_data.append(Movie_boxoffice)

with open('boxoffice.csv','a',encoding='utf-8') as o: #영진위에서 영화 정보 받아서 csv 파일 만드는 코드
    filed = ('movie_code','title','audience','recorded_at')
    writer = csv.DictWriter(o, fieldnames=filed)
    writer.writeheader()
    for l in Movie_boxoffice_data:
        writer.writerow(l)

details=[] #최종 상세정보들을 담을 딕셔너리
for crd in fixed_crds:
    url2 = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"
    params2 = {
        'key':token,
        'movieCd':crd
    }
    response2 = json.loads(requests.get(url2,params=params2).text)
    
    detail={} #for문 돌면서 넣을 임시 딕셔너리
    
    moviecrd=crd #영화코드
    movieNm=response2['movieInfoResult']['movieInfo']['movieNm'] #영화이름
    movieNmEn=response2['movieInfoResult']['movieInfo']['movieNmEn'] #영화영어이름
    movieNmOg=response2['movieInfoResult']['movieInfo']['movieNmOg'] #영화원문이름
    openDt=response2['movieInfoResult']['movieInfo']['openDt'] #개봉연도
    showTm=response2['movieInfoResult']['movieInfo']['showTm'] #상영시간
    
    genres=response2['movieInfoResult']['movieInfo']['genres'] #장르이름
    genress=[]
    for genre in range(0,len(genres)):
        genress.append(genres[genre]['genreNm'])
    final_genres='/'.join(genress) #장르 다 합치기
    
    directors=response2['movieInfoResult']['movieInfo']['directors'] #감독이름
    directorss=[]
    for director in range(0,len(directors)):
        directorss.append(directors[director]['peopleNm'])
    final_directors='/'.join(directorss)
    
    grades=response2['movieInfoResult']['movieInfo']['audits'] #시청등급
    gradess=[]
    for grade in range(0,len(grades)):
        gradess.append(grades[grade]['watchGradeNm'])
    final_grades='/'.join(gradess)
    
    actors=response2['movieInfoResult']['movieInfo']['actors'] #배우
    actorss=['-','-','-']
    for actor in range(0,len(actors)):
        if actor == 3:
            break
        # actorss.append(actors['peopleNm'])
        actorss[actor]=actors[actor]['peopleNm']
    
    detail={
        'movie_code':moviecrd,
        'movie_name_ko':movieNm,
        'movie_name_en':movieNmEn,
        'movie_name_og':movieNmOg,
        'prdt_year':openDt,
        'genres':final_genres,
        'directors':final_directors,
        'watch_grade_nm':final_grades,
        'actor1':actorss[0],
        'actor2':actorss[1],
        'actor3':actorss[2]
    }
    
    details.append(detail)

with open('movie.csv','a',encoding='utf-8') as f:
    filed = ('movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3')
    writer = csv.DictWriter(f, fieldnames=filed)
    writer.writeheader()
    for l in details:
        writer.writerow(l)

naver_url = 'https://openapi.naver.com/v1/search/movie.json' #네이버 URL

id = os.getenv('naver_id') #네이버 아이디 환경변수
secret = os.getenv('naver_secret') #네이버 비번 환경변수

headers = {
    'X-Naver-Client-Id' : id,
    'X-Naver-Client-Secret' : secret
} #요청하기 위해 박스에 담았다.

naver_movies=[] #영진위 영화 대표코드, 영화 썸네일 이미지의 URL, 하이퍼텍스트 link, 유저 평점 담은 리스트
for i in details:
    params = {
        'query' : i['movie_name_ko']
    }
    
    res=json.loads(requests.get(naver_url, headers=headers, params=params).text) #get 방식은 params post는 data로 보냄
    
    thumb_url = res['items'][0]['image']
    link_url = res['items'][0]['link']
    user_rating = res['items'][0]['userRating']
    
    naver_movie={
        'movie_code':i['movie_code'],
        'thumb_url':thumb_url,
        'link_url':link_url,
        'user_rating':user_rating
    }
    
    naver_movies.append(naver_movie)

with open('movie_naver.csv','a',encoding='utf-8') as z: #movie_naver.csv 만드는 코드
    filed = ('movie_code','thumb_url','link_url','user_rating')
    writer = csv.DictWriter(z, fieldnames=filed)
    writer.writeheader()
    for l in naver_movies:
        writer.writerow(l)
        
for k in naver_movies:
    image_url = k['thumb_url']
    movie_code = k['movie_code']
    file = urllib.request.urlretrieve(image_url,'images/'+str(movie_code)+'.jpg')
