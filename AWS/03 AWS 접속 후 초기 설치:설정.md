## AWS 접속 후 초기 설치/설정 (ubuntu)

#### apt-get update

```
~ apt-get update
```

#### python-pip설치

```
~ sudo apt-get install python-pip
```

#### git, vim 설치

```
~ sudo apt-get install git vim
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

#### Python 3.6.1 install

```
~ pyenv install 3.6.1
```

#### uwsgi install (가상 환경 내에 설치)

```
~ sudo pip install uwsgi
```

#### Nginx install

```
~ sudo apt-get install nginx
```

#### Supervisor install

```
~ sudo apt-get install supervisor
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

