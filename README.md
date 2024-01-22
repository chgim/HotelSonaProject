# Hotel Sona

## 프로젝트 개요
- 프로젝트 주제: 가상의 호텔 예약 웹 프로젝트
- 프로젝트 이름: Hotel Sona
- 개발 인원: 1명
- 개발 기간: 2023.05.06 ~ 2023.06.20  
- 개발 언어: Python
- Front-End: Html, Css, Javascript, Bootstrap(Template)
- Back-End: Django
- DB: sqlite3
- Api: 카카오 로그인 Api

## 프로젝트 기능
### 사용자
1.	accounts: Django 인증 로그인(django.contrib.auth), 카카오 로그인
2.	booking: 선택한 인원 수에 맞는 객실 조회 및 예약, 동일 날짜 중복 예약 방지
3.	mypage: 예약 확인 및 선택 취소, 체크아웃 날짜가 체크인 날짜보다 작은 경우 "이용완료" 표시, 로그인 한 사용자 대상 회원정보 수정
4.	inquires: 고객 질문 CRUD, 비공개 글 / 공개 글 선택, 작성자의 작성 글 삭제, 질문에 대한 관리자의 답변 있을 시 답변 표시

### 관리자
1.	회원 관리
2.	예약 관리
3.	문의 게시판 관리
4.	객실 관리


## 프로젝트 ppt
https://github.com/chgim/HotelSonaProject/blob/main/%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4%EC%BB%B4%ED%93%A8%ED%8C%85.pptx

## 보완점
- 카카오 로그인은 가능하지만 로컬 로그인과 세션을 동기화 하지 않아 카카오 계정과 함께 로그아웃 기능을 구현 못함
- 카카오 로그인 시 마이 페이지에서 예약 정보를 확인할 때 이메일 란에 이름이 들어감
- 카카오페이 결제 시스템 기능 추가 원함
- 각 객실마다 이용가능한 방의 수를 지정하길 원함  
- 최적화 필요
