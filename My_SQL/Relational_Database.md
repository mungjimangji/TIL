# 관계형 데이터 베이스 용어 정리
## 1. Table (aka Relation
  - 관계라고 부르기도 함.
  - 데이터를 기록하는 곳.
  ![table](img\table1.png)

<br>

## 2. Field (aka Column열, Attribute)
  - 각 필드에는 고유한 데이터 '형식(타입)'이 지정됨
  - 열이라고는 잘 안부름
  - 속성이라고 부르는 이유는 타입이 지정되기 때문
    <br>
    타입ex) 정수, 문자
    ![field](img\column.png)

<br>

## 3. Record (aka Row, Tuple)
  - 각 레코드에는 구체적인 데이터 '값'이 저장됨
  - 행이라고는 잘 안부름
  - 튜플이라고 부르지만 파이썬과는 상관 놉
  ![record](img\record.png)

<br>

## 4. Database (aka Schema)
  - 테이블의 집합(Set of tables)
  - Table이랑 다름 (더 큰 범위)
  ![database](img\database.png)

<br>

## 5. Primary Key(기본 키)(PK)
  - 각 레코드(열)의 고유한 값
  - 관계형 데이터베이스에서 레코드의 식별자로 활용
  - 중복이 불가능
  ![primarykey](img\primarykey.png)

<br>

## 6. Foreign Key(외래 키)
  - 테이블의 필드 중 다른 테이블의 레코드(행)를 식별할 수 있는 키
  - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는 데 사용
  - 관계형 데이터 베이스의 핵심! 외래키가 관계형 데이터 베이스를 만든다.
  ![ForeignKey](img\foreign.png)
  
