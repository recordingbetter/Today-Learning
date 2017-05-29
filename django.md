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
# 프로젝트 폴더 내에 blod app을 추가한다.
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

# 관리자 계정을 만든다 (서버 시작 후에 만들어야 한다.)
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

- mysite/settings.py 파일의 TEMPLATES 항목에 

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

### 9. 템플릿 동적 데이터

- 쿼리셋을 views.py 파일에 적용한다.
- post_list.html 에서 보이게 셋팅

```python
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




