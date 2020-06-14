# toyproject_1day3ggang

## toyproject 설명

할 일 리스트를 작성하면 메인화면의 타임라인에 최신 3개의 리스트를 띄워준다.

메인화면 참고 : [타임라인 디자인](https://www.w3schools.com/howto/howto_css_timeline.asp)

## 구조

프로젝트 명 : todolist

앱 1 :  account

- login.html

- sign up.html
- 모델
  - User 
    - user_id(pk)
    - user_name
    - email
    - password

앱 2 :  content

- base.html

- mainpage.html
- create.html
- update.html
- detail.html
- wholelist.html
- aboutus.html
- 모델
  - Todolist
    - user_id(fk)
    - title
    - image
    - description
    - write_time
    - finish_time
    
    superuser 아이디 : od3g
    <p></p>
    superuser 패스워드 : oneday3ggang
