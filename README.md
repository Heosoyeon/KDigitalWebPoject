## 웹 프로젝트 : 영화 소개 및 평점 부여, 게시판 작성

- User
  - 로그인, 로그아웃, 회원가입, 회원정보조회, 아이디찾기, 비밀번호 찾기, 회원탈퇴
- Home 화면
  - 로그인 전
    - 조회수 상위 3개의 게시글
     (클릭하면, 해당 게시글 출력)
    - 게시글 열람, 영화 정보 조회 가능 
  - 로그인 후
    - 평점 부과에 따른 관심 영화를 HOME에서 바로 보기 가능
      (5초 마다 포스터가 바뀌며, 포스터 클릭 -> 해당 영화 정보 조회 가능)
    - 조회수 상위 3개의 게시글
     (클릭하면, 해당 게시글 출력)
- 후기 게시판
  - summernote 사용
  - 수정, 삭제
  - 페이징 (한 페이지에 게시글 10개씩)
  - 추천 (한 id 당 1번만 가능)
  - 정렬 -> 조회수순, 최신순
  - 미로그인 : 게시판 작성, 추천 불가 
- 장르별 카테고리
   - 장르 : 로맨스, 판타지, 스릴러, 코미디, SF, 호러, 미스터리, 다큐멘터리, 애니메이션
   - 영화 포스터 클릭 > 
      - 영화정보 조회,
      - 예고편 Link 연결,
      - 평점 부과 (-> 로그인 시에만 가능)

## 시스템 구성도

<img src="https://user-images.githubusercontent.com/90740783/158526061-4b7bd105-a3ec-4838-b29e-218ea664d002.PNG" style="width:70%">


## ERD

<img src="https://user-images.githubusercontent.com/90740783/158525795-5326c26d-4c96-414b-8e1d-2b2299ab13f9.PNG" style="width:70%">

## 시연동영상

<h3>메인페이지</h3>

![MainPage](https://user-images.githubusercontent.com/99372040/159148858-6c83e6b7-d07f-4201-9d61-de991da861d3.gif)

<h3>User</h3>

![User](https://user-images.githubusercontent.com/99372040/159148877-9e374809-fe2c-4a87-81dc-f78e61efd32a.gif)

<h3>영화</h3>

![movie](https://user-images.githubusercontent.com/99372040/159148883-4635f1aa-f460-466c-877f-b76404aa3936.gif)

<h3>후기 게시판</h3>

![reviewboard](https://user-images.githubusercontent.com/99372040/159148890-95714ac7-761f-4963-b6c3-42111c3ffe86.gif)
![reviewboard(2)](https://user-images.githubusercontent.com/99372040/159148892-bf4d4b29-0c6c-4347-b0d9-68654413f99b.gif)
