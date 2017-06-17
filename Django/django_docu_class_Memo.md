
### requirements.txt 만들기

- 프로젝트 가상환경에 설치된 pip 리스트를 문서로 만든다.

```
$ pip freeze > requirements.txt
```

### reformatting!

### vim에서 ctrl+z로 강제 종료 되었을 때, `$ fg` + Enter 하면 restore 됨.
  
### url을 app 별로 관리
 
```python
# mysite/urls.py

from django.conf.urls import url, include
from django.contrib import admin

# polls.urls를 모듈로 불러와서 사용 가능하다. (동적)
from polls import urls as polls_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # polls.urls를 모듈로 사용.
    # url(r'^polls/', include('polls.urls')),
    
    # polls.urls를 모듈로 불러와서 사용 가능하다. (동적)
    url(r'^polls/', include(polls_urls)),
]
```

### git에 tag 달기

```
# tag 만들기
$ git tag -a part1 -m "DjangoTutorial Part1"

# tag push
$ git push origin part1
```

### html label tag

- label 테그 사이에 있는 텍스트를 클릭했을때 for의 값을 id로 가진 input tag를 선택하거나 해제한다.

```html

<input type="radio" name="choice" id="choice{{ forloop.counter }} value="{{ choice.id }}>

<label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>

```


### shell 사용시 extensions 설치

```
# 1. 가상환경에 django_extensions, ipython 설치
$ pip install django_extensions
$ pip install ipython

$ pip install django-shell-plus	# 내용 확인 필요

$ pip install werkzeug		# runserver_plus

# 2. settingds.py에 'django_extensions'를 INSTALLED_APPS에 추가

# 3. 터미널에서 shell_plus 실행
$ ./manage.py shell_plus
```

### models.py 파일을 모듈 디렉토리로 관리 가능 (패키지화)

- app 디렉토리 안에 models라는 모듈 패키지 디렉토리를 만들고, 클래스 별로 파이썬 파일을 만들고
- 모듈 패키지 디렉토리의 `__inint__` 파일에 클래스들을 import.

### ipython shell auto reload

```
$ %load_ext autoreload
$ %reload_ext autoreload
```

### 데이터 검사 방법

```
# 1. 내장함수 이용
>>> hasattr(p2, 'restaurant')

# 2. try
>>> from django.core.exceptions import ObjectDoesNotExist
>>> try:
>>>     p2.restaurant
>>> except ObjectDoesNotExist:
>>>     print("There is no restaurant here.")
There is no restaurant here.
```

### 사용가능한 속성 확인

```
shell 에서...
>>> dir(클래스오브젝트)
```

### 기존 자동 생성된 중간 테이블을 가공하여 사용하기

 - 똑같은 구조의 테이블 생성
 - 필드 이름을 다르게 하고 싶은 경우, db_colunm = '만드는 이름' 옵션을 주면 된다.
 - Meta 클래스에 db_table = '[기존 생성된 테이블의 이름]'
 - ManyToMany 필드가 있는 모델 클래스에 ManyToMany 필드에 through = '[새로 생성한 테이블의 이름' 옵션을 준다.
 - magrate 이미 같은 이름의 테이블이 있다고 충돌이 난다.
 - --fake 옵션으로 migrate (장고에서는 문제가 해결된걸로 인식)
 - migrate 이후에 Meta 속성을 지우고 다시 migrate하면 같은 구조로 생성된 클래스 이름으로 테이블 이름이 변경된다.

```python
class 새로운 모델:
like_post = models.ForeignKey(Post, db_column = 'post_id')

	class Meta:
		db_table = '[기존 생성된 테이블의 이름]'

# 새로운 모델이 이미 생성된 중간테이블을 가리키게 한다.
$ pym makemigrations
$ pym migrate --fake

# 완료되면 Meta 클래스를 주석처리 한 뒤 새롭게 생성할 클래스 이름으로 변경
$ pym makemigrations
$ pym migrate

```
 
### 모델 마이그레이션 롤백
 
```
# 생성된 마이그레이션 리스트 확인
$ pym showmigrations
 
# 원하는 마이그레이션으로 되돌림
$ pym migrate [app 이름] [돌리고싶은 마이스레이션 이름]
 
# 이후 버전의 마이그레이션은 사용하지 않을거면 파일 삭제
```
 
### 중간테이블에 오브젝트 생성

```python
# Post 클래스와 User 클래스를 FK로 가지는 중간 테이블 PostLike에 데이터 생성
# p2는 Post의 객체, u2는 User의 객체  
$ PostLike.objects.create(post = p2, user = u2)

# u1의 Post 객체 호출 (like_posts는 ManyToMany 필드의 related_name)
$ u1.like_posts
```


# 인스타그램

### 구조

```
기능들
	회원관리 모듈 (member/)
		로그인
		회원관리
		팔로우
		친구찾기
		친구추천
		마이페이지
			내가 올린글
			내 정보 관리
	
	글 관련 모듈 (post/)
		뉴스피드
		사진업로드
		댓글달기
		좋아요누르기
		태그달기
		
	알림 관련 모듈 (noti/)
		팔로워의 글 등록 알림
		댓글 알림
```	

## Common Web application 


### 기본 유저 인증 시스템

