## 파이썬 챗봇 만들기

### 1. 개발환경 세팅

#### 1.1 프로젝트 폴더 및 .gitignore 생성

```
telegramChat/
	.gitignore
```

- .gitignore.io에서 Visual Studio Code, Python, Flask, venv 를 선택해서 생성한 뒤 `.gitignore` 파일에 복사 붙여넣기

#### 1.2 가상환경 생성 및 진입

- **가상환경 만들기**

  ```bash
  ~/Desktop/telegramChat
  $ python -m venv venv
  ```

  ```
  telegram-bot
  	venv/
  	.gitignore
  ```

  

- **가상환경 진입**

  ```bash
  ~/Desktop/telegramChat
  $ source venv/Scripts/activate
  ```

- **VSCode 자동 가상환경 진입 설정**

  - 이 옵션을 설정하느 경우 반드시  `.vscode`폴더가 있는 디렉토리에서 open with code 혹은 open folder로 진입을 해야 터미널을 새로 켤 때 자동으로 가상환경 진입이 된다.

  - 자동으로 가상환경이 켜지지 않으면 당황하지 않고 `source venv/Scripts/activate` 명령어를 직접 쳐서 가상환경에 집입하자

  - **`Ctrl + Shift + P` -> Python: Select interpreter venv -> 사용할 환경 선택**

  - 설정이 완료되면 .vscode 폴더가 생성된다.

    ```bash
    telegram-bot/
        .vscode/
        venv/
        .gitignore
    ```



#### 1.3 Flask 개발용 서버 실행

##### 1.3.1 Flask 공식문서로 시작하기

반드시 가상환경 진입 여부를 확인하고 설치하자. 명령어 좌상단의 (venv)

```bash
(venv)
$ pip install Flask
```

```python
# telegram-bot/app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```



##### 1.3.2 서버 실행을 간편하게

공식문서에 있는대로 flask run 명령어를 수행하면 서버가 실행된다. 하지만 이 경우엔 app.py의 내용을 수정하면 서버를 재실행해야 반영된다. 따라서 코드를 추가해서 이를 방지하자

```python
# telegram-bot/app.py

from flask import Flask
app=Flask(__name__)
...
...

# 반드시 파일 최하단에 위치해야 함
if __name__ == '__main__':
    app.run(debug=True)
```

```bash
(venv)
~/Desktop/telegram-bot
$ python app.py
```



### 2. Telegram 봇 생성 및 요청 보내보기

#### 2.1 봇 만들기

- BotFather -> newbot -> name 입력 -> username 입력
- 토큰값 임시 저장하기 in 메모장

#### 2.2 요청 보내보기

- **요청**

  `getMe` 메소드를 사용해서 내 봇에 대한 정보를 받아온다

  ```
  https://api.telegram.org/bot<Token>/getMe
  ```

  

- **결과값**

```json
{
    "ok": true,
    "result": {
            "id": 769483976,
            "is_bot": true,
            "first_name": "first",
            "username": "firstfirstfirstfirst_bot"
    }
}
```





### 3. 사용자에게 메세지 보내기

#### 3.1 사용자의 ID 값 알아내기

> 사용자에게 메세지를 보내려면 사용자의 고유한 ID 값을 알아낸다



#### 3.2 메세지 보내기

```python
# send_message.py
```





#### 3.3 Flask로 메세지 보내기

```python
# app.py
```



### 4. ngrok

> 우리의 Flask 서버는 현재 로콜환경에서 개발용 서버로 작동하고 있다.
> 그래서 텔레그램 측에 웹훅을 정용하기 위해 주소를 알려주더라도 텔레그램 측에서 우리 서버 주소로 접근을 할 수가 없다.(사내 인트라넷에 글 올려놓고 부모님께 접속해보라고 링크 던져주는 것과 마찬가지인 상황)
>
> 이를 해결하귀 위해 로컬 서버 주소를 임시로 public하게 열어주는 툴인 엔그록(ngrok)을 사용해보자

#### 4.1 설치 파일 및 파일 배치

- [ngrok 공식 홈페이지](https://ngrok.com/download)

- 압축불기 -> ngrok.exe



#### 4.2 서버 실행



