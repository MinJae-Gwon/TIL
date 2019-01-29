# Django crud!



## 1. 가상환경 설정 및 프로젝트 생성

django 폴더에 폴더(프로젝트 상위 ex)workshop, intro, crud..) 생성



1. ### [가상환경 생성]

```bash
pyenv virtualenv 3.6.7 crud-venv
#crud란 가상환경을 만들겠다	
#bahs에서 
```

2. 가상환경 적용(미리 만들어 놓은 폴더 안으로 위치를 이동 시킨 후 !!)

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



Django: 모델 이라는 파이썬 객체를 통해 데이터 접속 & 관리

모델: 저장된 데이터의 구조(Schema)를 정의 ex) 필드 타입, 데이터의 최대 크기, 기본값 등

모델은 장고 웹 어플리케이션의 `models.py` 파일에서 정의됨. 이들은 `django.db.models.Model` 를 상속받은 서브(파생) 클래스로 구현되며, 필드, 메서드, 메타데이터등을 포함 할 수 있음.



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

**필드(Fields)**

데이터 베이스 테이블의 열을 나타내는 추상 클래스임. 모델 클래스의 각 속성은 테이블의 필드에 해당함. 각각의필드는 DB 목록(table)에 저장하길 원하는 데이터열을 나타냄.

```
title = models.CharField(max_length=100)
content = models.TextField()
```

위의 예제는 `title` 이라는 하나의 필드를 갖고 있으며, `models.CharField` 필드타입임. 즉, 이 필드가 작은 문자열을 포함하고 있다는 뜻임.



2.  **Migrations** : Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 테이블을 데이터베이스에서 생성할 수 있음. Python 모델 클래스의 수정 (및 생성)을 DB에 적용하는 과정을 Migration이라고 함.

```bash
#마이그레이션 파일(초안) 생성
python manage.py makemigrations
```



3. **Migrate** sql을 실제 작성 가능하게 하는 작업

```bash
해당 마이그레이션 파일을 실제 데이터 베이스에 반영(적용)
python manage.py migrate
```



4. 서버 실행

```bash
python manage.py runserver $IP:$PORT
```

DJANGO!



## 2. CRUD

django 전용 shell : Django 에서 동작하는 모든 명령을 대화식 Python 쉘에서 사용 할 수 있게 함

```bash
 #입력
 python manage.py shell
 #
 from [어플리케이션명].models import [클래스명] : 파이썬 쉘 내 사용을 위한 클래스 호출
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



**Create**

```bash
>>> post = Post(title='몇번째?', content='인가요?')
>>> post
Post: Post object (None)>
>>> post.save()
# save 중요!
>>> post.title
'몇번째?'
>>> post.content
'인가요?'
```

post라는 Post의 인스턴스를 생성. 이는 post 라는 변수임.

`post.title` 또는 `post.content` 로 접근하면, 파이썬 내에서만 인스턴스의 변수를 호출하는 것임. 따라서, `post.save()` 를 써야, 데이터 베이스에 저장이 됨.



**Read**

```bash
#Read all
>>> Post.objects.all()
<QuerySet [<Post: Post object (2)>, <Post: Post object (3)>]>

#Get one
>>> Post.objects.get(pk=3)
<Post: Post object (3)>
```

Django의 경우, id값이 아니라 pk(primary key)로 접근을 함.

```bash
#filter (WHERE)
>>> posts = Post.objects.filter(title='Hello').all()
>>> posts
<QuerySet [<Post: Post object (1)>]> 
#all()로 filter를 쓰면 복수 형으로 결과가 리스트의 형태로 뜸.

>>> posts = Post.objects.filter(title='Hello').first()
>>> posts
<Post: Post object (1)>
    
#like 
>>> posts = Post.objects.filter(title__contains='He').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#order by
#title이라는 필드로 오름차순
>>> posts = Post.objects.order_by('title').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#내림차순 (필드명 앞에 -붙임)
>>> posts = Post.objects.order_by('-title').all()
>>> posts
<QuerySet [<Post: Post object (1)>]>

#limit & offset
>>> Post.objects.all()[:1]
<QuerySet [<Post: Post object (1)>]>

>>> Post.objects.all()[1:2]
<QuerySet [<Post: Post object (2)>]>
```



**Delete**

django에서는 SQL과 다르게 id 값이 아닌 pk (primary key)로 고유값에 접근함.

```bash
>>> post = Post.objects.get(pk=1)
>>> post.delete()
(1, {'posts.Post': 1})
```

**Update**

파이썬 내 Post라는 클래스의 인스턴스가 수정된 것이므로 save를 반드시 해줘야 Database에도 수정이 적용된다.

```bash
>>> post = Post.objects.get(pk=2)
>>> post.title
'1번째'
>>> post.title = '2번째로변경'
>>> post.title
'2번째로변경'

>>> post.save()
>>> post = Post.objects.get(pk=2)
>>> post.title
'2번째로변경'
```



## 3. THROW & CATCH

**Model을 활용하여 웹페이지 생성하기(New / Create)**

```python
#views.py
from django.shortcuts import render
from .models import Post

def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post(title=title, content=content)
    post.save()
    
    return render(request, 'create.html')


#urls.py 매우 중요
from posts import views

urlpatterns = [
    path('create/', views.create),
    path('new/', views.new),
]
<-- new.html -->
<body>
    <form action="create/" method="get">
        <input type="text" name="title"/>
        <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>

