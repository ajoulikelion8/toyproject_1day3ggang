# Todolist Web

## toyproject 설명

#### 할 일 리스트를 작성하면 메인화면의 타임라인에 최신 3개의 리스트를 띄워준다.

메인화면 참고 : [타임라인 디자인](https://www.w3schools.com/howto/howto_css_timeline.asp)    
웹 프론트 참고 : [로그인 및 회원가입](https://codepen.io/)    

## 구조

프로젝트 명 : todolist

앱 1 :  account

- login.html
- sign up.html   


- 모델
  - MyUser 
    - user_id(pk)
    - user_name
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
    
    superuser 아이디 : user1
    <p></p>
    superuser 패스워드 : user1234    
    
    
    
<br/>    
<hr/>    

## 기능 소개     
|기능|내용|진행 상황|
|------|---|:---:|
|로그인|아이디, 패스워드 입력 시 로그인 됨|진행중|
|회원가입|유저 이름, 이메일, 아이디, 패스워드 입력 시 회원가입 완료|진행중|   

<br/>
<br/>
<hr/>   

## 라이브러리    
```plain    
pip install django    
pip install pillow -> 이미지 라이브러리     
```   
