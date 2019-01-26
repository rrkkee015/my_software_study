# HTML/CSS를 이용한 영화 소개 WEB 제작

## 1. 목표

- WEB 프론트엔드에 대한 이해
- 영화 추천 사이트를 위한 HTML를 통한 웹 페이지 마크업 및 레이아웃 구성
- CSS를 통한 선택자 활용 및 웹 페이지 꾸미기
- Bootstrap을 활용한 HTML/CSS, JS Component 활용
- 반응형 웹 페이지 구현

## 2. 준비 사항

1. HTML/CSS, Bootstrap 환경 구성
2. font-awesome을 이용하여 다양한 이미지 구성

## 3. 제작 단계

### 1. 영화 추천 사이트를 위한 레이아웃 구성

1. Bootstarp 사용을 위해 `<head></head>`사이에 링크 복사

   ```html
   <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
   <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
   <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
   ```

2. Google 폰트 사용을 위해 `<head></head>`사이에 링크 복사

   ```html
   <link href="https://fonts.googleapis.com/css?family=Nanum+Myeongjo:700" rel="stylesheet">
   <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR" rel="stylesheet">
   ```

3. Fontawesome 사용을 위해 `<head></head>`사이에 링크 복사

   ```html
   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
   ```

4. **Navigation Bar**의 고정을 위해서 **Sticky-top**을 이용했다.

   ```html
   <nav class="navbar navbar-expand-lg navbar-dark nav_color my_font sticky-top">
   ```

5. **Footer**의 고정을 위해서 **fixed-bottom**을 이용했다. 또한 인스타그램 링크와 **header**로 돌아오는 버튼의 사이를 벌리기위해서 **space-between**을 이용했다.

   ```html
   <footer class="fixed-bottom footer">
   ```

   ```css
   .footer{
       display:flex;
       justify-content:space-between;
       color:rgb(225, 231, 227);
       font-family: 'Noto Sans KR', sans-serif !important; 
       align-items: center;
       height:50px;
       background-color:rgb(107,116,111);
   }
   ```

6. **header** 폰트가 중심에 오도록 아래와 같은 코드를 이용했다.

   ```css
   .header{
       display : flex;
       background-image:url(images/eternal_sunshine.jpg);
       font-family: 'Nanum Myeongjo', serif;
       font-weight:bold;
       align-items: center;
       justify-content: center;
       height:350px;
       color:rgb(107, 116, 111) !important;
   }
   ```

### 2. 영화 리스트 구성

1. 6개의 영화 정보를 보여주기 위해서 6개의 카드를 준비했고, 반응형 웹을 설계하기 위해서 **container** 내부에 설계를 하였다.

2. 아래와 같은 반응형 웹을 만드려 했다.

   - 576px 미만 : 1개
   - 576px 이상 768px 미만 : 2개
   - 768px 이상 992px 미만 : 3개
   - 992px 이상 : 4개

   따라서 아래와 같은 코드를 사용했다.

   ```html
   col-12 col-sm-6 col-md-4 col-lg-3
   ```

   기본값은 1개를 보여주고 sm일 땐 2개 md일 땐 3개 lg일 땐 4개를 보여주는 grid 설계를 했다.

3. 영화 링크는 새 창에서 열려야 하기에 아래와 같은 키워드를 버튼에 추가하였다.

   ```html
   target="_blank"
   ```

### 3. 영화 상세 보기

1. Modal을 이용하여 상세 보기 레이아웃을 제작한다. **Bootstrap**의 **modal** 항목 중 **Vertically centered**을 참고하였다.

   ```html
   <!-- Button trigger modal -->
   <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">
     Launch demo modal
   </button>
   
   <!-- Modal -->
   <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
     <div class="modal-dialog modal-dialog-centered" role="document">
       <div class="modal-content">
         <div class="modal-header">
           <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
           <button type="button" class="close" data-dismiss="modal" aria-label="Close">
             <span aria-hidden="true">&times;</span>
           </button>
         </div>
         <div class="modal-body">
           ...
         </div>
         <div class="modal-footer">
           <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
           <button type="button" class="btn btn-primary">Save changes</button>
         </div>
       </div>
     </div>
   </div>
   ```

2. 영화에 대한 이미지를 보다 많이 제공하기 위해서 **carousel**을 이용했다.

   ```html
   <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
     <ol class="carousel-indicators">
       <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
     </ol>
     <div class="carousel-inner">
       <div class="carousel-item active">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
       <div class="carousel-item">
         <img src="..." class="d-block w-100" alt="...">
       </div>
     </div>
     <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
       <span class="carousel-control-prev-icon" aria-hidden="true"></span>
       <span class="sr-only">Previous</span>
     </a>
     <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
       <span class="carousel-control-next-icon" aria-hidden="true"></span>
       <span class="sr-only">Next</span>
     </a>
   </div>
   ```

## 4. 프로젝트 후기

- HTML/CSS에 대한 이해도를 높일 수 있었다.
- 반응형 웹 디자인에 대한 이해도를 높일 수 있었다.
- Bootstrap을 이용하여 다양한 코딩 자료를 통해서 다양한 서비스를 제공할 수 있었다는 점에서 좋은 경험을 할 수 있었다.
- Airbnb, skyscanner등과 같은 다양한 웹들이 반응형 웹을 이용하여 깔끔한 웹 서비스를 제공하고 있었다는 것을 알게되었다.
- 혹여나 아버지 회사에서 사이트를 만들어 달란 요청이 오더라도 이번 프로젝트 경험을 통해 남 부럽지 않은 사이트 디자인과 제작을 할 수 있을 거란 자신감을 얻을 수 있었다.