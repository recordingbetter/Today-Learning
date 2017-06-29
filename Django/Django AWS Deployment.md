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
sudo apt-get install language-pack-ko
sudo locale-gen ko_KR.UTF-8
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
sudo apt-get install python-pip
```

#### zsh 설치

```
sudo apt-get install zsh
```


#### oh-my-zsh 설치

```
sudo curl -L http://install.ohmyz.sh | sh
```


#### Default shell 변경

```
sudo chsh ubuntu -s /usr/bin/zsh
```

#### pyenv requirements설치

[공식문서](https://github.com/yyuu/pyenv/wiki/Common-build-problems)

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

#### pyenv 설치

```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

#### pyenv 설정 .zshrc에 기록

```
vi ~/.zshrc

# 아래 내용 추가
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Python 3.6.1 install

```
$ pyenv install 3.6.1
```

### AWS Command Line Interface 설치

```
$ pip install awscli
# 버전 확인
$ aws --version
```

### AWS Configure

```
$ aws configure
AWS Access Key ID [None]: 만든 유저 키
AWS Secret Access Key [None]: 만든 유저 키
Default region name [None]: ap-northeast-2
Default output format [None]: json
```

#### Pillow 라이브러리 설치

[공식문서](https://pillow.readthedocs.io/en/3.4.x/installation.html#basic-installation)

```
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
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







