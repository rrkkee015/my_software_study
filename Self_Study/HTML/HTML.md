## HTML 배우기 2018 - 12 - 18

- HTML은 웹사이트에 있는 내용을 위한 구조를 제공한다. 이미지, 텍스트, 비디오 같은

  *HAN DONG HUN이 출력되는 입력*

```html
<h1>
    HAN DONG HUN
</h1>
```

- HTML은 요소로 구성되어 있다. 이 요소가 웹페이지를 구성하고 내용을 정의한다.

  - HTML의 간단한 구조

    1. HTML element (아니면 그냥 element) : HTML 태그로 구성된 HTML document 안에 있는 내용물을 말한다.
    2. HTML Tag : 요소 이름, <>(angle bracket)으로 둘러진 애
    3. 오프닝 태그 : 첫번째 HTML tag를 말하고 HTML element의 시작을 알릴 때 사용한다.
    4. Content : 오프닝 태그와 클로징 태그 사이에서 정보를 가진 아이
    5. 클로징 태그 : 두번째 HTML tag HTML element의 끝을 알린다. 클로징 태그에는 / 를 붙힌다.

    ```html
    <p>
        Hello World!
    </p>
    ```

    - 처음 <p>를 오프닝 태그라고 하고 마지막 </p>를 클로징 태그라고 한다.
    - 안에 Hello World!는 content이다.
    - 이 모든 걸 싸잡아서 HTML element라고 부른다.
    - 우리가 이미지, 텍스트 이런 것들을 조직하고 보여주기 위해서 많은 태그들을 사용한다.

- 우리가 웹사이트를 만들기 위해 사용되는 HTML 요소 중 하나에는 body element가 있다. body에 둘러진 애는 스크린에만 표시된다.

  *Body의 기본형*

  ```html
  <body>
      
  </body>
  ```

  다른 타입의 content들도 body로 구성이 가능하다.

  *Body 안에 다른 타입 집어넣기*

  ```html
  <body>
      <p>
          What's up, doc?
      </p>
  </body>
  ```

  *예제*  (<p>,</p> 없이 그냥 <body>,</body>만 써도 출력이 되긴 함)

  ```html
  1. body element를 생성해보자
  2. opening and closing body 사이에 원하는 말을 집어넣자.
  <body>
  	<p>
      "잠은 오고 할 건 많고, 영화나 보고 잘까"
      </p>    
  </body>     
  ```

- HTML 구조 : HTML은 family tree relationships의 집합체로 구성되있다고 한다. (뭔소리야)  위의 예제에서 <body> tags 안에 <p> tags를 집어넣었는데 요소안에 다른 요소를 집어 넣으면 애기 요소라고 여겨진다. parent element 안에 nested 되었다 라고 불려짐

  *예제* 

  ```html
  <body>
      <p>
          This paragraph is a child of the body
      </p>
  </body>
  ```

  위의 예제에서 보면 <p> element가 <body> element 안에 nested 되었죠? <p>가 <body> 애기로 여겨지고 <body>는 부모다. 애기 낳는 건 얼마든지 할 수 있다. 할머니가 될 수 있고 할머니의 할머니를 만들 수도 있다.

  *심화 예제*

  ```html
  <body>
      <div>
          <h1>
              Sibling to p, but also grandchild of body
          </h1>
          <p>
              Sibling to h1, but also grandchild of body
          </p>
      </div>
  </body>
  ```

  위의 예제를 보면 <body> element는 <div> elemnet의 부모다. <h1>와 <p> elements는 <div>의 자식들이다. 왜냐면 둘다 같은 레벨에 있거든 (같은 들여쓰기라서) 그리고 얘들 <h1>와 <p>는 <body>의 손자 손녀다.

  HTML 계급을 이해하는게 되게 중요한데, 애기 elements들이 부모 element에게 상속 받을 수 있다. CSS 배울 때  webpage 계급을 배울 것이다.

  *예제 div 애기로 문단을 넣어봐*

  ```html
  <body>
      <h1>
          Hello World
      </h1>
      <div>
          <p>
              This paragraph is a child of the div element and a grandchild of the body element
          </p>
      </div>
  </body>
  ```

