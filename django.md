## 장고란?

- 파이썬에서 같은 작업을 반복하지 않고 데이터베이스를 쉽게 사용하게 해주는 프레임워크

### 프레임 워크 (frame work)

- 프로젝트마다 반복되는 작업을 쉽게 할 수 있게 만든 프로그램


## 장고 시작하기

### SSH key 생성하여 적용

[https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/]()

1. 터미널에서 홈폴더에 .ssh 폴더를 생성한다.
2. `$ ssh-keygen -t rsa -b 4096 -C "깃헙 계정"`
3. 만들어진 파일 id_rsa.pub의 내용을 복사
	`$ cat id_rsa.pub`
4. github.com/profile/SSH and GPG keys 항목에 SSH key를 추가하여 붙여넣는다.
5. github의 저장소를 생성하여 나오는 SSH 주소 "git@github.com:~~"로 git을 생성한다.

## Blog 만들기 (djangogirls Tutorial)

### 1. 프로젝트 시작

```shell
# 장고 프로젝트를 새로 만든다.
$ ~/djangogirls$ django-admin startproject mysite

# 상위 폴더 이름을 변경
$ mv mysite django_app

# 명령어 확인
$ ./manage.py

# 로컬에서 서버를 시작 (컨트롤+C)로 종료
$ ./manage.py runserver
```

### 2. app 추가

```shell
# 프로젝트 폴더 내에 blog app을 추가한다.
$ ./manage.py startapp blog
```

```python
# mysite/settings.py 파일의 INSTALLED_APPS 항목에 blog를 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

### 3. 모델 만들기

```python
# blog/models.py에 블로그 글의 모델을 만든다.

from django.db import models
from django.utils import timezone

# models의 Models를 상속받음
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

```

### 4. 데이터베이스 설정

```shell
# 만들어진 모델을 데이터베이스에 적용한다.
$ ./manage.py migrate

# 데이터베이스를 만들기 위해 변경된 사항을 체크하여 보관한다.
$ ./manage.py makemigrations (app name:생략하면 전체)

# 체크했던 변경 사항들을 데이터베이스에 적용한다.
$ ./manage.py migrate (app name:생략하면 전체)
```

- 클래스 1개가 1테이블
- 데이터베이스 내용 확인은 SQLite Browser

### 5. 관리자

```python
# blog/admin.py 에 아래 내용을 추가
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

```
# 터미널에서 서버 시작
$ ./manage.py runserver

# 관리자 계정을 만든다
$ ./manage.py createsuperuser

```

- 웹브라우저에서 127.0.0.1:8000/admin으로 접속 후 관리자 계정으로 로그인
- External Libraries/site-packages/django/contrib 에 있는 내용이 자동으로 생성됨

### 6. url

- root url 정규표현식 : `r'^$'`

```python
# mysite/urls.py

from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),	# 기본주소/admin/ 으로 접속 시 admin.site.urls 실행
    url(r'^$', views.post_list), # 기본주소로 접속 시, views.post_list 실행
]
```

### 7. templates

- 프로젝트 폴더 하위에 templates/blog 폴더 생성
- mysite/settings.py 파일의 TEMPLATES 항목에 아래 내용 추가 (지정한 경로의 폴더에서 template을 찾는다)

```python
# mysite/settings.py
# 괄호는 상위폴더를 뜻한다. 그래서 djang _app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# templates 폴더 경로 변수 생성
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```

```python
# 같은 파일 아래 부분에 TEMPLATES의 DIRS의 리스트에 위 경로를 입력해준다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


### 8. ORM / Query Sets

- ORM : 장고에서 데이터베이스를 객체로 불러오기 위한 쿼리

```sql
# django shell
$ ./manage.py shell

# blog.models에서 Post를 불러온다
>>> from blog.models import Post
# 출력하여 확인
>>> Post.objects.all()

# 실제 쿼리 확인
>>> pl = Post.objects.all()
>>> print(pl.query)
SELECT "blog_post"."id", "blog_post"."author_id", "blog_post"."title", "blog_post"."text", "blog_post"."created_date", "blog_post"."published_date" FROM "blog_post"
```

```sql
# User 테이블에서 user데이터를 불러온다.
>>> from django.contrib.auth.models import User
# user를 설정해준다.
>>> user = User.objects.get(id=1)

# 새 포스트 작성
>>> Post.objects.create(title='test title', text='test text', author=user)