</body>
    
<-- create.html -->
<body>
   <h1> 성공적으로 Post를 생성 했습니다! </h1>
</body>
```

`views.py` 에서 `render` 함수로 `new.html` 을 호출함. input 태그를 통해 들어오는 값은 총 2가지로, 각각 `title` 과 `content`라는 `name`의 속성으로 정의 되어 있다. 여기서 `Dict`의 구조를 띔. {title: 사용자 입력 값, content: 사용자 입력값}

`views.py` 안 `create` 함수에서 `Dict`에서 저장된 value값을 가져와 각각 `title` 과 `content` 라는 변수에 저장.

```bash
title = request.GET.get('title')
content = request.GET.get('content')
```



데이터베이스에 내용을 저장하는 작성함. 아래의 경우, Post 클래스를 사용하기 위해 `models.py`에 작성된 Post 클래스를`import`를 해와야함.

```
from .models import Post

post = Post(title=title, content=content)
post.save()
```

최종적으로, `new.html` 에서 사용자가 내용을 입력하면, `form` 태그 `action` 속성으로 연결된 `create.html` 으로 이동되어,`views.py` 에 정의된 `create` 함수가 실행된다. 해당 함수에 정의된 변수명에 따라, 데이터베이스에 내용이 저장되며, 사용자는 `create.html` 에 따라, "성공적으로 Post되었습니다" 라는 결과를 화면을 보게 된다.



**URL구조 변경**

지금까지 우리는 프로젝트 폴더 내에 존재하는 urls.py (어플리케이션 폴더의 상위디렉토리)에 모든 url을 저장해왔다. 그런데 만약, 한 프로젝트 내에 무수히 많은 어플리케이션을 생성하고, 관련 url을 urls.py에 작성한다면, traceability 적인 측면 뿐만 아니라 직관적으로 각 어플리케이션에 해당하는 url을 구분하기 힘들 것이다.

따라서, urls.py를 각 어플리케이션 내에 새로 생성하여, 손쉽게 urls.py를 관리 할 수 있도록 해보자.

1. 프로젝트 폴더 (posts) 내부에 urls.py 파일 생성



2. \__pycache__  폴더 내부에 있는 urls.py 파일에서 아래 내용 복사 후 

   프로젝트 폴더 (posts) 내부 urls.py에 붙여넣기

```python
from django.urls import path
from . import views
#현재 디렉토리 내에 views.py를 불러오므로 from 에는 현재 디렉토리를 의미하는 . 을 써줌.
urlpatterns = [
    path('create/',views.create),
    path('new/',views.new),
]
```



3. \__pycache__  폴더 내부에 있는 urls.py 파일 수정

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('posts/', include('posts.urls')),
    #프로젝트명 url 호출 하겠다
    path('admin/', admin.site.urls),
]

```

`path`의 첫 번째 인수로, `'posts/'` 값을 줌에 따라, posts(어플리케이션)에 적용되는 모든 url을 직관적으로 이해할 수있음. 또한 두번째 인수로, `include('posts.urls')` 을 주어, posts(어플리케이션) 내 urls.py와 연결을 시켰음. 이 때, 외장 함수인 include를 import 하였음.



4. 서버 호출 후 , 인터넷 주소창에 /posts/create 입력
5. new.html

```
<form action="/post/create/" method="get">
```





## ADMIN

관리자 계정 customize : `admin.py` 파일

관리자 페이지 주소 : `http://playground-wabak.c9users.io:8080/admin/`



[1] admin 파일 내부

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)    # 관리자 페이지 기본 형태
```



 [2] `기본주소/admin` 접속하여 관리자 페이지에 들어가기 위해 계정 생성을 해야함

```bash
(crudvenv) harrylee0810:~/workspace/django/crud (master) $ python manage.py createsuperuser
Username (leave blank to use 'ubuntu'): admin
Email address: admin@admin.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```



[3] 객체의 내용도 보일 수 있게 admin 페이지를 커스터마이징 할 필요가 있음. `admin.ModelAdmin` 상속을 통해 커스터마이징이 가능함.

```python
# admin.py

from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):   #admin.ModelAdmin을 상속받은 PostAdmin이라는 클래스
    list_display = ('title','content',) #관리자 페이지에서, object 목록을 1,2,3,4가 아니라, 제목과 내용으로 보여주는

admin.site.register(Post, PostAdmin) # 위 클래스명 적어준 거. 이렇게 하면 관리자페이지에서 제목과 내용 보임
```



[4] 데이터베이스에 저장된 레코드 보는 페이지 작성

```python
# views.py

from django.shortcuts import render
from .models import Post  # ✅ post 기능 쓰려고 적어 줌

def new(request):
    return render(request,'new.html')
    
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    
    return render(request,'create.html')
    
#데이터베이스에 저장된 레코드 보는 페이지✅✅
def index(request):
    # All Post
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
```



```python
# index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Index</h1>           <!-- 관리자 파일 말고, ...일반 페이지에  내가 작성한 콘텐츠 출력하기 --> 
    <ul>
     <-- 반복문을 돌리기 위해 jinja 템플릿 사용 -->
    {% for post in posts %}
        <li>{{ post.title }} - {{post.content}}</li>   ✅✅✅✅✅✅✅✅✅✅✅
    {% endfor %}
    </ul>
</body>
</html>
```



