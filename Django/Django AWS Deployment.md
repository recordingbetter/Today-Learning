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

# WSGI application (base.py에서는 WSGI_APPLICATION 변수 삭제)
WSGI_APPLICATION = 'config.wsgi.debug.application'

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_debug['django']['allowed_hosts']
```

- settings/deploy.py 파일에 아래 내용 작성

```
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 배포모드니까 DEBUG는 False
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']
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

# yes 하면 접속됨 -> 터미널 화면 상단에 ubuntu@ip-... 확인
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

#### apt-get update
```
~ sudo apt-get update
```

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
~ brew install awscli

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

# 새로 지정할때,
~ aws configure --profile [aws 키의 이름]
```

#### Pillow 라이브러리 설치

[공식문서](https://pillow.readthedocs.io/en/3.4.x/installation.html#basic-installation)

```
~ sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

### vim에서 테마 변경

:colorscheme [tab]

## local project upload (로컬에서 테스트 완료 후 업로드)

- AWS 접속

```
# ssh -i [키 파일] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP]
$ ssh -i ~/.ssh/aws_joe.pem ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com

$ ssh -i ~/.ssh/aws_joe.pem ubuntu@13.124.12.223
```

### 로컬 프로젝트 복사 전에 AWS의 srv 폴더의 권한을 ubuntu로 변경

```
$ sudo chown -R ubuntu:ubuntu /srv/
```


- 로컬 프로젝트를 AWS에 복사

```
# scp -i [키 파일] -r [local project] ubuntu@[생성된 인스턴스의 Public DNS 또는 Public IP]:[destination]
$ scp -i ~/.ssh/aws_joe.pem -r /Users/Joe/projects/django/deploy_ec2 ubuntu@ec2-13-124-12-223.ap-northeast-2.compute.amazonaws.com:/srv/deploy_ec2

$ scp -i ~/.ssh/aws_joe.pem -r /Users/Joe/projects/django/deploy_ec2 ubuntu@13.124.12.223:/srv/deploy_ec2
```

### AWS의 프로젝트 폴더에 가상환경 설정 후 requirements 설치

```
~ pyenv virtualenv [파이썬버전] [가상환경 이름]
~ pyenv local [가상환경 이름]

~ pip install -r requirements.txt
```

### runserver

```
~ python manage.py runserver --settings=config.settings.deploy 0:8000
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

#### 해당 쉘의 환경변수 확인

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

- AWS에서 테스트 하려면...(이후 uwsgi 실행을 위해 확인함)

```
# .config_secret/uwsgi/deploy.ini에 아래 내용 작성

[uwsgi]
home = /home/ubuntu/.pyenv/versions/deploy_ec2
chdir = /srv/deploy_ec2/django_app
module = config.wsgi.deploy

uid = deploy
gid = deploy

socket = /tmp/ec2.sock
chmod-socket = 666
chown-socket = deploy:deploy

enable-threads = true
master = true
pidfile = /tmp/ec2.pid

vacuum = true
logger = file:/tmp/uwsgi.log


# 실행하려면

~ ~~.uwsgi --ini .config_secret/uwsgi/deploy.ini~~

~ sudo /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --http :8000 --ini /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini
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
$ sudo nginx -s stop
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

##### Nginx conf 파일을 Django 프로젝트에서 만들어줘도 된다.

- deploy/.config_secret/nginx/nginx.conf

```
user deploy;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	 server_names_hash_bucket_size 250;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;
	gzip_disable "msie6";

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}

#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}

```

- deploy/.config_secret/nginx/ec2.conf

```
server {
    listen 80;
    server_name *.compute.amazonaws.com;
    charset utf-8;
    client_max_body_size 128M;

    location / {
        uwsgi_pass    unix:///tmp/ec2.sock;
        include       uwsgi_params;
    }
}
```

- AWS에서 아래 명령으로 기존 config 파일에 덮어씌움

```
~ sudo cp -f /srv/deploy_ec2/.config_secret/nginx/nginx.conf /etc/nginx/nginx.conf
~ sudo cp -f /srv/deploy_ec2/.config_secret/nginx/ec2.conf /etc/nginx/sites-available
```

- 아래 명령으로 서비스할 사이트 목록 정리 (링크 생성. 아래에도 내용 있음)

```
~ sudo ln -sf /etc/nginx/sites-available/ec2.conf /etc/nginx/sites-enabled/ec2.conf
~ sudo cp -f /srv/deploy_ec2/.config_secret/uwsgi/uwsgi.service /etc/systemd/system/uwsgi.service

# 기존 default 삭제 (이제 default index.html은 볼 수 없음)
~ sudo rm -rf /etc/nginx/sites-enabled/default
```


#### AWS Console에서 80 포트를 열어줌

- Security Group에서 DeployEC2 그룹의 Inbound rule에 HTTP 추가

#### Nginx 내부 가상 서버

