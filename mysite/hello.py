import random
import requests
from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ssafy")
def ssafy():
    return "This is SSAFY!"

@app.route("/greeting/<string:name>")
def greeting(name):
    return f'반갑습니다!{name}님'

@app.route("/cube/<int:num>")
def cube(num):
    cube = num**3 
    return f'{num}의 세제곱은 {cube}입니다.'

@app.route("/lunch/<int:person>")
def lunch(person):
    menu = ['고등어 순살 조림', '해물 소스 비빔', '곰탕', '쇠소기 미역국', '코다리 조림', '햄소세지 찌개']
    order = random.choice(menu)
    tomorr = random.sample(menu,person)
    return f'오늘 메뉴는 {order}입니다! 내일은 {tomorr} 중 하나가 나옵니다!'

@app.route("/html")
def html():
    multiline_string='''
    <h1>이것은 h1입니다</h1>
    123
    123
    <p1>ㅎㅇ</p1>
    '''
    return multiline_string

@app.route("/html_file")
def html_file():
    return render_template('html_file.html')

@app.route("/hi/<string:name>")
def hi(name):
    return render_template('hi.html', name_in_html=name)


@app.route("/fake_naver")
def fake_naver():
    return render_template('fake_naver.html')    


#Day04
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args['name']
    result = random.choice(['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png'])
    return render_template('pong.html', name_in_html=name, result=result)


@app.route('/lotto/<int:num>')
def lotto(num):
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    response = requests.get(url)
    lotto = response.json()

    winner=[]
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])

    bonus = lotto['bnusNo']    
    return render_template('lotto.html', w=winner, b=bonus, n=num)    