[https://docs.djangoproject.com/en/1.11/topics/auth/](https://docs.djangoproject.com/en/1.11/topics/auth/)  

#### 기본 유저 모델을 사용

```python
from django.contrib.auth.models import User
```

### 기본 User 모델 Customizing

[https://docs.djangoproject.com/en/1.11/topics/auth/customizing/](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/)

#### 1. 가장 쉬운 방법

1) 새로운 모델 member를 만들고 settings.py에 아래 내용 추가

```python
AUTH_USER_MODEL = 'member.User'
```

2) post app model에서 사용되었던 User를 `settings.AUTH_USER_MODEL`로 변경 -> 이후 User 모델이 변경되어도 적용하기 편하다.(커스터마이징과 별개)

```python
# post.models.py에 settings.AUTH_USER_MODEL를 사용하기 위해 setting import
from django.conf import settings
```

3) 새로운 앱 member의 User 모델은 AbstractUser 상속받음

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

4) 이전의 모든 migration 파일을 삭제하고 migrate
5) models.py 파일에서 

```python
from django.conf import settings
# User를 모두 settings.AUTH_USER_MODEL로 변경
```
6) post.views.py 파일에서

```python
from django.contrib.auth import get_user_model

User = get_user_model()
```
[https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.get_user_model](https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.get_user_model)


### 사용 방법
[https://docs.djangoproject.com/en/1.11/topics/auth/#Installation](https://docs.djangoproject.com/en/1.11/topics/auth/#Installation)

1. INSTALLED_APPS에 'django.contrib.auth', 'django.contrib.contenttypes' 추가
2. MIDDLEWARE에 SessionMiddleware, AuthenticationMiddleware

```python
from django.contrib.auth.models import User


# shell에서 유저 생성
$ u = User.objects.create_user('Joe')

# 만들어진 유저에 비번 변겅
$ u.set_password('adminadmin')

# 포스트 생성
$ p1 = Post.objects.create(author = u)

# 추가 유저 생성
$ u2 = User.objects.create_user('Kay')

# 포스트에 댓글 달기
$ p1.comment_set.create(post = p1, author = u2, content = 'making reply')

$ Comment.objects.create(post = p1, author = u2, content = 'making another replay')

# 댓글 확인
$ p1.comment_set.all()

```

## ImageField

- Pillow 라이브러리 설치
[https://pillow.readthedocs.io/en/4.1.x/](https://pillow.readthedocs.io/en/4.1.x/)

```
# Xcode command line 설치

# 외부 라이브러리 설치
$ brew install libtiff libjpeg webp little-cms2

# pillow 설치
$ pip install Pillow
```

### image 파일을 저장하기 위한 media 폴더 지정하기

- 루트폴더 하위에 media 폴더 생성

```python
# config.settings.py에 media 폴더 위치를 지정해준다.
MEDIA_URL = '/media/'
# django_app/media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# config.urls.py 파일에 아래 내용 추가
# static 함수는 리스트를 반환하므로 기존 urlpatterns 에 더해준다.
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# 위 내용과 같다.
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

# post.models.py 에서 모델클래스 설정시 이미지 파일 저장 위치 지정
class Post(models.Model):
    photo = models.ImageField(blank=True, upload_to='post', )
# 파일은 media/post 에 저장된다.
```




#### Pycharm에서 클래스, 함수 등 사용된 부분 찾기

**shift+command+F**


#### get\_or\_create

[https://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet.get_or_create](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#django.db.models.query.QuerySet.get_or_create)

- 조건에 주어진 객체가 발경되면, 해당객체의 값을 튜플과 False 반환.
- 조건에 주어진 객체가 발견되지 않으면 새 객체를 생성(defaults 값 반영)하고 저장한다. 새 객체의 값의 튜플과 True를 반환

```python
# 있으면 True, 없으면 False + 객체 생성
tag, tag_created = Tag.objects.get_or_create(name = tag_name)

# 문서 예제
obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    #get 할때에는 defaults 부분은 전달되지 않음
    defaults={'birthday': date(1940, 10, 9)},
)
```

#### debuger

- Edit Configuratios 에서 셋팅
- sctipt : manage.py
- script parameters : runserver / shell_plus
- 디버거 선택, 멈출 지점 선택 후 디버깅

### FileField

- Storage.save() 매소드로 저장됨




### QuerySet

- ManyToMany 관계에서 중간자 모델에 데이터 만들기

```python
# Post, User가 ManyToMany 관계일때
p = Post.objects.get(pk=1)
u = User.objects.get(pk=2)

# PostLike가 중간자 모델
p.postlike_set.create(user = u)
```

### Model Field & Form Field

[https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#field-types](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#field-types)

### bound & unbound form

- bound : 데이터가 채워져 있는 폼 생성
- unbound : 빈칸으로 폼 생성

### CONTEXT_PROCESSORS

- TEMPLATE_CONTEXT_PROCESSORS :모든 template에서 사용할 수 있는 변수
- 이미 있는 것을 쓸 수도 있고, 만들 수도 있다.

1) context_processors.py 파일을 만들고

```python
from .forms import LoginForm


def forms(request):
    context = {
        'login_form': LoginForm(),
        }
    return context
```

2) settings.py의 TEMPLATES에 추가

```python
# settings.py 일부
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
                # context_processors 추가
                'member.context_processors.forms',
            ],
        },
    },
]
```