- nginx는 내부 가상버서를 돌려서 여러 도메인을 개별적으로 처리 가능

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
# pid는 필요없음...
pidfile = /tmp/ec2.pid

# uwsgi가 종료되었을때 tmp/소켓 파일 자동 삭제
vacuum = true
# 오류시 로그파일 작성
logger = file:/tmp/uwsgi.log

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

# 8000포트로 실행 (웹브라우저에서 확인 가능)
~ sudo /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --http :8000 --ini /srv/deploy_ec2/.config_secret/uwsgi/deploy.ini
```

- ini 파일을 사용하지 않을 경우

```
# 7/4
~ /root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug

# 가상환경 내부에서
~ uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug
```

- uwsgi 실행 확인

```
# uwsgi가 실행 중인지 확인 - 아래 2개 파일이 존재하면 실행 중..
/tmp/ec2.pid
/tmp/ec2.sock
```

#### 서비스할 사이트 목록 정리 (sites-enable)

```
# 기본 설정을 삭제 (링크되어있는 파일)
~ sudo rm /etc/nginx/sites-enable/default

# 서비스할 ec2 파일의 Symbolic link 생성
~ sudo ln -s ..sites-available/ec2/

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

## Docker

- 각 서버 운영체제에 맞는 가상OS을 만들어 컨테이너 단위로 관리
- 메모리에 저장되며, docker를 종료하거나 시스템이 종료되면 없어진다. (이미지를 파일로 만들 수 있음)

### local에서 설치, 테스트

