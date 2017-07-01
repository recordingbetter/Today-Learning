# Django AWS Deployment

## Django Deployment Check List

- [deployment ckecklist](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/)

## Secret key, debug 등을 git에 올라가지 않게 분리하기

- 프로젝트 루트 폴더 상위에 .config\_secret 폴더를 만든다
- settings\_common.json 파일을 만들어 아래 내용 기입

```json
{
  "django": {
    "secret_key": "settings.py에 있던 secret_key 내용"		# settings.py에서는 ''
  }
}
```

- settings\_debug.json, settings\_deploy.json 파일을 .config\_secret 폴더에 만든다.

```json
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}

```

- settings.py 파일을 base.py로 바꾸어 settings 파이썬 패키지 폴더를 만들어 이동한다.
- base.py 파일에 ROOT\_DIR, CONFIG\_SECRET\_DIR 등을 셋팅

```python
ROOT_DIR = os.path.dirname(BASE_DIR)
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
```

- base.py에서 settings\_common.py 파일을 읽어온다.

```python
config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']
```

- settings/base.py에서 ALLOWED_HOSTS, DEBUG 삭제
- settings/base.py에서 아래 내용 추가

```
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')
```

- settings/debug.py 파일을 만들고 아래 내용 작성

```
# base 파일의 내용을 모두 상속받음
from .base import *

config_secret_debug = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True

ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']
```

- settings 파일이 이동되고 이름이 변경되었으므로 runserver 옵션 필요

```
$ ./manage.py runserver --settings=config.settings.debug
```

- .gitignore에 내용 추가

```
.config_secret/

```

## AWS 설정

