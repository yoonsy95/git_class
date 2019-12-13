import requests, pprint, random
from flask import Flask, render_template, escape, request
from decouple import config

app = Flask(__name__)

url='https://api.telegram.org'
token=config('TELEGRAM_BOT_TOKEN')
chat_id=config('CHAT_ID')

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 텔레그램이 보내주는 데이터 구조 확인
    pprint.pprint(request.get_json())
    
    # 2. 사용자 아이디, 메시지 추출
    chat_id = request.get_json().get('message').get('from').get('id')
    message = request.get_json().get('message').get('text')
    # print(chat_id, message)


    # 사용자가 로또라고 입력하면 로또 번호 6개 올려주기
    if message == '로또':
        result = sorted(random.sample(range(1,46),6))

    # 그 외의 경우 메아리
    else:
        result = message


    # 3. 텔레그램 API에 요청해서 답장 보내주기
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')

    return '', 200

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    # 1. 사용자가 입력한 데이터 받아오기 // request -> flask
    message=request.args.get('message')

    # 2. 텔레그램 API 메시지 전송 요청 보내기 // requests -> python module
    requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')

    return render_template('write.html')

# @app.route('/writereply')
# def writereply():
#     return render_template('writereply.html')

# @app.route('/reply')
# def reply():
#     # 1. 사용자가 입력한 데이터 받아오기 // request -> flask
#     message=request.args.get('message')

#     chat_id=requests.get(f'{url}/bot{token}/getUpdates').json()['result'][-1]['message']['from']['id']

#     # 2. 텔레그램 API 메시지 전송 요청 보내기 // requests -> python module
#     requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={message}')

#     return render_template('writereply.html')





if __name__ == '__main__':
    app.run(debug=True)
