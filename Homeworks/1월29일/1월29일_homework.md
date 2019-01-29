# Django Web Framgework

```
학습해야 할 내용
- SQLite RDBMS
```

아래 동작을 수행하기 위한 SQL을 각각 작성하세요.



다음과 같은 스키마를 가지는 DB 테이블 friends를 생성한다.

```sql
CREATE TABLE friends(
	id INTEGER,
	name TEXT,
	location TEXT
)
```



해당 테이블에 다음과 같이 데이터를 입력한다.

```sql
sqlite>INSERT INTO friends (id, name, location) VALUES (1, Justin, Seoul);
sqlite>INSERT INTO friends (id, name, location) VALUES (2, Simon, New York);
sqlite>INSERT INTO friends (id, name, location) VALUES (3, Chang, Las Vegas);
sqlite>INSERT INTO friends (id, name, location) VALUES (4, John, Sydney);
```



스키마를 다음과 같이 변경하다.

```sql
sqlite>ALTER TABLE friends ADD COLUMN married INTEGER;
```



데이터를 다음과 같이 추가한다.

```SQL
sqlite>UPDATE friends SET married=0;
sqlite>UPDATE friends SET married=1 WHERE id = 1 or id = 4;
```



**아래 동작을 수행하기 위한 SQL을 각각 작성하세요.**



married 가 0 인 데이터를 모두 삭제한다.

```sql
sqlite> DELETE FROM friends WHERE married=0;
```



테이블을 삭제한다

```sql
sqlite>DROP TABLE friends;
```

