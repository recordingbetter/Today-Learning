# 장고란?

- 파이썬에서 같은 작업을 반복하지 않고 데이터베이스를 쉽게 사용하게 해주는 프레임워크

### 프레임 워크 (frame work)

- 프로젝트마다 반복되는 작업을 쉽게 할 수 있게 만든 프로그램


# 장고 시작하기

### SSH key 생성하여 적용

[https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/]()

1. 터미널에서 홈폴더에 .ssh 폴더를 생성한다.
2. `$ ssh-keygen -t rsa -b 4096 -C "깃헙 계정"`
3. 만들어진 파일 id_rsa.pub의 내용을 복사
	`$ cat id_rsa.pub`
4. github.com/profile/SSH and GPG keys 항목에 SSH key를 추가하여 붙여넣는다.
5. github의 저장소를 생성하여 나오는 SSH 주소 "git@github.com:~~"로 git을 생성한다.



### 1. 프로젝트 시작

```shell
# 장고 프로젝트를 새로 만든다.
$ ~/djangogirls$ django-admin startproject mysite

# 상위 폴더 이름을 변경
$ mv mysite django_app

# 명령어 확인
$ ./manage.py

# 로컬에서 서버를 시작 (컨트롤+C)로 종료
$ ./manage.py runserver
```


