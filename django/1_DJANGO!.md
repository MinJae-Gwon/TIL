# DJANGO!

### 1. DJANGO Installation & START

```bash
pip install django
```

```bash
django-admin startproject intro .
#django 폴더에 manage.py 파일 생성 됨
```

```bash
#server 시작
(intro-venv) wabak:~/workspace/django/intro (master) $ python manage.py runserver $IP:$PORT
Performing system checks...

System check identified no issues (0 silenced).

You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

January 24, 2019 - 01:35:51
Django version 2.1.5, using settings 'intro.settings'
Starting development server at http://0.0.0.0:8080/
Quit the server with CONTROL-C.
```



##### [solving error]

http://0.0.0.0:8080/ 접속 후

```
Invalid HTTP_HOST header: 'playground-wabak.c9users.io:8080'. You may need to add 'playground-wabak.c9users.io' to ALLOWED_HOSTS. #오류 확인
```



DJANGO가 생성한 intro 폴더 내부 settings.py 접속 후

```
ALLOWED_HOST = [] #내부에 playground-wabak.c9users.io:8080 복사
```



##### [settings]

터미널에 아래 문구 삽입할 시

```
python manage.py startapp pages
```

pages 폴더가 생성 됨



settings.py 파일 내부에 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #추가
    'pages.apps.PagesConfig',
]
```



pages(APP) 폴더 내부에 templates 폴더 추가





### VIEWS

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
```

### URLS

```python
from django.contrib import admin
from django.urls import path
### 추가하기
from pages import views

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
]

```

### TEMPLATE

폴더 내부에 index.html 파일 생성



### RUNSERVER

```bash
(intro-venv) wabak:~/workspace/django/intro (master) $ pyton manage.py runserver $IP:$PORT
```





### 2. How django Works

##### [Random Dinner]

views.py에 함수 생성

```python
# Template variable
def dinner(request):
    menu = ['선산곱창','버거킹','와촌','지코바']
    pick = random.choice(menu)
    return render(request,'dinner.html',{'dinner':pick})
#변수는 dict 형태로 설정해야함
```



urls.py에 path 추가

```python
from django.contrib import admin
from django.urls import path
from pages import views
#중요!!
urlpatterns = [
    path('dinner/', views.dinner),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```



template 폴더에 dinner.html 생성

```html
<body>
    <h1>오늘 저녁은 {{ dinner }}</h1>
</body>
```



##### [Hello]

views.py에 함수 생성

```python
#variable routing
def hello(request, name):
    return render(request, 'hello.html',{'name':name})
```



urls.py에 path 추가

```python
urlpatterns = [
    path('hello/<str:name>/',views.hello),
    path('dinner/', views.dinner),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```



template 폴더에 hello.html 생성

```html
<body>
    <h1>안녕, {{ name }}!</h1>
</body>
```



#### [Throw/Catch]

views 내부에 함수 생성

```python
# Form tag    
def throw(request):
    return render(request, 'throw.html')
```



url.py 내부에 추가

```
path('throw/',views.throw),
```



templates 폴더 내부에 throw.html 파일 생성

```html
<body>
    <form action="/catch" method="get">
        #catch로 던진다
        <input type="text" name="message"/>
        #message 같은 넘겨 줄 것 변수 설정
        <input type="submit" value="Submit"/>
    </form>
</body>
```



views 내부에 함수 생성

```python
def catch(request):
    message = request.GET.get('message')
    #
    return render(request, 'catch.html',{'message':message})
```



url.py 내부에 추가

```python
path('catch/',views.catch),
```



templates 폴더 내부에 catch.html 파일 생성

```html
<body>
    <h1>Catch! {{ message }}</h1>
</body>
```





#### [FORM 외부 요청]

views.py 내부에 함수 작성

```python
#Form 외부로 요청    
def naver(request):
    return render(request, 'naver.html')
```



urls.py 추가

```python
path('naver/',views.naver),
```



template 폴더에 naver.html 생성

https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=파이썬 => 아래와 동일

https://search.naver.com/search.naver?&query=파이썬

action 내부 : https://search.naver.com/search.naver

name 내부 : query

```html
<body>
    <form action="https://search.naver.com/search.naver" method="get">
    #
        <input type="text" name="query"/>
        #네이버 검색 
        <input type="submit" value="Submit"/>
    </form>
</body>
```



#### [Bootstrap]