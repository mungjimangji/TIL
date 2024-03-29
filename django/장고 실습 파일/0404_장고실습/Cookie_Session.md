# Cookie & Session
## HTTP 특징
1. 비 연결 지향(connectionless)
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - HTTP는 먼저 클라이언트가 request를 서버에 보내면, 서버는 클라이언트에게 요청에 맞는 response를 보내고 접속을 끊는 특성이 있음
2. 무상태(stateless)
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
**-> 쿠키와 세션은 위 두 가지 특징을 해결하기 위해 사용**
## 쿠키(Cookie) 특징
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
<br>
 -> 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 사용자 추적, 상태 유지 등에 사용되는 데이터 저장 방식
- 사용자 인증이 유효한 시간을 명시 가능, 유효 시간이 정해지면 브라우저가 종료되어도 인증이 유지 됨

- ### 쿠키 사용 예시
  1. 브라우저(클라이언트)는 쿠키를 **로컬에 KEY-VALUE의 데이터 형식**으로 저장
  2. 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청시 저장된 쿠키를 전송 <br>
  -> 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문 
  3. ex. 장바구니에 상품 담기
- ### 쿠키 사용 목적
  1. 세션 관리 (Session management)
    - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
  2. 개인화 (Personalization)
    - 사용자 선호, 테마 등의 설정
  3. 트래킹 (Tracking)
    - 사용자 행동을 기록 및 분석
> 응답한 서버로부터 쿠키를 받아 브라우저에 저장하고, 클라이어트가 같은 서버에 재 요청 시마다 저장해 두었던 쿠키도 요청과 함께 전송한다.<br>
-> **로그인 되어있다는 사실을 입증할 데이터를 계속 보내는 것**
- ### 쿠키의 동작 방식
  1. 클라이언트가 페이지를 요청
  2. 서버에서 쿠키를 생성
  3. HTTP 헤더에 쿠키를 포함 시켜 응답
  4. 브라우저가 종료 되어도 쿠키 만료 기간이 있다면 클라이언트에서 보관하고 있음
  5. 같은 요청을 할 경우 HTTP 헤더에 쿠키를 함께 보냄
  6. 서버에서 쿠키를 읽어 이전 상태 정보를 변경 할 필요가 있을 때 쿠키를 업데이트 하여 변경된 쿠키를 HTTP 헤더에 포함시켜 응답
## 세션(Session) 특징
- 서버 측에서 생성되어 클라이언트와 서버간의 상태를 유지
- 상태 정보를 저장하는 데이터 저장 방식
- 세션은 쿠키를 기반하지만 사용자 정보 파일을 브라우저에 저장하는 쿠키와 달리 세션은 서버 측에서 관리함
- 사용자에 대한 정보를 서버에 두기에 쿠키보다 보안에 좋지만, 사용자가 많아질 수록 서버 메모리를 많이 차지하게 됨 <br>
(동접자 수가 많은 웹 사이트인 경우 서버에 과부하를 주게 되므로 성능 저하의 요인이 됩니다.)

- **->쿠키에 세션 데이터를 저장하며 매 요청시마다 세션 데이터를 함께 보냄**
- ### 세션 작동 예시
  1. 클라이언트가 로그인을 하면 서버가 session 데이터를 생성 후 저장
  2. 생성된 session 데이터에 인증 할 수 있는 session id를 발급
  3. 발급한 session id를 클라이언트에게 응답
  4. 클라이언트는 응답 받은 session id를 쿠키에 저장
  5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
  6. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함

>세션은 서버측에서 저장 됨<br>
서버 측에서는 세션 ID를 생성하고, 이 ID를 클라이언트 측으로 전달하여, 클라이언트는 쿠키에 이 ID를 저장