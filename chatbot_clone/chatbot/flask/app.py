import random
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

# python fileName으로 호출

# @app.route('/')
# def hello_world():
#     return '어서와'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/mulcam')
def mulcam():
    return '20층 스카이라운지'

@app.route('/dday')
def dday():
    today=datetime.now()
    new_year=datetime(2020,1,1)
    result = new_year-today
    return f'한 살 더 먹기까지: <b>{result.days}</b>일'

# 사용자 이름을 돌려주는 페이지
# @app.route('/greeting/<string:name>')
# def greeting(name):
#     return f'반갑습니다 {name}님'
@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html',html_name=name)

# 세제곱 결과를 돌려주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result=number ** 3
    return render_template('cube.html', number=number,result=result)

# 인원수에 맞게 메뉴를 추천해주는 페이지
@app.route('/lunch/<int:people>')
def lunch(people):
    menu=['보쌈수육정식','고추참치덮밥','돼지불백','샐러드','히레카츠']
    
    order=random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies=['나이브스 아웃','조커','엔드게임']
    return render_template('movie.html',movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age=request.args.get('age')
    return render_template('pong.html',age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력받을 페이지를 랜더링해줌
@app.route('/vonvon')
def concon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def gotmademe():
    name=request.args.get('name')
    # data list
    first_options=['잘생김','못생김','졸잘','자상함','순수함']
    second_options=['귀찮음','친절함','애교','의리']
    third_options=['똘끼','돈복','코딩력','식욕']

    # 각 데이터 리스트 요소 하나씩 무작위로 뽑음
    # random.sample: list 형태로 들어옴
    first=random.sample(first_options, 1)
    # random.choice: str
    second=random.choice(second_options)
    third=random.choice(third_options)

    
    
    return render_template('godmademe.html',name=name,first=str(first[0]), second=str(second), third=str(third))

# app.py 가장 하단 위치
# 1. 앞으로 flask run으로 서버 켜는게 아니라
#    python app.py로 버버 실행한다
# 2. 내용이 바뀌어도 서버를 껐다 켜지 않아도 된다.
if __name__ == '__main__':
    app.run(debug=True)