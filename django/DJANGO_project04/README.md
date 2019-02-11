# 04_Project



1. 데이터베이스

ORM을 통해서 작성될 클래스의 이름은 Movie 이며, 다음과 같은 정보를 저장합니다.

```python
#models.py
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    title_en = models.TextField()
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.TextField()
    watch_grade = models.TextField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```



2. 페이지

#### (1) [영화 목록]

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
    <h1>INDEX</h1>
    <a href="/movies/new/"><p>NEW</p></a>
    <ol>
        {% for movie in movies %}
           <a href="/movies/{{movie.pk}}/"></a> <li>TITLE: {{ movie.title }} / SCORE: {{ movie.score }}</li>
        {% endfor %}
    </ol>
    
</body>
</html>
```



```python
#views.py
def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})
```



#### (2) [영화 정보 생성 Form]

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
    <h1>NEW</h1>
    <form action="/movies/create/" method="post">
        {%csrf_token%}
        title: <input type="text" name="title"/>
        title_en: <input type="text" name="title_en"/>
        audience: <input type="number" name="audience"/>
        open_date: <input type="date" name="open_date"/>
        genre: <input type="text" name="genre"/>
        watch_grade: <input type="text" name="watch_grade"/>
        score: <input type="number" name="score"/>
        poster_url: <input type="text" name="poster_url"/>
        description: <textarea name="description"></textarea>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```

```python
#view.py
def new(request):
    return  render(request,'new.html')
```



#### (3) [영화 정보 생성]

```html
#create.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>CREATE</h1>
    <p>영화정보 생성이 완료되었습니다.</p>
    <a href="/movies/">LIST</a>
</body>
</html>
```



```python
#views.py
def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre,
                watch_grade=watch_grade, score=score, poster_url=poster_url, description=description,    
    )
    movie.save()
    return render(request,'create.html')
```



#### (4) [영화 정보 조회]

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
    <h1>DETAIL</h1>
    title: {{movie.title}}
    title_en: {{movie.title_en}}
    audience: {{movie.audience}}
    open_date: {{movie.open_date}}
    genre: {{movie.genre}}
    watch_grade: {{movie.watch_grade}}
    score: {{movie.score}}
    poster_url: {{movie.poster_url}}
    description: {{movie.description}}
    
    <a href="/movies/">LIST</a>
    <a href="/movies/{{movie.pk}}/edit/">UPDATE</a>
    <a href="/movies/{{movie.pk}}/delete/">DELETE</a>
</body>
</html>
```



```python
#view.py
def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})
```



#### (5) [영화 정보 수정 Form]

```html
#edit.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>EDIT</h1>
    <form action="/movies/{{movie.pk}}/update/" method="post">
        {% csrf_token %}
        title: <input type="text" name="title" value={{movie.title}}>
        title_en: <input type="text" name="title_en" value={{movie.title_en}}>
        audience: <input type="number" name="audience" value={{movie.audience}}>
        open_date: <input type="date" name="open_date" value={{movie.open_date}}>
        genre: <input type="text" name="genre" value={{movie.genre}}>
        watch_grade: <input type="text" name="watch_grade" value={{movie.watch_grade}}>
        score: <input type="number" step="0.01" name="score" value={{movie.score}}>
        poster_url: <input type="text" name="poster_url" value={{movie.poster_url}}>
        description: <textarea name="description" value={{movie.description}}></textarea>
        <input type="submit" value="Submit"/>
    </form>
</body>
</html>
```



```python
#views.py
def edit(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'edit.html', {'movie':movie})
```



#### (6) [영화 정보 수정]

```python
#views.py
def update(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.title = request.POST.get('title')
    movie.title_en = request.POST.get('title_en')
    movie.audience = request.POST.get('audience')
    movie.open_date = request.POST.get('open_date')
    movie.genre = request.POST.get('genre')
    movie.watch_grade = request.POST.get('watch_grade')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    
    return redirect(f'/movies/{movie.pk}/')
```



#### (7) [영화 정보 삭제]

```python
#views.py
def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect(f'/movies/')
```



## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/delete/', views.delete),
    path('<int:movie_id>/update/', views.update),
    path('<int:movie_id>/edit/',views.edit),
    path('create/', views.create),
    path('new/', views.new),
    path('<int:movie_id>/', views.detail),
    path('', views.index),
]
```

