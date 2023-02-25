# SQL Statements
- SQL 언어를 구성하는 가장 기본적인 코드 블록
```
SELECT column_name FROM table_name;
```
## SQL Statements 유형
|유형|역할|세부|SQL 키워드|
|:---:|:---:|:---:|:---:|
|DDL|데이터 정의|데이터의 기본 구조 및 형식 변경|CREATE / DROP / ALTER|
|DQL|데이터 검색|-|SELECT|
|DML|데이터 조작|추가, 수정, 삭제|INSERT / UPDATE / DELETE|
|DCL|데이터 제어|데이터 및 작업에 대한 사용자 권한 제어|COMMIT / ROLLBACK / GRANT / REVOKE|

## DQL 데이터 검색
- SELECT statement 실행 순서
  - **FROM** -> **SELECT** -> **ORDER BY**
    1. 테이블에서 (FROM)
    2. 조회하여 (SELECT)
    3. 정렬 (ORDER BY)