# Weather_Forecast_


### 🖥️ 프로젝트 소개
- tkinter, beautifulsoup, selenium를 이용해 날씨를 알 수 있게 만든 프로그램

### 🕰️ 개발 기간
- 23.11.09일   ~   23.12.07일

### ⚙️ 개발 환경
- `python 3.11`
- **IDE** : Visual Studio Code

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


### 😥beautifulsoup과 selenium을 동시에 사용한 이유
request.text를 이용해 가져온 데이터는 사이트의 텍스트형태의 html 입니다.
이런 데이터에서 원하는 부분만 추출하기 위해 우리는 beautifulsoup를 사용할 것 입니다

### 📌 주요 기능

사진
![main](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/a044e495-8b53-49a4-aee7-1897ffa0df95)
![result](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/ad994fba-e9f2-40b3-a8c1-8662238eced7)
![weekly](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/971f58ac-a1db-46c3-a11d-17bf5a3a50f2)
![if_rain](https://github.com/EndlessCreation/Web_basic_study_2021-1/assets/68912105/849dfba7-a868-44cc-bd0c-98d53f165fa9)

### 📚 참조

* tkinter 사용법: <https://076923.github.io/posts/Python-tkinter-1/>

* beautifulsoup 및 request 사용법: <https://pythonblog.co.kr/coding/10/>

* 크롤링 특정 영역 화면 캡쳐하기: <https://youtube.com/watch?v=DKt3UdWHNSw&t=1097s>
