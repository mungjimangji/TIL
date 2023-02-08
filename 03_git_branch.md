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
  
  <br>
  <br>

## branch 병합 시나리오
  > - branch 관련된 명령어는 간단하다.
  > - 다양한 시나리오 속에서 어떤 상황인지 파악하고 자유롭게 활용할 수 있어야 한다.
  ### merge
  - 각 branch에서 작업을 한 이후 이력을 합치기 위해 merge 명령어를 사용
  - 병합을 진행할 때, 서로 다른 이력(commit)에서
    - 동일한 파일을 수정한 경우 충돌이 발생
      1. 파일을 확인하고 적절하게 수정
      2. 수정한 이후에 직접 커밋 실행
    - 다른 파일을 수정한 경우
      - 충돌 없이 자동으로 Merge Commit이 생성됨
  
    <br>

    ### 상황 1. fast-foward
      - fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황
      - 단순히 앞으로 이동
      
      <br>
      
      1. feature/home branch 생성 및 이동
      ```
      (master) $ git branch feature/home # 브랜치 만들기
      (master) $ git checkout feature/home # home으로 이동해줘
      ```

      2. 작업 완료 후 commit
      ```
      (feature/home) $ touch home.txt # 홈 텍스트 파일 만들기
      (feature/home) $ git add . # 변경사항 2통으로 추가하기
      (feature/home) $ git commit -m 'ADD home.txt' # 커밋 만들기
      (feature/home) $ git log --oneline # 진행사항 한줄로 나타내기
      
      b534a34 (HEAD -> feature/home) Complete Home!!!!
      89616a (master) Init
      ```

      3. master 이동
      ```
      (feature/home) $ git checkout master # 마스터로 이동해줘
      (master) $ git log --oneline
      ```

      4. master에 병합
      ```
      (master) $ git merge feature/home
      
      Updating e89616a..b534a34
      Fast-forward
      home.txt | 0
      1 file changed, 0 insertions(+), 0 deletions(-)
      create mode 100644 home.txt
      ```

      5. 결과 : fast-foward
      ```
      (master) $ git log --oneline
      
      b534a34 (HEAD -> master, feature/home) Complete Home!!!!
      e89616a Init
      ```

      6. branch 삭제
      ```
      (master) $ git branch -d feature/home 

      Deleted branch feature/home (was b534a34).
      ```
      <br>

    ### 상황 2. merge commit
      - 서로 다른 이력(commit)을 병합(merge)하는 과정에서 `다른 파일이 수정` 되어 있는 상황
      - git이 auto merging을 진행하고, commit이 발생된다.
      
      <br>
      
      1. feature/about branch 생성 및 이동
      ```
      (master) $ git checkout -b feature/about
      (feature/about) $
      ```

      2. 작업 완료 후 commit
      ```
      (feature/about) $ touch about.txt
      (feature/about) $ git add .
      (feature/about) $ git commit -m 'Add about.txt'
      (feature/about) $ git log --oneline
      
      5e1f6de (HEAD -> feature/about) 자기소개 페이지 완료!
      b534a34 (master) Complete Home!!!!
      e89616a Init
      ```

      3. master 이동
      ```
      (feature/about) $ git checkout master
      (master) $
      ```

      4. master에 추가 commit 이 발생시키기!!
        - 다른 파일을 수정 혹은 생성하세요!
        ```
        (master) $ touch master.txt
        (master) $ git add .
        (master) $ git commit -m 'Add master.txt'
        (master) $ git log --oneline
        98c5528 (HEAD -> master) 마스터 작업....
        b534a34 Complete Home!!!!
        e89616a Init
        ```








