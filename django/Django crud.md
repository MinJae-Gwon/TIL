# Django crud!



## 1. 가상환경 설정 및 프로젝트 생성



1. ### [가상환경 생성]

```bash
pyenv virtualenv 3.6.7 crud-venv
#crud란 가상환경을 만들겠다	
#bahs에서 
```

2. 가상환경 적용

```bash
pyenv local crud-venv	
```



3. django 설치(가상환경 내에 django 설치가 안되어 있으므로)

```bash
pip install django
```



4. ### [프로젝트 생성]

```bash
django-admin startproject crud .
# .은 현재 dicrectory에서 생성한다는 뜻
```

(프로젝트 이름 오타 시 => 오타 발생 폴더 삭제 => manage.py 삭제(.python-version은 삭제하면 안됨!) => 프로젝트 재생성)



5. settings.py 파일에 host 등록

```python
ALLOWED_HOSTS = ['playground-wabak.c9users.io']
```



6. 서버실행

```bash
python manage.py runserver $IP:$PORT
```



7. 앱 생성

```bash
python manage.py startapp posts
#posts= 앱 이름, 수정 가능
```



8. settings.py에 앱 등록

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #추가
    'posts.apps.PostsConfig',
    ]
	#대문자 주의!
    #Posts = 앱 이름, 첫머리 대문자 필수
    #Config = 첫머리 대문자 필수
```



자! 서버를 실행하면 'migration' 에러가 발생합니다! 해결해 봅시다



### [models.py 폴더] : 데이터베이스 관리 역할



1. models.py 내부에서 데이터베이스 테이블 생성

```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    #charField 길이 제한 필수
    content = models.TextField()
    #TextField 길이 제한 불필요
```



2. 파이썬 코드를 sql문으로 옮길 수 있게 하는 작업

```bash
python manage.py makemigrations
```



3. sql을 실제 작성 가능하게 하는 작업

```bash
python manage.py migrate
```



4. 서버 실행

```bash
python manage.py runserver $IP:$PORT
```

DJANGO!



## 2. 

django 전용 shell

```bash
 #입력
 python manage.py shell
```

```bash
#결과
Python 3.6.7 (default, Jan 21 2019, 06:57:30) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

```bash
from students.models import Students
```

```bash
student = Student(name='MinJae', email='min@gmail.com', birthday=19930303, age=27)
```



3. admin





## 3. THROW & CATCH

new.html (throw)

create.html (catch)

-django! 참고-



1. 프로젝트 폴더 (posts) 내부에 urls.py 파일 생성



2. \__pycache__  폴더 내부에 있는 urls.py 파일에서 아래 내용 복사 후 

   프로젝트 폴더 (posts) 내부 urls.py에 붙여넣기

```python
from django.urls import path
from . import views
# 수정 필요! => . : 현재 위치에서
urlpatterns = [
    path('create/',views.create),
    path('new/',views.new),
   
]
```



3. \__pycache__  폴더 내부에 있는 urls.py 파일 수정

```python
from django.contrib import admin
from django.urls import path, include
from posts import views
urlpatterns = [
    path('posts/', include('posts.urls')),
    #프로젝트명 url 호출 하겠다
    path('admin/', admin.site.urls),
]

```



4. 서버 호출 후 , 인터넷 주소창에 /posts/create