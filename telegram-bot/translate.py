import requests
from decouple import config

url='https://translation.googleapis.com/language/translate/v2'
key=config('GOOGLE_TOKEN')
data={
    'q': '엄마 판다는 새끼가 있네',
    'source': 'ko',
    'target': 'en'
}
result=requests.post(f'{url}?key={key}',data).json()
print(result)

# result.get('data').get('translations')[0].get(translatedText)



# 웹훅주소:  https://api.telegram.org/bot769483976:AAEJQsJkzcNww_yCCUz2zdfHO3DJwv2Tl00/setWebhook?url=https://yunsy.pythonanywhere.com/769483976:AAEJQsJkzcNww_yCCUz2zdfHO3DJwv2Tl00