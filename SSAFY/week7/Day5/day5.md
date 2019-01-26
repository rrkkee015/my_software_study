# 2019-01-25

## 반응형 웹

**viewport** 사이즈는 디바이스 크기를 기준으로 잡는다.

757px은 대부분의 패드 디바이스는 커버 가능



미디워 쿼리는 어느 사이즈에 도달 했을 시 다른 css 요소에 영향을 줘서 변화를 주는 것이다.



**col-sm,md,lg** 이런식으로 단위를 나눠서 반응형 웹을 짤 수 있다.

```html
<body>
    <!-- container 생성 -->
    <div class="container-fluid">
        <!-- row 생성 -->
        <div class="row">
            <div class='bg-danger col-md-2 px-1'>
                글 1
            </div>
```

sm을 쓰게 되면 디바이스가 작은경우에  그 브레이크 포인트에서 그리드 시스템을 그만 쓰도록 하겠다라는 의미이다.

반응형 웹의 우수한 예가 에어비앤비



디바이스 크기에 따라서 다중으로 변화를 줘야한다.

```html
<body>
    <!-- container 생성 -->
    <div class="container-fluid">
        <!-- row 생성 -->
        <div class="row">
            <div class='bg-danger col-lg-2 col-md-4 col-sm-6 px-1'>
                글 1
            </div>
            <div class='bg-success col-lg-2 col-md-4 col-sm-6 px-1'>
                글 2
            </div>
            <div class='bg-warning col-lg-2 col-md-4 col-sm-6 px-1'>
                글 3
            </div>
```

bootstrap.com에 가면 Documentation에 Layout에 가보면 Grid에 가보면 위의 내용이 나와있다.

`<div class="card col-md-4 col-sm-6" style="width: 18rem;">` sm device 까지 2개씩 md device까지 4개씩 의 뜻이다. `<div class="row mt-4 justify-content-center">`을 하면 가운데 정렬이 된다.