# 1월 4일 숙제 - OS & Command Line Interface

### 학습해야 할 내용

- CLI (Command Line Interface) 기본 명령어
- 파일 및 디렉토리 조작



#### 1. True / Fasle

1. windows 와 unix 계열 운영체제는 CLI(Command Line Interface) 에서 같은 명령어를 사용한다. [X]

   ```
   다릅니다 !!
   windows에서 현재 위치의 파일 리스트를 보려면 dir
   unix에서는 ls를 사용한다.
   ```

2. 우리가 사용하는 컴퓨터는 windows 이므로, unix 계열 운영체제 명령어를 학습할 필요가 없다. [X]

   ```
   공부해야 합니다 !!
   개발자는 unix 계열 운영체제를 사용할 일이 많습니다. 미래의 개발자를 꿈 꾸는 우리이기에 공부를 해야하며 windows에서도 unix 명령어들을 사용할 수 있게 해주는 git bash도 있기에 공부해야합니다 !
   
   git bash(Bourne Again SHell)
   ```

3. CLI(Command Line Interface)는 결국 컴퓨터를 조작하기 위해 사용하는 것이다. [O]

   ```python
   CLI(Command Line Interface)로 파일도 만들 수 있고, 폴더도 만들 수 있고 들어가고 나가고 리스트 확인하고 하는 거 보면 컴퓨터를 조작하기 위한 명령어임을 알 수 있습니다 !!
   ```

4. CLI(Command Line Interface)를 통해서 바탕화면에 새로운 파이썬 파일(.py)을 생성할 수 있다. [O]

   ```python
   만들 수 있습니다 !!!
   mkdir(폴더 생성), touch(파일 생성), cd(특정 폴더로 이동), ls(목록 출력)과 같은 명령어로 수행할 수 있습니다.
   cd Desktop
   touch Python.py를 하면 생성 되었습니다 !!
   ```



#### 2. 다음 unix 명령어들에 대하여 간략하게 기술하세요.

1. ls

   ```
   ls는 현재 위치의 폴더에서 목록(list)을 알려주는 명령어 입니다 !! 단, 숨김파일 및 숨김폴더는 보여주지 않습니다. 파일, 폴더명 앞에 '.'이 존재하는 숨김파일 및 숨김폴더를 보기 위해선 ls -a 이라는 명령어를 사용해야합니다.
   ```

2. cd

   ```
   cd(Change Directory)의 명령어는 unix에서 특정 폴더(directory)로 이동하는 명령어입니다 ! (윈도우에서도 같은 명령어 입니다.)
   참고로 cd ~ 명령어를 사용하면 처음 폴더로 돌아가고
   cd ..을 사용하면 이전 폴더로 이동합니다
   또한 초기 사용자 폴더에서 cd desktop 명령어를 사용하면 바탕화면으로 이동합니다.
   ```

3. mkdir

   ```
   원하는 이름의 폴더를 생성해주는 명령어 입니다 !!
   ```

4. touch

   ```
   원하는 이름의 파일을 생성해주는 명령어 입니다 !!
   파일명 뒤에 확장자를 추가할 수 있으며 확장자에 따라 파일의 종류가 달라집니다 !
   ```



#### 3. CLI(Command Line Interface)와 익숙해지게 되면, Tap 키를 매우 빈번하게 사용하게 됩니다. 그 이유는 무엇일까요? (git bash 를 켜고 cd Desk 까지만 입력 후 탭 키를 눌러 봅시다 !)

```
그 이유는 자동 문장 완성을 지원해주기 때문입니다 !!
cd Desk 에서 Tab 키를 눌렀다면 cd Desktop/까지 자동으로 문장을 완성시켜주기 때문에 매우 편리합니다 !!

ex) my_software_study라는 하위 폴더로 이동하고싶다.
cd my_soft + (Tab)
cd my_software_study 까지 자동 완성
 
굿 !
```

