[.ebextensions(folder)](http://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/ebextensions.html)

도커를 사용하지 않고 nginx, uwsgi를 안쓰면 EB에서 아파치? 등으로 해줌

yum 아마존 리녹스의 패키지 설치 파일


leader_only

EB + Docker
[read this](http://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create_deploy_docker.html)




### S3 Bucket create

```
# ~/.aws/credential

[eb_deploy]
aws_access_key_id = [key]
aws_secret_access_key = [key]
```

```
# ~/.aws/config
[eb_deploy]
region = ap-northeast-2
output = json
```

```
# Python shell
>>> import boto3
>>> session = boto3.Session(profile_name='eb_deploy')
>>> client = session.client('s3')
# Bucket 이름은 유일해야한다.
>>> client.create_bucket(Bucket='[bucket_name]', CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'})
```

```
# django의 key 파일에 [key] 입력
# .config_secret/settings_deploy.json
{
  "aws": {
    "access_key_id": "[key]",
    "secret_access_key": "[key]",
    "s3_bucket_name": "[bucket_name]",
    "s3_signature": "s3v4",
    "s3_region": "ap-northeast-2"
  }
}
```

```
# s3 연결 확인
pym collectstatic
```

### ElasticBeanstalk


export AWS_EB_PROFILE = eb_deploy

eb ssh


RDS에 DB 여러개 만들어 쓸 수 있음


psql --host=eb-deploy-docker-joe.cyyhwkunq9gl.ap-northeast-2.rds.amazonaws.com --user=recordingbetter --port=5432 postgres

CREATE DATABASE eb_database OWNER=sdsf;



EB ssh

sudo docker exec [running docker image ID] /root/.pyenv/versions/app/bin/python /srv/[app name]/django_app/manage/py migrate --noinput

sudo docker exec `sudo docker ps --no-trunc -q` /root/.pyenv/versions/app/bin/python /srv/[app name]/django_app/manage/py migrate --noinput



custom management commands

management/commands/[command name].py

### EB 내부의 Docker에 접속

```
# eb에 접속
$ eb ssh

# 실행 중인 docker 이미지 확인
$ sudo docker ps

# 실행 중인 컨테이너에 접속
$ docker exec -it [실행중인 컨테이너 이름] /bin/zsh
```

### migrations 파일 위치 확인
```
$ find . -path "\*/migrations/\*.py"
```


2017-08-03 10:54:01.302724



