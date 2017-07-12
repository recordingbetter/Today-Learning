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

# pyenv 설치
RUN         apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
RUN         curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
ENV         PATH /root/.pyenv/bin:$PATH

# python 설치
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

# Superviser
RUN         apt-get -y install supervisor

EXPOSE      4567
```

- 위에서 만들어진 이미지를 베이스로 바뀔 수 있는 설정의 Dockerfile을 만든다.

```
# eb 이미지 생성

FROM        eb_ubuntu
MAINTAINER  recordingbetter@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/deploy_eb/docker 폴더에 복사
COPY        . /srv/deploy_eb_docker
# cd /srv/deploy_eb/docker 와 같음
WORKDIR     /srv/deploy_eb_docker

# requiremments.txt 설치
RUN         /root/.pyenv/versions/deploy_eb_docker/bin/pip install -r .requirements/deploy.txt

# .config/supervisor/uwsgi.conf로 이동
#RUN         uwsgi --http :8000 --chdir /srv/deploy_ec2/django_app --home /root/.pyenv/versions/deploy_eb_docker -w config.settings.debug

# supervisor 파일 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/


# nginx 설정파일, nginx 사이트 파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/

# nginx 링크 작성
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx.conf
RUN         rm -rf /etc/nginx/sites-enabled/default

CMD         supervisord -n
# 80포트와 8000포트를 열어줌
EXPOSE      80 8000
```

- 아래 명령으로 위 스크립트를 실행

```
# docker build -t <사용할 이미지 이름> <프로젝트 경로> -f <Dockerfile이 존재하는 경로>

# 바뀌지 않을 ubuntu 기본 설정 이미지
$ docker build -t eb_ubuntu . -f .dockerfiles/Dockerfile.ubuntu

# 바뀔 수 있는 설정의 이미지
$ docker build -t eb . -f .dockerfiles/Dockerfile
```

- 도커 이미지 실행

```
# 컨테이너 안에서 zsh이 실행된다. (uwsgi 꺼짐...)
$ docker run --rm -it eb /bin/zsh

# -p <port1>:<port2>
# 컨테이너가 실행되는 환경의 port1로 들어오는 연결을 컨테이너의 port2로 연결해줌
$ docker run --rm -it -p 4040:8080 eb /bin/zsh

# zsh에 들어가지 않고 실행 (모든 실행들이 유지됨)
# 9000포트로 들어오는 연결을 도커가 80포트로 nginx에 전달해줌
$ docker run --rm -it -p 9000:80 eb

# runserver로 확인
~ ./manage.py runserver --settings=config.settings.deploy 0:9000
```

- 도커 이미지 리스트

```
$ docker images
```

### 터미널 새 창을 열어 실행 중인 컨테이너에 접속하기

```
# 실행 중인 컨테이너 확인
$ docker ps

# 실행 중인 컨테이너에 접속
$ docker exec -it [실행중인 컨테이너 이름] /bin/zsh
```