- [EC2 설정 페이지](https://ap-northeast-2.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-2#)

- AWS EC2 인스턴스 생성

- key pair 만들고 다운로드하여 ~/.ssh/ 폴더에 저장

- 키 파일의 권한 변경

```
# 소유자 외에는 해당 파일을 읽을 수 없게 함.
$ chmod 400 [키파일 이름]
```

- AWS ssh로 [연결](http://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

```
# ssh -i [키 파일] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP]
$ ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com

# 처음 접속하는 서버인데 계속 할건가 물어봄
The authenticity of host 'ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com (13.124.12.223)' can't be established.
ECDSA key fingerprint is SHA256:EkaIuENAjn1tVMQb2aG
Are you sure you want to continue connecting (yes/no)?

# yes 하면 접속됨 -> 터미널 화면 상단데 ubuntu@ip-... 확인
```

#### 언어팩 설치 (선택사항 - 에러메세지가 한글로 나와서 검색이 어렵다)

```
~ sudo apt-get install language-pack-ko
~ sudo locale-gen ko_KR.UTF-8
```

## AWS User/Group 만들기

- [IAM Dashboard](https://console.aws.amazon.com/iam/home?region=ap-northeast-2#/home)

### Programmatic access User

- Users -> Add User -> User name 입력 -> Access type : Programmatic access 
- 기존 그룹을 복사하여 넣거나 새로운 그룹 생성 (권한 그룹)
- Access key ID와 Secret access key를 보관하거나 cvs 파일로 다운로드 (단 한번만 보인다)
- 해당 user의 account no, Access key ID, Secret access key를 사용하여 server에 접속 가능
- AWS Management Console에 로그인할 수 없다.

### AWS Management Console access User

- Users -> Add User -> User name 입력 -> Access type : AWS Management Console access 
- 기존 그룹을 복사하여 넣거나 새로운 그룹 생성 (권한 그룹)
- account no와 Password를 복사하여 보관하거나 cvs 파일로 다운로드 (단 한번만 보인다)
- 해당 user의 account no, Username, Password를 사용하여 Management Console에 로그인 가능


## Ubuntu 기본 설정

#### python-pip설치

```
~ sudo apt-get install python-pip
```

#### zsh 설치

```
~ sudo apt-get install zsh
```


#### oh-my-zsh 설치

```
~ sudo curl -L http://install.ohmyz.sh | sh
```


#### Default shell 변경

```
~ sudo chsh ubuntu -s /usr/bin/zsh
```

#### pyenv requirements설치

[공식문서](https://github.com/yyuu/pyenv/wiki/Common-build-problems)

```
~ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

#### pyenv 설치

```
~ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

#### pyenv 설정 .zshrc에 기록

```
~ vi ~/.zshrc

# 아래 내용 추가
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Python 3.6.1 install

```
~ pyenv install 3.6.1
```

### AWS Command Line Interface 설치

```
~ pip install awscli

# 버전 확인
~ aws --version
```

### AWS Configure

```
~ aws configure
AWS Access Key ID [None]: 만든 유저 키
AWS Secret Access Key [None]: 만든 유저 키
Default region name [None]: ap-northeast-2
Default output format [None]: json
```

#### Pillow 라이브러리 설치

[공식문서](https://pillow.readthedocs.io/en/3.4.x/installation.html#basic-installation)

```
~ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

### vim에서 테마 변경

:colorscheme [tab]

## local project upload

- AWS 접속

```
# ssh -i [키 파일] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP]
$ ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com

$ ssh -i ~/.ssh/aws_joe.pem ubuntu@13.124.12.223
```

- 로컬 프로젝트를 AWS에 복사

```
# scp -i [키 파일] -r [local project] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP]:[destination]
$ scp -i ~/.ssh/aws_joe.pem -r /Users/Joe/projects/django/deploy_ec2 ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com:/srv/deploy_ec2

$ scp -i ~/.ssh/aws_joe.pem -r /Users/Joe/projects/django/deploy_ec2 ubuntu@13.124.12.223:/srv/deploy_ec2
```

- AWS의 파일/폴더 삭제

```
# ssh -i [키 파일] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP] rm -rf [target]
$ ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com rm -rf /srv/deploy_ec2

$ ssh -i ~/.ssh/aws_joe.pem ubuntu@13.124.12.223 rm -rf /srv/deploy_ec2
```

### 위 내용을 .zshrc에 alias로 만들 수 있음

```
$ vim ~/.zshrc

# .zshrc에 아래 내용 추가
# AWS 접속
alias con-ec2="ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com"

# AWS의 프로젝트 폴더 삭제
alias delete-ec2="ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com rm -rf /srv/deploy_ec2"

# AWS에 local 프로젝트를 복사
alias scp-ec2-ori="scp -i ~/.ssh/aws_joe.pem -r /Users/Joe/projects/django/deploy_ec2 ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com:/srv/deploy_ec2"

# AWS의 프로젝트 폴더 삭제 후 local 프로젝트 복사를 한번에
alias scp-ec2="delete-ec2 && scp-ec2-ori"
```

```
# 해당 쉘의 환경변수 확인
$ env
$ echo $DJANGO_SETTINGS_MODULE

# DJANGO_SETTINGS_MODULE 환경변수 추가
$ export DJANGO_SETTINGS_MODULE=config.settings.debug

# migrate
$ /managy.py migrate --settings=config.settings.debug

# 이후부터는 아래 명령으로 실행 가능 
$ /managy.py renserver
```

```
# 터미널에서 새 탭을 열지 않고 변경 사항 적용
$ source ~/.zshrc
```

## Nginx

```
# AWS에서 nginx user 설정
~ sudo adduser nginx
```

### uWSGI 설치 (가상환경 안에서)

```
# AWS에서
~ pip install uwsgi
```

### 프로젝트에서 wsgi 파일 분리

```python
# wsgi/debug.py
import os
from django.core.wsgi import get_wsgi_application

# 환경변수 설정 (os.environ) config.settings.debug 값 적용
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")
application = get_wsgi_application()


# wsgi/deploy.py
import os
from django.core.wsgi import get_wsgi_application

# 환경변수 설정 (os.environ) config.settings.deploy 값 적용
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deploy")
application = get_wsgi_application()
```

### uwsgi 실행

```
# uwsgi --http :8000 --home (virtualenv경로) --chdir (django프로젝트 경로-소스루트) -w (wsgi 설정파일)

# local에서  확인
$ uwsgi --http :8000 --home /usr/local/var/pyenv/versions/deploy_ec2 --chdir /Users/Joe/projects/django/deploy_ec2/django_app -w config.wsgi.debug

# AWS에서
$ uwsgi --http :8000 --home ~/.pyenv/versions/deploy_ec2 --chdir /srv/deploy_ec2/django_app -w config.wsgi.deploy
```

### uwsgi를 실행할 설정파일을 만든다.

- local에서 테스트 중...

```
# .config_secret/uwsgi/debug.ini에 아래 내용 작성

[uwsgi]
home = /usr/local/var/pyenv/versions/deploy_ec2
chdir = /Users/Joe/projects/django/deploy_ec2/django_app
module = config.wsgi.debug
http = :8000

# 실행하려면
$ uwsgi --ini .config_secret/uwsgi/debug.ini
```

- AWS에서...

```
# .config_secret/uwsgi/deploy.ini에 아래 내용 작성

[uwsgi]
home = /usr/local/var/pyenv/versions/deploy_ec2
chdir = /Users/Joe/projects/django/deploy_ec2/django_app
module = config.wsgi.deploy
http = :8000

# 실행하려면
~ uwsgi --ini .config_secret/uwsgi/deploy.ini
```

### 프로젝트에 사용중인 static file을 지정한 폴더에 모아주는 명령

- static URL을 따로 설정 (base.py에서는 삭제 후)
- git으로 관리하지 않는다.(프로젝트에 만들어진 파일이 아님)
- 필요할때 collectstatic 하면 다시 생김
- 프로젝트에 만들어진 static 파일은 'static'폴더에 저장
- collectstatic 하면 'static' 파일도 모임

```
# settings/debug.py에 추가
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 터미널에서
$ ./manage.py collectstatic --settings=config.settings.debug

# 프로젝트 내부에 static_root 폴더가 생기고 static file들이 모임

# settings/base.py에 추가 (내가 만든 static 파일을 저장할 폴더)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
    ]
```

### Nginx 설치, 설정 (local)

```
# install nginx
$ brew install nginx

# 실행
$ nginx

# 실행 상태 확인
$ ps -ax | grep nginx

# nginx 종료
$ nginx -s stop
```

- 설정파일 : '/usr/local/etc/nginx/nginx.conf'
- 기본 html 위치 : '/usr/local/Cellar/nginx/1.12.0_1/html'
- localhost:8080으로 접속했을때 처음 열리는 html : '/usr/local/Cellar/nginx/1.12.0_1/html/index.html'

### Nginx 설치, 설정 (AWS)

#### Nginx 안정화 최신버전 사전세팅 및 설치

```
~ sudo apt-get install software-properties-common python-software-properties
~ sudo add-apt-repository ppa:nginx/stable
~ sudo apt-get update
~ sudo apt-get install nginx

# 버전 확인 
~ nginx -v
```

#### user 추가

```
~ sudo adduesr [username]
```

#### Nginx 동작 User 변경

```
~ sudo vi /etc/nginx/nginx.conf

# 아래 내용 수정
user [username];

server_names_hash_bucket_size 250;
```

#### AWS Console에서 80 포트를 열어줌

- Security Group에서 DeployEC2 그룹의 Inbound rule에 HTTP 추가

#### Nginx 내부 가상 서버

- nginx는 내부 가상버서를 돌려서 여러 도메일을 개별적으로 처리 가능

```
# 현재 데이터(설정파일)를 가지고 있는 사이트들
/etc/nginx/sites-available
site a
site b
site c
site d

# 현재 서비스를 하고 있는 사이트들(b, c는 서비스 중지, 파일은 보관)
/etc/nginx//sites-enable
(symbolic link)site a
(symbolic link)site d
```

- 서비스할 사이트에 대해 설정 파일을 만들어준다.

```
# /etc/nginx/sites-available에 ec2 파일 생성하여 아래 내용 작성
~ sudo vi /etc/nginx/sites-available/ec2

server {
			listen 80;
			server_name ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com;
			charset utf-8;
			client_max_body_size 128M;
			
			location / {
			uwsgi_pass		unix:///tmp/ec2.sock;
			include			uwsgi_params;
			}
}
```

#### http 요청 처리 방식

- EC2 -> (http) -> Django
- EC2 -> (http) -> uWSGI (WSGI) -> Django
- EC2 -> (http) -> Nginx -> (uWSGI's UnixSocket) -> uWSGI (WSGI) -> Django

#### uWSGI 파일 생성 (UnixSocket)

- local Django project에서 
- deploy_ec2/.config_secret/uwsgi/deploy.ini 파일 생성

```
[uwsgi]
home = /home/ubuntu/.pyenv/versions/deploy_ec2
chdir = /srv/deploy_ec2/django_app
module = config.wsgi_modules.deploy

# 실행할 유저
uid = deploy
# 실행할 그룹
gid = deploy

# UnixSocket
socket = /tmp/ec2.sock
# 소켓 소유 권한
chmod-socket = 666
# 소켓 소유자 (유저:그룹)
chown-socket = deploy:deploy

enable-threads = true
master = true
pidfile = /tmp/ec2_pid

# uwsgi가 종료되었을때 tmp/소켓 파일 자동 삭제
vacuum = true
```
- local에 있는 프로젝트를 aws로 업로드

```
# alias 사용
$ scp-ec2
```

- AWS에서 tmp 폴더의 권한을 변경

```
~ sudo chown -R deploy:deploy /tmp/
```

-  작성한 deploy.ini 파일을 실행 (요청을 받을 준비)

```
# 현재 유저가 tmp 폴더의 소유자일 경우
~ uwsgi --ini .config_secret/uwsgi/deploy.ini

# 현재 파일을 실행하는 유저가 tmp 폴더의 소유자일 경우 명령이 복잡해짐...
~ sudo -u deploy /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --ini .config_secret/uwsgi/deploy.ini

# uwsgi가 실행 중인지 확인 - 아래 2개 파일이 존재하면 실행 중..
/tmp/ec2.pid
/tmp/ec2.sock
```

#### 서비스할 사이트 목록 정리 (sites-enable)

```
# 기본 설정을 삭제 (링크되어있는 파일)
~ sudo rm /etc/nginx/sites-enable/default

# 서비스할 ec2 파일의 Symbolic link 생성
~ sudo ln -s ..sites-available/ec2 /etc/nginx/sites-enable/

# 서비스 사이트 목록이 변경되었으므로 nginx 재시작
~ sudo systemctl restart nginx
```

#### uWSGI 서비스 설정파일 작성 (시작 프로그램)

- 현재 실행 방식으로는 쉘을 종료하면 uWSGI가 종료되므로 service 설정 파일을 작성한다.
- 이 설정이 되어야 24시간 실행 됨..
- nginx는 service 설정 필요 없음

```
~ sudo vi /etc/systemd/system/uwsgi.service
```

```
# 아래 내용 작성

[Unit]
Description=uWSGI Emperor service
After=syslog.target

[Service]
ExecPre=/bin/sh -c 'mkdir -p /run/uwsgi; chown deploy:deploy /run/uwsgi'
ExecStart=/home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --uid deploy --gid deploy --master --emperor --ini /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini

Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

#### 참고

```
# uwsgi 시작
~ sudo systemctl start uwsgi

# uwsgi.service 상태(로그?) 확인
~ sudo systemctl status uwsgi.service
```