- Headings : HTML 안에서 Headings은 뉴스의 헤드라인이랑 유사하다. 읽는 사람 주의를 확 끌어와야 하거든, 혹은 영화, 교육 기사의 타이틀로 사용하기도 한다. HTML에서는 6개의 다른 headings or headings elements가 있다.

  ```python
  <h1> #제일 큰 글자
  <h2>
  <h3>
  <h4>
  <h5>
  <h6> #제일 작은 글자
  ```

  *예제*

  ```html
  <hi>BREAKING NEWS</hi>
  ```

  *예제 <h3> 밑에 <h2> Habitat를 삽입해봐, 했으면 Habitat 밑에 Countries with Larrge Brown Bear Populations을 넣어봐, 했으면 그 다음 줄에 <h3> Countries with Small Brown Bear Populations을 넣어봐, 했으면 마지막으로 그 밑에 <h2> Media를 넣어봐*

  ```html
  <body>
      <h1>
          The Brown Bear
      </h1>
      <h2>
          About Brown Bears
      </h2>
      <h3>
          Species
      </h3>
      <h3>
          Features
      </h3>
      <h2>
          Habitat
      </h2>
      <h3>
          Countries with Large Brown Bear Populations
      </h3>
      <h3>
          Countries with Small Brown Bear Populations
      </h3>
      <h2>
          Media
      </h2>
  </body>
  ```

- Divs : HTML 연예인 <div> element. <div>는 'division'의 줄임말이고 섹션으로 나눈 페이지를 담는 애다. 이러한 섹션은 grouping elements를 하는데 매우 유용하다.

  *예제*

  ```html
  <body>
      <div>
          <h1>
              Why use divs?
          </h1>
          <p>
              Great for grouping elements!
          </p>
      </div>
  </body>
  ```

  div 얘는 비디오, 사진, text 같은 HTML elements를 담을 수 있다. 두개의 들여쓰기 elements를 nest 할 때 div 안에다가 하는 것이 가독성이 좋다.

  *예제 읽기 좋게 나누기*

  ```html
  <body>
      <div>
      	<h1>
          	The Brown Bear
      	</h1>
      	<h2>
          	About Brown Bears
      	</h2>
      	<h3>
          	Species
      	</h3>
      	<h3>
          	Features
      	</h3>
      </div>
      <div>
      	<h2>
          	Habitat
     		</h2>
      	<h3>
          	Countries with Large Brown Bear Populations
      	</h3>
      	<h3>
          	Countries with Small Brown Bear Populations
      	</h3>
      </div>
      <div>
      	<h2>
          	Media
      	</h2>
      </div>
  </body>
  ```

- 속성 : 우리가 element's tag를 확장하고 싶으면 속성을 사용하면 된다.  Opening tag에서 추가되고 2가지 파트가 있다.

  1. 이름
  2.  값

  주로 쓰는 건 id 이다. 다른 content를 명시하기 위해서 id를 쓰고 하나 이상의 div를 쓸 때 크게 도움이 된다. 그리고 많은 용도로 쓰이기도 하는데 우리는 지금 구분 짓는데만 초점을 둬보겠다.

  *예시* 

  ```html
  <div id="intro">
      <h1>
          Itroduction
      </h1>
  </div>
  ```

  *예시*

  ```html
  <body>
      <h1>
          The Brown Bear
      </h1>
       <div id = "introduction">
      	<h2>
          	About Brown Bears
      	</h2>
      	<h3>
          	Species
      	</h3>
      	<h3>
          	Features
      	</h3>
      </div>
      <div id = "habitat">
      	<h2>
          	Habitat
     		</h2>
      	<h3>
          	Countries with Large Brown Bear Populations
      	</h3>
      	<h3>
          	Countries with Small Brown Bear Populations
      	</h3>
      </div>
      <div id = "media">
      	<h2>
          	Media
      	</h2>
      </div>
  </body>
  ```

