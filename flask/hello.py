from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python') #무조건 /로 시작
def python():
    return 'Python is fun!'

@app.route('/dictionary/<string:word>') #<>로 variable 지정, string=>문자열만 가능
def dictionary(word): #() 안에 변수 입력 필수
    dictionary ={
        'apple':'사과',
        'banana':'바나나',
        'pear':'배',
        'watermelon':'수박'
    }
    result = dictionary.get(word,'나만의 단어장에 없는 단어입니다.') #dictionary['word']로 할 시 키값이 없을 떄 오류가남, .get은 None 반환
    return f'{word}(은)는 {result}!'