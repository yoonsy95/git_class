import requests
from decouple import config

# API 요청 기본사항
url='https://api.telegram.org'

# python-decouple
# 유출 방지 위하여 환경변수 만듦 => .env // 띄어쓰기 금지
# token='769483976:AAEJQsJkzcNww_yCCUz2zdfHO3DJwv2Tl00'
token=config('TELEGRAM_BOT_TOKEN')

# 봇과 대화하고 있는 사용자 CHAT_ID 추출
# chat_id=requests.get(f'{url}/bot{token}/getUpdates').json()['result'][0]['message']['from']['id']
chat_id=config('CHAT_ID')

# 보낼 메세지 입력받기
text= input('input message: ')

# API에 요청을 보내 메세지 보내기
send_message=requests.get(f'{url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)



