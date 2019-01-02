# Day03

## 연습문제

1. ```python
   str = input('문자를 입력하세요')
   
   a = str[0]
   b = str[-1]
   print(a+b)
   ```

2. ```python
   #문제 2.
   #자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
   
   number = int(input('숫자를 입력하세요: '))
   for i in range(number):
       print(i+1)
   
   i=0
   while i < number:
       print(i+1)
       i+=1
    
   cf)입력 받은수 쪼개서 큰 순서대로 출력
   
   while True:    
       print(number%10)
       number = number//10
       if number %10 ==0:    
           break   
   ```

3. ```python
   #홀짝 구분
   number = int(input('숫자를 입력하세요'))
   
   if number%2 ==0:
       print('짝수입니다')
   else:
       print('홀수입니다') 
   ```

4. ```python
   # 문제 4.
   # 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
   # 국어는 90점 이상,
   # 영어는 80점 초과,
   # 수학은 85점 초과, 
   # 과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
   # 다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
   
   a = int(input('국어: '))
   b = int(input('영어: '))
   c = int(input('수학: '))
   d = int(input('과학: '))
   # 1.
   if a>=90 and b>80 and c>85 and d>=80:
       print("True")
   else:
       print("False")
   
   
   # 2.
    if a<90 or b<=80 or c<=85 or d<80:
        print("False")
    else:
        print("True")
   
   # 3.
   print(a>=90 and b>80 and c>85 and d>=80)
   ```

5. ```python
   # 문제 5.
   # 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
   # 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
   # # 입력 예시: 300000;20000;10000
   # '''
   
   prices = input('물품 가격을 입력하세요: ')
   a=prices
   b=a.split(';')
   
   b = list(map(int, b))
   # #1. b = [int(i) for i in b]
   # #2. for i in range(len(b)):
   #       b[i] = int(b[i])
   # 3.
   #int_price = []
   #for i in b:
   #    int_price.append(int(i))
   #
   
   b.sort()
   #b=sorted(b,key=int)
   #sorted는 소트 후 새로운 리스트를 리턴한다는 점이고 리스트 자체의 sort함수는 리스트 그 자체를 소트시킨다는 점이 다르다.
   b.reverse()
   # #b.sort(reverse=True) 가능
   print(b)
   
   #Chain, 가독성 낮아짐
   #sorted_price = sorted(list(map(int, b)), reverse=True)
   
   
   ```



## HTML

* index.html 파일 생성(확장자.html)
* 연습
* HTML:5 입력하면 form  자동 생성

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>HTML 실습</title>
    <style>
        h1,h3 {
            color: red;
        }  
        h2 { 
            color: aqua;
        }
        
        #green {
            color:green;
        }
        .yellow { 
            color: yellow;
        }  
    </style>
</head>
<body>
    <!-- ctrl+/로 주석 만들기
         여러줄 가능합니다.
    -->
    <h1>이것은 h1 태그입니다.</h1>
    <h2>이것은 h2 태그입니다.</h2>
    <h3>이것은 h3 태그입니다.</h3>
    <h4 id="green">이것은 h4 태그입니다.</h4>
    <h5 class="yellow">이것은 h5 태그입니다.</h5>
    <h6 class="yellow">이것은 h6 태그입니다.</h6>
<!-- css우선순위 : inline > id > class > tag -->
    <p style="color: pink;">
        이것은 p 태그입니다. <br>
        이것은 p 태그입니다. <br>
        이것은 p 태그입니다.
        이것은 p 태그입니다.
    </p>

    <ul>
        <li>리스트 1번째</li>
        <li>리스트 2번째</li>
        <li>리스트 3번째</li>
    </ul>

    <ol>
        <li>리스트 1번째</li>
        <li>리스트 2번째</li>
        <li>리스트 3번째</li>
    </ol>

    <div>
        <b>여기는 div입니다.</b>
        <i>여기는 div입니다.</i> 
        <b>w3school로 html tag 정보 얻어 가세요</b>
    </div>


    </h2>
    <div>
<!-- 이미지 삽입 -->
    <img src="./dog.jpg" alt="개 이미지입니다." width="300px" height="300px">
    </div>
    <!-- 이미지 url -->
    <img src="https://d81pi4yofp37g.cloudfront.net/wp-content/uploads/python-1.png" alt="파이썬 로고입니다." width="300px" height="300px">
</body>
</html>
```



## BootStrap



## FLASK

* pip install flask
* mysite 폴더 생성
* GitBash에서 cd mysite까지 설정 후
* FLASK_APP=hello.py flask run

```python
from flask import Flask, render_template
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
```



## Templates 폴더 생성

* hi.html

```html
<style>
    h1{
        color: blue;
    }
</style>

<h1>만나서 반갑습니다! {{name_in_html}} 님!</h1>
```



* html_file.html

```html
<h1>여기는 h1! h1!</h1>
<p> 여기는 p1! p1!</p>
```



* fake_naver.html

```html
<h1>네이버</h1>
<form action='https://search.naver.com/search.naver'>
    <input type="text" name="query">  <!--query= 검색값, name 값이 action에서 돌아감 -->
    <input type="submit">
</form>

<h1>다음</h1>
<form action='https://search.daum.net/search'>
    <input type="text" name="q">
    <input type="submit">
</form>
```

