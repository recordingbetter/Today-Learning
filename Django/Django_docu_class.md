
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

### ipython sell auto reload

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