# filter
>>> Post.objects.filter(title__contains='title')
<QuerySet [<Post: first title>, <Post: test title>]>
# 실제 쿼리 확인
>>> pl = Post.objects.filter(title__contains='title')
>>> print(pl.query)
SELECT "blog_post"."id", "blog_post"."author_id", "blog_post"."title", "blog_post"."text", "blog_post"."created_date", "blog_post"."published_date" FROM "blog_post" WHERE "blog_post"."title" LIKE %title% ESCAPE '\'

# timezone 불러오기
>>> from django.utils import timezone
# 범위 설정
>>> Post.objects.filter(published_date__lte=timezone.now())
[<Post: Sample title>]
```

```sql
# 특정 포스트를 불러옴
>>> post = Post.objects.get(title='test title')
# 퍼블리시
>>> post.publish()
```

#### get

- `model.objects.get(조건)`
- 조건에 맞는 1개의 결과만 반환한다.
- `value_name.column_name`으로 사용
- 조건에 맞는 값이 1개 이상일 경우 에러 발생

```python
key = model1.objects.get(pk=1)
print(key.name)
```
  
#### all

- `model.objects.all()`
- 모든 값을 반환

```python
key = model1.objects.all()
print(key[0]['name'])
```

#### filter

- `model.objects.filter(조건)`
- 조건에 맞는 모든 값을 반환

```python
key = model2.objects.filter(name='lee')
print(key[0]['name'])
```

#### 조건 키워드

|키워드|설명|사용예|
|---|---|---|
|\_\_lt / \_\_gt</br>\_\_lte / \_\_gte|~보다 작다 / ~보다 크다</br>~보다 작거나 같다. ~보다 크거나 같다.|id가 1보다 큰 데이터 검색</br>model1.objects.filter(id\_\_gt=1)|
|\_\_in|주어진 리스트 안에 존재하는 데이터 검색|model1.objects.filter(id\_\_in[2, 3, 5]|
|\_\_year</br>\_\_month</br>\_\_day|해당 년도, 월, 일 검색|model1.objects.filter(published_date\_\_year=2015)|
|\_\_isnull|해당 열의 값이 null인 데이터 검색|model1.objects.filter(name__isnull=True)|
|\_\_contains</br>\_\_icontains|해당 열의 값이 지정한 문자열을 포함하는 데이터 검색</br>\_\_icontains는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_contains='com')|
|\_\_startswith</br>\_\_istartswith|해당 열의 값이 지정한 문자열로 시작하는 데이터 검색</br>\_\_istartswith는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_startswith='com')|
|\_\_endswith</br>\_\_iendswith|해당 열의 값이 지정한 문자열로 끝나는 데이터 검색</br>\_\_iendswith는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_endswith='com')|
|\_\_range|문자, 숫자, 날짜의 범위를 지정|model1.objects.filter(id\_\_range(2, 10)|
  
#### order by

- `model.objects.order_by('값')`
- 기본은 오름차순 정렬
- 내림차순일 경우, 컬럼명 앞에 `-`를 붙여준다.

```python
value = model.objects.order_by('pk')		#오름차순
value = model.objects.order_by('-pk')		#내림차순
```

#### values

- `model.objects.values('값')`
- 특정 컬럼의 값만 반환

```python
value = model.objects.values('pk')		# query set 형태로 pk값만 반환
```
  

### 9. 템플릿 동적 데이터

- blog/views.py 파일에 아래 내용을 추가하여 urls.py 파일에서 호출할때 실행할 함수를 만든다.
- 쿼리셋을 views.py 파일에 적용한다.
- post_list.html 에서 보이게 셋팅

```python
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # posts 변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)을 대입
    # posts = Post.objects.all()

    # posts 변수에 ORM을 사용해서 전달할 쿼리셋이 Post의 published_date가 timezone.now()보다 작안값을 가질때만 해당하도록 필터를 사용한다.
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title': 'PostList from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context = context)
```

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Django Girls Tutorial by Joe</title>
</head>
<body>
    <div>
        <h1><a href="#">Django Girls Blog by Joe</a></h1>
        <h3>{{ title }}</h3>
    </div>

# posts를 순회하기 위해 for문을 사용
{% for post in posts %}
    <div>

        <h2><a href="#">{{ post.title }}</a></h2>
        <p>{{ post.author }}</p>
        <p>{{ post.text }}</p>
        <p>published: {{ post.published_date }}</p>
    </div>
{% endfor %}
</body>
</html>
```

