# git : 분산버전관리 시스템
  - 로컬에서 버전을 기록하고 관리
  <br>
  <br>
  <br>
  ## git init
    * 특정 폴더에 git 저장소(repository)를 만들고 버전 관리
     * .git 폴더가 생성됨
     * git bash에서는 (master)라는 표기를 확인할 수 있음
     * git init 명령어를 사용해야 git으로 관리 됨
  


  ## git 버전 관리 기초 흐름
    * 작업(수정)한 파일 상태 -add-> 커밋할 파일 상태 목록 -commit-> 버전
      1. 작업을 하고
      2. 변경된 파일을 모아 (add)
      3. 버전으로 남긴다. (commit)
    
    1. Working Directory : 와 보고서 다 썼다~ (1통)
    - $ git add -
    2. Staging Area : 버전으로 기록하기 위한 파일의 변경사항의 목록 (2통)
    - $ git commit -
    3. Repository : 커밋(버전)들이 기록되는 곳 (3통)
  ### 기본 명령어
    - add(커밋 대상 기록)
      * $ git add <file>
        - working directory(1통)상의 변경 내용을 staging area(2통)에 추가하기 위해 사용
          - untracked 상태의 파일을 staged로 변경 (나중에)
          - modified 상태의 파일을 staged로 변경 (배움)
    
    - 커밋(버전 기록)
      * $ git commit -m '<커밋메세지>'
        - Staged(2통에 있던것들) 상태의 파일들을 커밋을 통해 버전으로 기록
        - -m : 메세지 옵션
        - 커밋 메세지는 변경 사항을 나타낼 수 있도록 명확하게 작성해야 함
    
    - 파일 만들기
      * $ touch 파일명
    
    - 유저 이메일, 이름 확인하기
      * $ git config user.email / $ git config user.name
    
    - 깃허브에 올리기
      1. $ git add 파일명
      2. $ git commit -m "이름"
      3. $ git push origin main
  ### Git의 버전 관리
    - Git은 데이터를 파일 시스템의 스냅샷으로 관리하고 매우 크기가 작음
    - 파일이 달라지지 않으면 성능을 위해 파일을 새로 저장 안함

  ### 현재 상태를 알고 싶어요
    * $ git status
      - Working Directory(1통) / Staging Area(2통)의 상태를 앎
      - git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
        - 파일의 상태를 알 수 있음
          * Untracked files (1통)
            - 1.txt 를 만들었지만, add를 하지 않음
            - (상황) 1.txt 를 만들었지만, add를 하지 않음
          
          * Changes not staged for commit (1통)
            - 커밋을  위해 staged가 아닌 변경 사항들
            - (상황) 커밋된 적 있는 보고서.txt 파일을 수정한 상태!
          
          * Changes to be committed (2통) 
            - 커밋될 변경사항들 (곧 커밋 될 애들)
            - (상황) 보고서.txt 만들고 add함.
          
          * nothing to commit, working tree clean 
              - (상황) 작업한 것도 커밋할 것도 없어 (1통, 2통 비어있음)
    
    * $ git log
      - Repository(3통) 의 상태를 앎
      - 현재 저장소에 기록된 커밋을 조회
      - 다양한 옵션을 통해 로그를 조회할 수 있음
        - $ git log -1 : 최근 한개 조회
        - $ git log --oneline : 최근 한줄로 조회
        - $ git log -2 --oneline : 최근 2개를 한줄로 조회
        - ※ 하이픈의 갯수나 띄어쓰기 유의


