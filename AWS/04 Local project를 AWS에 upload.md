## Local project를 AWS에 upload

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

