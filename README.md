# PROJECT: We&Olufsen
## 소개
- [Bango & Olufsen](https://www.bang-olufsen.com/ko/kr) 클론 사이트
- 고급 스피커 판매 사이트: 카테고리 분류, 회원관리, 장바구니, 주문, 정렬기능, 페이지네이션

## 팀 인원
- BE(2명): 손찬규, 박서윤
- FE(4명): 신수정, 심동규, 이현주, 정훈조

## 개발 기간
- 개발 기간 : 2022-07-18 ~ 2022-07-29 (12일)
- 협업 툴 : Slack, Trello, Github, Notion

## 기술 스택
|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |                                                  Deploy                                                 |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |:------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> 


## Backend 역할
**박서윤**
- 회원가입(SignUpView)
  - POST
  - 정규식 통해 이메일과 패스워드 조건 확인
  - email unique 처리
  - 패스워드 암호화
- 상품상세페이지(ProductDetailView)
  - GET
  - 해당 product_id의 상세페이지 구현
- 주문페이지(OrderView)
  - POST
  - transaction.atomic()으로 order에서 발생할 오류 방지
- 장바구니(CartView)
  - POST, GET, DELETE, PATCH
  - get_or_create 이용하여 장바구니에 존재여부 고려

**손찬규**
- 로그인(LoginView)
  - POST
  - JWT를 이용하여 토큰 발급
- 상품페이지(ProductListView)
  - GET
  - limit, offset을 통한 pagination 구현
  - Q객체 사용: 데이터 정렬 후, 전송
 
 
## 모델링
<img width="1400px" src="https://user-images.githubusercontent.com/91110192/181713064-a61209dc-5678-491c-b41e-5d59c664fb56.png"/>

## 사이트 시현 영상
<img src="https://user-images.githubusercontent.com/91110192/191254956-09abe406-efd7-42f9-b388-c8751f2b1aa5.gif">

## API 명세서
<img width="797" alt="스크린샷 2022-07-30 오후 3 33 59" src="https://user-images.githubusercontent.com/91110192/181878038-25f4d635-4407-4d84-b4f1-fbe2c041096f.png">
<img width="789" alt="스크린샷 2022-07-30 오후 3 33 51" src="https://user-images.githubusercontent.com/91110192/181878041-6ccdd0d4-9a61-4354-9086-7fa46f2e6cf7.png">
<img width="793" alt="스크린샷 2022-07-30 오후 3 33 35" src="https://user-images.githubusercontent.com/91110192/181878044-bf1f17df-6cf4-42ae-9a1e-25c518bbf126.png">
<img width="796" alt="스크린샷 2022-07-30 오후 3 33 21" src="https://user-images.githubusercontent.com/91110192/181878045-98d8a784-5828-43f7-80f9-a6f403c55fba.png">

* [WeOlufsen API](https://pastoral-slice-3c4.notion.site/API-40dd9ab8a58f442baad377974f308ecc)를 보시면, 자세한 API를 확인 가능합니다.

## 참고
- 이 프로젝트는 [Bang & Olufsen](https://www.bang-olufsen.com/ko/kr) 사이트를 참조하여 학습 목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
