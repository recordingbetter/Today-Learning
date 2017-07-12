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

### root user -> IAM에서 생성

### 권한 제한 유저 

- Security Group/User 생성
- 만들어진 인스턴스에 배정 (Networking)

#### Programmatic access User

- Users -> Add User -> User name 입력 -> Access type : Programmatic access 
- 기존 그룹을 복사하여 넣거나 새로운 그룹 생성 (권한 그룹)
- Access key ID와 Secret access key를 보관하거나 cvs 파일로 다운로드 (단 한번만 보인다)
- 해당 user의 account no, Access key ID, Secret access key를 사용하여 server에 접속 가능
- AWS Management Console에 로그인할 수 없다.

#### AWS Management Console access User

- Users -> Add User -> User name 입력 -> Access type : AWS Management Console access 
- 기존 그룹을 복사하여 넣거나 새로운 그룹 생성 (권한 그룹)
- account no와 Password를 복사하여 보관하거나 cvs 파일로 다운로드 (단 한번만 보인다)
- 해당 user의 account no, Username, Password를 사용하여 Management Console에 로그인 가능


