## uWSGI

### 프로젝트에서 wsgi 파일 분리

```
# django_app/config/wsgi/debug.py
import os
from django.core.wsgi import get_wsgi_application

# 환경변수 설정 (os.environ)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")

application = get_wsgi_application()
```

```
# django_app/config/wsgi/deploy.py
import os
from django.core.wsgi import get_wsgi_application

# 환경변수 설정 (os.environ)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.deploy")

application = get_wsgi_application()
```

### uwsgi 실행

```
# uwsgi --http :8000 --home (virtualenv경로) --chdir (django프로젝트 경로-소스루트) -w (wsgi 설정파일)

# local에서 test
$ uwsgi --http :8000 --home /usr/local/var/pyenv/versions/deploy_ec2 --chdir /Users/Joe/projects/django/deploy_ec2/django_app -w config.wsgi.debug

# AWS에서
$ uwsgi --http :8000 --home ~/.pyenv/versions/deploy_ec2 --chdir /srv/deploy_ec2/django_app -w config.wsgi.deploy
```

- ini 파일을 사용하지 않을 경우

```
# 7/4
~ /root/.pyenv/versions/deploy_eb_docker/bin/uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug

# 가상환경 내부에서
~ uwsgi --http :8000 --chdir /srv/deploy_eb_docker/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug
```

### uwsgi를 실행할 설정파일 생성 (ini)

- local에서 테스트

```
# .config/uwsgi/debug.ini

[uwsgi]
home = /usr/local/var/pyenv/versions/deploy_ec2
chdir = /Users/Joe/projects/django/deploy_ec2/django_app
module = config.wsgi.debug
http = :8000

# 실행하려면
$ uwsgi --ini .config/uwsgi/debug.ini
```

- AWS에서 테스트 (이후 uwsgi 실행을 위해 확인함)

```
# .config_secret/uwsgi/deploy.ini에 아래 내용 작성

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

# 실행하려면
~ sudo /home/ubuntu/.pyenv/versions/deploy_ec2/bin/uwsgi --http :8000 --ini /srv/deploy_ec2/.config/uwsgi/deploy.ini
```

- AWS에서 tmp 폴더의 권한을 변경

```
~ sudo chown -R deploy:deploy /tmp/
```

- uwsgi 실행 확인

```
# uwsgi가 실행 중인지 확인 - 아래 2개 파일이 존재하면 실행 중..
/tmp/ec2.pid
/tmp/ec2.sock
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
