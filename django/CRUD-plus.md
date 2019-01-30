# CRUD

### Naming Convention

1.  project 이름
   - 소문자, 숫자, `_` 만 사용 가능
   - 숫자로 시작 금지
2.  App 이름
   - 소문자, 숫자, `_` 만
   - 숫자로 시작 금지
   - 명사 **복수형** 추천

1. Model  이름()
   - 대문자로 시작- `class Post`, `class Comment`
   - 단수형 명사
   - 숫자 미사용 권장
2.  URL
   - `path('posts/', include('posts.urls')),



### [template에서 hardcoding 된 URL 제거]

```python
#urls

from django.urls import path
from . import views

app_name = 'posts'✅

urlpatterns = [
    
    path('',views.index, name='list'),✅
    path('create/',views.create, name='create'),
    path('new/',views.new, name='new'),
    path('<int:post_id>/',views.detail, name='detail'),
    path('<int:post_id>/delete/',views.delete, name='delete'),
    path('<int:post_id>/edit/',views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
]
```



### []

```python
# views
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # DB INSERT
    post = Post(title=title, content=content)
    post.save()
    return redirect('posts:detail', post.pk)✅
	<!-- return redirect(f'/posts/{post.pk}/') -->

def delete(request, post_id):
    #삭제하는 코드
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:list')✅
	<!-- return redirect('/posts/') -->
    
def update(request, post_id):
    #수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect('posts:detail', post.pk)✅
	<!-- return redirect(f'/posts/{post_id}/') -->
```



```html
#index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Index</h1>
    <a href="{% url 'posts:new' %}">new</a>
    <!--아래는 수정 전 -->
    <!-- <a href="/posts/new/">new</a> -->✅
    
    <ul>
        {% for post in posts %}
        <li><a href="{% url 'posts:detail' post.pk %}">{{post.title}}</a></li>
        <!--아래는 수정 전 -->
        <!-- <li><a href="/posts/{{post.pk}}/">{{post.title}}</a></li> -->✅
        
        {% endfor %}
    </ul>
   
</body>
</html>html
```



```html
#new.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action='{% url 'posts:create' %}' method='post'>✅
        <!-- "/posts/create/" -->
        {% csrf_token %}
        <input type="text" name="title"/>
        <input type="text" name="content"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



```html
#detail.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>Post Detail</h1>
    <h2>Title : {{ post.title }}</h2>
    <p>Content : {{ post.content}}</p>
    <a href="{% url 'posts:list' %}">list</a>✅
    <!-- /posts/ -->
    <a href="{% url 'posts:edit' post.pk %}">edit</a>✅
    <!-- /posts/{{post.pk}}/edit/ -->
    <a href="{% url 'posts:delete' post.pk %}">delete</a>✅
    <!-- /posts/{{post.pk}}/delete/ -->
</body>
</html>
```



```html
#edit.html

<form action="{% url 'posts:update' post.pk %}" method="post">
    	<!-- /post/{{post.pk}}/update/ -->
        {% csrf_token %}
        <input type="text" name="title" value="{{ post.title }}"/>
        <input type="text" name="content"value="{{ post.content }}"/>
        <input type="submit" value="Submit"/>
</form>
```

