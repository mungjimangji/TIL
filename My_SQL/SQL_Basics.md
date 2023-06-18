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

  ### Filtering data 관련 Keywords
  > Clause
    - DISTINCT / WHERE / LIMIT
  > Operator
    - BETWEEN / IN / LIKE / Comparison / Logical

  - **DISTINCT** clause
  <br>
  : 조회 결과에서 중복된 레코드를 제거
  ```
  SELECT DISTINCT select_list
  FROM table_name;
  ```
    - SELECT 키워드 바로 뒤에 작성해야 함
    - SELECT DISRINCT 키워드 다음에 고유함 값을 선택하려는 하나 이상의 필드를 지정
  - **WHERE** clause
  <br>
  : 조회 시 특정 검색 조건을 지정
  ```
  SELECT DISTINCT select_list
  FROM table_name
  WHERE search_condition;
  ```
    - FROM clause 뒤에 위치
    - search_condition은 비교 연산자 및 논리 연산자(AND, OR, NOT등)를 사용하는 구문이 사용됨
    - 1과 4 사이 (officeCode>=1 AND officeCode<=4 와 같음)
    - 
      ```
      WHERE
        officeCode BETWEEN 1 AND 4;
      ```
    - 1 또는 3 또는 4 값인 데이터
      ```

      ```

