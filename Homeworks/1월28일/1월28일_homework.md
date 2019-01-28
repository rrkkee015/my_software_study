# Django Web Framework

```
학습해야 할 내용
- SQLite RDBMS
```

1. 우리가 사용하는 SQLite는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하세요.

   1. 관계형 모델을 기반으로하는 데이터베이스 관리시스템입니다.
   2. 모든 데이터가 테이블로 저장해서 담기고, 행과 열로 표현된다.

2. 참 / 거짓

   2.1 RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [참]

   2.2 SQL에서 명령어는 대문자로 써야만 동작한다. [거짓]

   2.3 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [참]

   2.4 SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다. [참]

   2.5 한 개의 DB에는 한 개의 테이블만 존재한다. [거짓]

3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.

   ```
   sqlite> .nullvalue 'NULL'
   sqlite> CREATE TABLE ssafy(
   	..> id INTEGER,
   	..> location TEXT,
   	..> class INTEGER
   	..>);
   sqlite> INSERT INTO ssafy (id, loaction)
   	..> VALUES (1, 'JEJU');
   sqlite> SELECT class FROM ssafy WHERE id=1;
   ```

   ```
   NULL
   ```