- 텍스트 보여주기 : HTML 안에 있는 텍스트를 보여주기 위해서 span 구문을 쓴다.

  - p 가 정제된 text를 담고 있다.
  - span이 HTML 혹은 문장의 작은 부분을 담고 있다. 얘들은 한 줄에 있는 애들도 다른 애들로 구분지을 수 있다.

  *예시*

  ```html
  <div>
      <h1>
          Technology
      </h1>
  </div>
  <div>
      <p>
          <span>Self-driving cars</span> are anticipated to replace up to 2 million jobs over the next two decades.
      </p>
  </div>
  ```

  위에 예시에서 2개의 div가 있다. 두번째 div에서 p가 있구 span도 있는데 span은 "Self-driving cars"를 나머지 문장에서 구분 지어줬다.

  span의 가장 좋은 방법은 하나의 문장 혹은 라인에서 명확하게 타게팅하고 싶을 때 쓰는 것인데, 블록으로 나누는 걸 원하면 div 쓰셈

  *예시*

  ```html
  <body>
      <h1>
          The Brown Bear
      </h1>
       <div id = "introduction">
      	<h2>
          	About Brown Bears
      	</h2>
           <p>
               The brown bear (Ursus arctos) is native to parts of northern Eurasia and North America. Its conservation status is currently Least Concern. There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear."
           </p>
      	<h3>
          	Species
      	</h3>
      	<h3>
          	Features
      	</h3>
           <p>
               "Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe. "
           </p>
      </div>
      <div id = "habitat">
      	<h2>
          	Habitat
     		</h2>
      	<h3>
          	Countries with Large Brown Bear Populations
      	</h3>
      	<h3>
          	Countries with Small Brown Bear Populations
      	</h3>
          <p>
              "Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan."
          </p>
      </div>
      <div id = "media">
      	<h2>
          	Media
      	</h2>
      </div>
  </body>
  ```

- 텍스트 스타일 : em으로 텍스트를 강조하고 strong으로 하이라이트 줄 수 있다. 웹 디자인 할 때 em, strong을 쓸건데 em은 italic이고 strong은 bold이다.

  *예제*

  ```html
  <p>
      <strong>The Nile River</strong> is the <em>longest</em> river in the world, measuring over 6,850 kilometers long (approximately 4,260 miles).
  </p>
  ```

  *예제*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
    </div>
  </body>
  ```

- Line Breaks : \n과 같은 역할을 하는애가 br이다.  얘는 신기한게 오직 opening tag만 가지고 있다.

  *예제*

  ```html
  <p>
      The Nile River is the longest river <br> in the world, measuring over 6,850 <br> kilometers long (approximately 4,260 <br> miles).
  </p>
  ```

  *예제*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
    </div>
  </body>
  ```

- Unordered Lists : ul을 사용하면 특별한 순서 없는 리스트를 만들 수 있다. 각각의 리스트 아이템들은 bullet point를 가지고 있다. 리스트 아이템들은 그냥 못옴. li tag를 가지고 들어와야함.

  *예시* 

  ```html
  <ul>
      <li>Limes</li>
      <li>Tortillas</li>
      <li>Chicken</li>
  </ul>
  
  결과값
  ● Limes
  ● Tortillas
  ● Chicken
  ```

  위에 예시에서 ul tag를 만들었고 전부 li tag를 붙혔다.

  *예시*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
    </div>
  </body>
  ```

- Ordered Lists : 숫자가 정해진 리스트 나머지는 Unordered lists랑 같다. ol을 사용한다.

  *예시*

  ```html
  <ol>
      <li>Preheat the oven to 350 degrees.</li>
      <li>Mix whole wheat flour, baking soda, and salt.</li>
      <li>Cream the butter, sugar in sparate bowl.</li>
      <li>Add eggs and vanilla extract to bowl.</li>
  </ol>
  
  결과값
  1. Preheat the oven to 350 degrees.
  2. Mix whole wheat flour, baking soda, and salt.
  3. Cream the butter, sugar in separate bowl.
  4. Add eggs and vanilla extract to bowl.
  ```

  *예시*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
            <li>Russia</li>
            <li>United States</li>
            <li>Canada</li>
        </ol>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
    </div>
  </body>
  ```

