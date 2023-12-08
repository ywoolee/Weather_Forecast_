# Weather_Forecast_


### 🖥️ 프로젝트 소개
- tkinter, beautifulsoup, selenium를 이용해 날씨를 알 수 있게 만든 프로그램

-----------------------------

### 🕰️ 개발 기간
- 23.11.09일   ~   23.12.09일

-------------------------------  

### ⚙️ 개발 환경
- `python 3.11`
- **IDE** : Visual Studio Code

------------------------------------------

### 📋 실행하기에 앞서 해야되는 것
 1. tkinter 설치
Python에서 GUI를 직접 만들 수 있도록 해주는 library인 tkinter를 먼저 설치해줘야합니다.
설치방법은 아래 코드를 terminal에 그대로 작성하시면 설치가 됩니다.
    ```python
    pip install tk
    ```
    
2. beautifulsoup 설치
beautifulsoup또한 tkinter와 동일하게 아래의 코드를 terminal에 그대로 작성하시면 됩니다.
    ```python
    pip install beautifulsoup4
    ```

3. selenium설치
    selenium도 위의 기능들과 같이 아래의 코드를 그대로 작성하시면 설치 가능합니다.
    ```python
    pip install beautifulsoup4
    ```
    
4. 파일 위치 설정
    selenium으로 주간 날씨에 대한 스크린 샷을 저장하기 떄문에 저장 위치가 중요합니다.
    github에 있는 weather파일을 모두 다운받아 바탕화면에 weather파일을 두면 됩니다.


-------------------------------

### 📌 사용 방법

1. weather파일에 있는 weather.py파일을 열고 실행시킵니다.

2. 실행하게 되면 아래의 사진과 같은 창이 나오게 됩니다.
![main](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/a044e495-8b53-49a4-aee7-1897ffa0df95)

3. 조회하고 싶은 도시를 "한글"로 입력하고 검색버튼을 누릅니다.
3.1. 만약 "도시의 이름을 입력하세요."라고 나와있는 칸을 건드리지 않거나 아무것도 입력하지 않고 검색을 하게된다면 
아래 사진과 같은 오류창이 뜨게 됩니다.
![error](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/a8e2e468-e13f-497b-b70a-81528ef405d0)

    3.2. 도시를 잘 입력하고 날짜를 잘 선택해서 검색을 누르게 된다면 아래 두 사진처럼 일기예보를 볼 수 있습니다.
![result](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/ad994fba-e9f2-40b3-a8c1-8662238eced7)
![if_rain](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/849dfba7-a868-44cc-bd0c-98d53f165fa9)

4. 3번과 동일하게 도시를 입력하고 주간 날씨를 누르게 되면 크롬창이 실행되면서 주간날씨에 대한 정보를 수집합니다. 
이 과정을 지나게 되면 새로운 창이 켜지며 해당 도시의 주간날씨를 보여줍니다.
![weekly](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/971f58ac-a1db-46c3-a11d-17bf5a3a50f2)

5. 창을 끄고싶다면 종료버튼을 누르면 창이 꺼지게 됩니다.

--------------------------------

### 💬코드 설명

-------------------------------------

### ❓beautifulsoup과 selenium
- beautifulsoup과 selenium은 모두 웹의 html요소를 파이썬으로 가져오는 역할을 합니다.

- 이 둘의 차이점이라고 한다면 beautifulsoup는 requests라이브러리를 이용해 웹의 정보를 바로 받아서 데이터를 파싱해 정적 수집을 하지만
seleium의 경우 selenium과 chromedriver를 이용해 웹을 열고 브라우저를 받아 동적 수집을 할 수 있습니다. 
따라서 beautifulsoup과 selenium보다 상대적으로 더 빠릅니다. 

- 이 프로젝트에서 두가지 모두를 사용하게 된 이유는 일일 날씨의 경우 빠르게 날씨와 기온만을 빠르게 보는 것에 중점을 두어 스크린샷보다 데이터를 얻는 속도가 빠른 텍스트로 표현하기 위해 beautifulsoup사용했고 주간 날씨의 경우 네이버의 주간에보탭의 정보가 충분히 좋고 보기 쉽게 되어있다고 판단해 스크린샷으로 찍어서 보여주는 것이 더 효과적이라고 생각을 해서 selenium을 이용했습니다

--------------------------------------

### 📚 참조

* tkinter 사용법: <https://076923.github.io/posts/Python-tkinter-1/>

* beautifulsoup 및 request 사용법: <https://pythonblog.co.kr/coding/10/>

* 크롤링 특정 영역 화면 캡쳐하기: <https://youtube.com/watch?v=DKt3UdWHNSw&t=1097s>

