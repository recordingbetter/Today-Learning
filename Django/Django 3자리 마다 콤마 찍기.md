# 3자리 마다 콤마 찍기

### settings.py에 앱 추가

```
INSTALLED_APPS = [
    ...
    'django.contrib.humanize',
]
```

### html에서 로드

```
{* load humanize *}
```

### intcomma 템플릿 태그 사용

```
{* item.name|intcomma *}
```

더 많은 내용은 [여기](https://docs.djangoproject.com/en/1.11/ref/contrib/humanize/)


