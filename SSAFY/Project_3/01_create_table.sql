-- 요구 스키마를 가진 테이블 생성
CREATE TABLE movies(
    영화코드 INTEGER PRIMARY KEY,
    영화이름 TEXT,
    관람등급 TEXT,
    감독 TEXT,
    개봉연도 INTEGER,
    누적관객수 INTEGER,
    상영시간 INTEGER,
    제작국가 TEXT,
    장르 TEXT
);

-- csv import를 위한 코드
.mode csv

-- boxoffice.csv를 movies 테이블에 불러오기
.import boxoffice.csv movies

-- 제대로 import가 되었는지 출력하기
SELECT * FROM movies;