### 10. bootstrap 적용

(1) bootstrap을 다운받아 django_app/static 폴더에 넣어준다.
(2) mysite/settings.py에 static 폴더 경로 추가

```python


# django_app/static 폴더의 경로를 STATIC_DIR에 할당
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# 이 경로로 시작하는 URL은 정적파일들의 위치에서 파일을 찾아 리턴
STATIC_URL = '/static/'

# 이 리스트(또는 튜플)의 경로는 STATIC_URL로 요청된 파일을 찾는 폴더로 사용됨
STATICFILES_DIRS = (
    STATIC_DIR,
)
```
(3) post_list.html에 아래 내용을 추가해 준다. (bootstrap 경로)

```html
<head>
    <!--적용되면 경로는 static/bootstrap/css/bootstrap.css 이렇게 바뀜. 탬플릿태그-->
    
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.css' %}">
    
</head>
```

(4) bootstrap을 적용해줄 부분에 적용해준다.

### 11. 템플릿 확장하기 (post_detail 만들기)

(1) views.py에 view 추가

```python

def post_detail(request):
    context = {
    	# id값(장고에서는 pk로 사용가능)이 아래 urls.py에서 보내준 pk값과 일치하는 post를 보내준다.
        'post': Post.objects.get(id=pk)
    }
    return render(request, 'blog/post_detail.html', context)
```

(2) urls.py에 경로 추가

```python

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url에 이름을 정해주면 다른 곳에서 참조가 가능하다.
    url(r'^$', views.post_list, name='post_list'),
    # post/로 시작하고 숫자 1개 이상을 가진 뒤 /로 끝나는 url
    # post 이후에 오는 숫자를 pk로 이름지어줌. -> views.py에서 인자로 사용 가능
    # views.post_detail(request, pk) 형태로 전달됨
    url(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
```

(3) html에서 경로를 정해준다.

```html
<div class="post-list">
    {% for post in posts %}
    <div class="post">
    # 경로를 urls.py에서 리버스로 가지고 온다.
        <h3><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h3>
        <p class="text-right"><small>published: {{ post.published_date }}</small></p>
        <p>{{ post.text|truncatechars:120 }}</p>

    </div>
{% endfor %}
</div>
```


### 12. 글쓰기 기능 만들기 post_create.html

(1) urls.py에 post 작성을 위한 url을 만들어 준다.

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
    # views.post_detail(request, pk) 형태로 전달됨
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/create/$', views.post_create, name='post_create'),
]
```

(2) views.py에 "POST" 매소드로 요청이 올때 실행할 post_create를 만들어준다.

```python
def post_create(request):
	# 요청의 method가 'GET'일 경우
    if request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_create.html', context)
        
    # 요청의 method가 'POST'일 경우 
    elif request.method == 'POST':
    	# request.POST 값은 딕셔너리로 나온다.
        data = request.POST
        title = data['title']
        text = data['text']
        user = User.objects.first()
       # 데이터베이스에 위 값으로 데이터를 쓴다.
        post = Post.objects.create(
            text=text,
            title=title,
            author=user,
            )
       # 요청 처리가 완료되면 post_detail url+pk를 리버스로 가지고 와서 redirect
       # url dispatcher
        return redirect('post_detail', pk=post.pk)
```

(3) post_create.html에 보여줄 화면을 만든다.

```html
{% extends 'blog/base.html' %}
{% block content %}
<form action="" method="POST">
    {# 응답이 적잘한 사용자에게서 왔는지 확인한다. 해킹방지 #}
    {% csrf_token %}
    <input name="title" type="text">
    <textarea name="text" id="" row="10" cols="100"></textarea>
    
    {# submit 타입의 버튼은 form의 내용을 POST라는 매서드로 서버로 보낸다. #}
    <button type="submit">Add post</button>
</form>
{% endblock %}
```

(4) 장고 폼을 적용하기 위해 blog/forms.py 파일 생성
- blog app에 사용될 form들을 관리하는 파일

```python
# blog/forms.py
# django의 forms를 import
from django import forms

# post_create에서 사용할 form을 정의하는 클래스 생성 
class PostCreateForm(forms.Form):
    title = forms.CharField(
        label='제목',
        max_length = 10,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    text = forms.CharField(
        label='내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'form-control',
            }
        ),
        required = True
    )
```