- 사진 : 지금까지 배운 애들은 전부 text다 ! 근데 사진좀 넣어볼까 ? img tag가 사진 넣는데 도와줄거얌. 대부분 애들이 opening tag, closing tag 두개 다 필요한데 img tag는 좀 다르고 img tag는 마지막에 / 만 추가해주면 됨.

  *예시*

  ```html
  <img src="image-location.jpg"/>
  ```

  마지막에 / 넣어주면 됨, 생략해두 되구

  img 얘는 src를 attribute(속성)을 가지고 오는데 image 파일의 소스, 위치라고 생각하면 된다.

  *예시*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
            <li>Russia</li>
            <li>United States</li>
            <li>Canada</li>
        </ol>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
        <img src = "https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg"/>
    </div>
  </body>
  ```

- Image Alts : alt 속성은 text 대안이다. 이미지의 뜻을 가져오는 애인데 img tag에 그냥 추가할 수 있다.

  *예시*

  ```html
  <img src="#" alt="A field of yellow sunflowers"/>
  ```

  alt의 목적으론

  1. 이미지 불러오는거 실패하면 유저가 alt 속성으로 알 수 있다.
  2. 보기 좋다.
  3. 검색이 된다.

  *예시*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
            <li>Russia</li>
            <li>United States</li>
            <li>Canada</li>
        </ol>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
        <img src = "https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg" alt = "very horrible bear"/>
    </div>
  </body>
  ```

- Videos : video tag로 비디오도 넣을 수 있다. src가 필요하고 img tag와는 다르게 얘는 closing tag가 필요하다.

  *예시*

  ```html
  <video src="myVideo.mp4" width = "320" height = "240" controls> 
      Video not supported
  </video>
  ```

  위의 예시에서 src가 있는데 URL로도 사용 가능하다. width와 height로 사이즈도 꾸릴 수 있다. controls은 비디오에 pause, play, skip 기능을 포함시키는거임. Video not supported는 브라우저가 비디오 끌고 못 오면 보여주는 애다.

  *예시*

  ```html
  <body>
    <h1>The Brown Bear</h1>
    <div id="introduction">
      <h2>About Brown Bears</h2>
        <p>The brown bear (<em>Ursus arctos</em>) is native to parts of northern Eurasia and North America. Its conservation status is currently <strong>Least Concern.</strong> <br><br> There are many subspecies within the brown bear species, including the Atlas bear and the Himalayan brown bear.</p>
      <h3>Species</h3>
      <h3>Features</h3>
      <p>Brown bears are not always completely brown. Some can be reddish or yellowish. They have very large, curved claws and huge paws. Male brown bears are often 30% larger than female brown bears. They can range from 5 feet to 9 feet from head to toe.</p>
    </div>
    <div id="habitat">
      <h2>Habitat</h2>
      <h3>Countries with Large Brown Bear Populations</h3>
        <ol>
            <li>Russia</li>
            <li>United States</li>
            <li>Canada</li>
        </ol>
      <h3>Countries with Small Brown Bear Populations</h3>
      <p>Some countries with smaller brown bear populations include Armenia, Belarus, Bulgaria, China, Finland, France, Greece, India, Japan, Nepal, Poland, Romania, Slovenia, Turkmenistan, and Uzbekistan.</p>
    </div>
    <div id="media">
      <h2>Media</h2>
        <img src = "https://s3.amazonaws.com/codecademy-content/courses/web-101/web101-image_brownbear.jpg" alt = "very horrible bear"/>
        <video src = "https://s3.amazonaws.com/codecademy-content/courses/freelance-1/unit-1/lesson-2/htmlcss1-vid_brown-bear.mp4 width = "320" height = "240" controls>
        Video not supported
        </video>
    </div>
  </body>
  ```

- 정리 

  1. HTML : Hyper Text Markup Language 이고 웹페이지 만들 때 사용된다.
  2. 대부분 elements 들은 opening tag와 closing tag를 가지고 있다. 그리고 그 사이엔 raw text 혹은 다른 HTML tag를 가지고 있다.
  3. HTML elements는 애기를 나을 수 있다.
  4. content 들은 body tag로 놓여질 수 있다.
  5. 글씨 크기는 h1 에서 h6 tag로 표현이 가능하다
  6. p, span, div tags 는 텍스트 혹은 블록을 나누는데 사용된다.
  7. em, strong 은 글씨 체를 표현한다
  8. br는 /n과 같은 역할을 한다
  9. ul은 순서 없이 나열 ol은 순서 가지고 나열한다.
  10. img, video로 링크를 연결해서 보여줄 수 있다.