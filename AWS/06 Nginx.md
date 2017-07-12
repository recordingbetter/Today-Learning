## Nginx / Supervisor

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

- [project]/.config/nginx/nginx.conf

```
user root;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

# Docker로 실행할 경우 필요함
daemon off;

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

- [project]/.config/nginx/nginx-app.conf

```
server {
    listen 80;
    server_name *.compute.amazonaws.com;
    charset utf-8;
    client_max_body_size 128M;

    location / {
    # 소켓파일 위치
        uwsgi_pass    unix:///tmp/eb.sock;
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

### 참고

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

#### http 요청 처리 방식

- EC2 -> (http) -> Django
- EC2 -> (http) -> uWSGI (WSGI) -> Django
- EC2 -> (http) -> Nginx -> (uWSGI's UnixSocket) -> uWSGI (WSGI) -> Django


### sites-available / sites-enabled

- 서비스할 사이트에 대해 설정 파일을 만들어준다.
- /etc/nginx/sites-available에 ec2 파일 생성하여 아래 내용 작성

```
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

- sites-enabled에 서비스할 사이트 파일 링크

```
# 기본 설정을 삭제 (링크되어있는 파일)
~ sudo rm -rf /etc/nginx/sites-enable/default

# 서비스할 ec2 파일의 Symbolic link 생성
~ sudo ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx.conf

# 서비스 사이트 목록이 변경되었으므로 nginx 재시작
~ sudo systemctl restart nginx
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








