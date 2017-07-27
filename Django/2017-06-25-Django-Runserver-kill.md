---
layout: post
title:  "Django Runserver가 종료되지 않을때"
date:   2017-06-25 22:00:06 +0900
categories: jekyll update
---

# Django Runserver가 종료되지 않을때

Django 작업 중, runserver하던 터미널을 종료하거나, Pycharm을 종료했을때 8000번 포트가 사용중이라 이후 작업이 곤란했던 적이 있다.  
이때, 실행중인 runserver를 찾아 강제 종료하는 방법이다.

```
$ ps auwx|grep runserver
Joe              61900   0.8  0.2  2446756  35460 s002  S+   11:42PM   0:00.50 /usr/local/var/pyenv/versions/3.5.3/envs/TDD/bin/python manage.py runserver
Joe              61903   0.0  0.0  2423384    228 s001  R+   11:42PM   0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn runserver
Joe              61899   0.0  0.2  2438228  30660 s002  S+   11:42PM   0:00.38 python manage.py runserver

$ kill -9 61900
```

몇 번 포트인지는 안나와서 아쉽...