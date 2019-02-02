-- 누락된 극한직업 영화 추가하기
INSERT INTO movies 
VALUES (20182530,'극한직업','15세이상관람가','이병헌',20190123,3138467,111,'한국','코미디');

-- 특정 데이터 출력 및 삭제
SELECT * FROM movies WHERE 영화코드 = 20040521;
DELETE FROM movies WHERE 영화코드 = 200402521;

-- 특정 데이터 출력 및 수정 후 다시 출력
SELECT * FROM movies WHERE 영화코드 = 20185124;
UPDATE movies SET 감독 = '없음' WHERE 영화코드 = 20185124;
SELECT * FROM movies WHERE 영화코드 = 20185124;