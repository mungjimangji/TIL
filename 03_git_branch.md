# Git branch

<br>

## branch 관련 명령어
  - 독립적인 작업 흐름을 만들고 관리
  ```
  $ git init
  (master) $ touch README.md
  (master) $ git add .
  (master) $ git commit -m 'Init'
  ```
  1. 브랜치 생성
  ```
  (master) $ git branch {브랜치명}
  ```
  2. 브랜치 이동
  ```
  (master) $ git checkout {브랜치명}
  ```
  3. 브랜치 생성 및 이동
  ```
  (master) $ git checkout -b {브랜치명}
  ```
  4. 브랜치 삭제
  ```
  (master) $ git branch -d {브랜치명}
  ```
  5. 브랜치 목록 확인
  ```
  (master) $ git branch
  ```
  6. 브랜치 병합
  ```
  (master) $ git merge {브랜치명}
  ```
  - master 브랜치에서 {브랜치명}을 병합
## branch 병합 시나리오
  - branch 관련된 명령어는 간단하다.
  - 다양한 시나리오 속에서 어떤 상황인지 파악하고 자유롭게 활용할 수 있어야 한다.
  ### 상황 1. fast-foward
  - fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황