- [다운로드 후 설치](https://store.docker.com/editions/community/docker-ce-desktop-mac?tab=description)

```
# ubuntu 16.4 버전으로 컨테이너 생성
$ docker run --rm -it ubuntu:16.04 /bin/bash
# 컨테이너 쉘로 진입한다.

# 터미널 새로운 창에서 컨테이너 정보 확인
$ docker ps

# 생성된 컨테이너에 파일 복사
$ docker cp . [자동생성 컨테이너 이름]:/srv/deploy_ec2

# 컨테이너 쉘에서 확인
root@019f938cf887:/srv/deploy_ec2# l
README.md  django_app/  requirements.txt
```

### 서버 환경을 자동으로 셋팅하기 위한 도커 파일 생성

- 로컬 deploy_ec2 폴더에 dockerfile 이름으로 도커파일 생성

```
# ubuntu 설치
FROM        ubuntu:16.04
MAINTAINER  recordingbetter@gmail.com

# 필요한소스설치 (-y는 자동으로 y를 눌러줌)
RUN         apt-get -y update
RUN         apt-get install -y python-pip
RUN         apt-get install -y git vim

# pyenv
RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH

RUN         pyenv install 3.6.1

# zsh 설치, 적용
RUN         apt-get -y install zsh
RUN         wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN         chsh -s /usr/bin/zsh

RUN         echo '\n# pyenv\n' >> ~/.zshrc
RUN         echo 'export PATH="/home/ubuntu/.pyenv/bin:$PATH"\n' >> ~/.zshrc
RUN         echo 'eval "$(pyenv init -)"\n' >> ~/.bash_profile
RUN         echo 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.zshrc

EXPOSE      4567

```

### 같은 이미지를 여러번 생성하지 않게 하기 위해 Dockerfile을 여러개 생성

- 바뀌지 않을 셋팅의 이미지를 만든다.

```
# Dockerfile.ubuntu 파일 생성
# ubuntu의 기본 설정
# ubuntu 설치 ( 원래는 배포용 유저를 만들어야함. 여기서는 root로 작업함 )
FROM        ubuntu:16.04
MAINTAINER  recordingbetter@gmail.com

# 필요한소스설치 (-y는 자동으로 y를 눌러줌)
RUN         apt-get -y update
RUN         apt-get install -y python-pip
RUN         apt-get install -y git vim

# pyenv
RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH

RUN         pyenv install 3.6.1

# zsh 설치, 적용
RUN         apt-get -y install zsh
RUN         wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
RUN         chsh -s /usr/bin/zsh

# pyenv settings
RUN         echo '\n# pyenv\n' >> ~/.zshrc
RUN         echo 'export PATH="/home/ubuntu/.pyenv/bin:$PATH"\n' >> ~/.zshrc
RUN         echo 'eval "$(pyenv init -)"\n' >> ~/.zshrc
RUN         echo 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.zshrc

# pyenv virtualenv
RUN         pyenv virtualenv 3.6.1 deploy_eb_docker

# uwsgi install
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install uwsgi

# Nginx install
RUN         apt-get -y install nginx

EXPOSE      4567
```

- 위에서 만들어진 이미지를 베이스로 바뀔 수 있는 설정의 Dockerfile을 만든다.

```
FROM        eb_ubuntu
MAINTAINER  recordingbetter@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/deploy_eb/docker 폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb/docker 와 같음
WORKDIR     /srv/deploy_eb_docker
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/debug.txt

# 80포트와 8000포트를 열어줌
EXPOSE      80 8000
```

- 아래 명령으로 위 스크립트를 실행

```
# docker build -t <사용할 이미지 이름> <프로젝트 경로> -f <dockerfile이 존재하는 경로>

# 바뀌지 않을 ubuntu 기본 설정 이미지
$ docker build -t eb_ubuntu . -f .dockerfiles/dockerfile.ubuntu

# 바뀔 수 있는 설정의 이미지
$ docker build -t eb . -f .dockerfiles/dockerfile
```

- 도커 이미지 실행

```
$ docker run --rm -it testapp /bin/zsh

# -p <port1>:<port2>
# 컨테이너가 실행되는 환경의 port1로 들어오는 연결을 컨테이너의 port2로 연결해줌
$ docker run --rm -it -p 4040:8080 eb /bin/zsh

# runserver로 확인
~ ./manage.py runserver --settings=config.settings.deploy 0:8000

```

- 도커 이미지 리스트

```
docker images
```

### 터미널 새 창을 열어 실행 중인 컨테이너에 접속하기

```
# 실행 중인 컨테이너 확인
~ docker ps

# 실행 중인 컨테이너에 접속
~ docker exec -it [실행중인 컨테이너 가이름] /bin/zsh
```

### Supervisor

- 설정된 프로그램 실행 상태를 모니터하고 있다가 종료되면 바로 다시 실행시킴

- supervisor 설치

```
~ sudo apt-get install supervisor
```

- [project]/.config/supervisor/nginx.conf

```
[program:nginx]
command = nginx
```

- [project]/.config/supervisor/uwsgi.conf

```
[program:uwsgi]
command=/root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --ini /srv/deploy_eb_docker/.config/uwsgi/uwsgi-app.ini
```





### 장고 환경 설정

- 쉘 단위로 적용됨. (터미널 탭마다 다르게 할 수 있음)
- runserver 등 할때 settings 값 안줘도 됨

```
$ export DJANGO_SETTINGS_MODULE=config.settings.deploy
```



## AWS RDS 사용

### DRS 인스턴스 만들기

### 장고 프로젝트에서 디비 셋팅

### migrate - deploy

### postgrespl db에 접속하여 확인

```
$ psql --host=deploy-eb-rds.chuejjlksokd.ap-northeast-2.rds.amazonaws.com --port=5432 --username=recordingbetter --dbname=eb_database

# 테이블 리스트
\dt

# 종료
\q
```

### .requirements/deploy.py에 추가

```
psycopg2<2.8
```

### admin css 적용을 위해 collectstatic 추가

- .static_root 폴더 이동, .gitignore에 추가

```
# config/settings/deploy.py
- STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
```

### member app

- member app 추가
- AbstractUser를 상속받은 MyUser 모델을 생성
- migration을 위해 기존 테이블들을 초기화

```
$ ./manage.py migrate [name] zero 

# 처음 django project를 만들때 user model을 정해주지 않으면 django에서 자동으로 User 모델을 만들어 다른 앱들과 연결시켜두기 때문. 이 연결 전으로 되돌려 migrate 해야한다.
```

- migrate 하여 확인

```
$ ./manage.py migrate
$ ./manage.py showmigrations
```

- static_root, media 경로 셋팅
- 





# Python shell에서 AWS S3 생성하기

- 생성 전에 AWS IAM에서 User에 S3 FullAccess 권한 부여

In [1]: import boto3

In [2]: session = boto3.Session()

In [4]: client = session.client('s3')

In [6]: client.create_bucket(Bucket='deploy-eb-docker-joe', CreateBucketConfiguration={'LocationConstraint
   ...: ': 'ap-northeast-2'})
Out[6]:
{'Location': 'http://deploy-eb-docker-joe.s3.amazonaws.com/',
 'ResponseMetadata': {'HTTPHeaders': {'content-length': '0',
   'date': 'Wed, 05 Jul 2017 07:43:47 GMT',
   'location': 'http://deploy-eb-docker-joe.s3.amazonaws.com/',
   'server': 'AmazonS3',
   'x-amz-id-2': 'l/sksWwOWVn7189meEYxnXuXtQ4G7JpXi8Fw5dXVVfX6qS+gy2wYWXdKBcqIag00PWnldsSvilA=',
   'x-amz-request-id': 'E902BCC379765CA0'},
  'HTTPStatusCode': 200,
  'HostId': 'l/sksWwOWVn7189meEYxnXuXtQ4G7JpXi8Fw5dXVVfX6qS+gy2wYWXdKBcqIag00PWnldsSvilA=',
  'RequestId': 'E902BCC379765CA0',
  'RetryAttempts': 0}}



docker none 이미지 삭제
docker rmi $(docker images -f "dangling=true" -q)


docker tag <ori> <make>

pip install awsebcli

eb init
eb create

eb deploy

오류 확인
eb ssh
cat /var/log/eb-activity.log


ebingnore

!.config_secret/

eb open


2c05

