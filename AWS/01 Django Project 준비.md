## Django Deployment Check List

- Django에서의 Check list는 아래에서 확인.

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

- settings\_debug.json 파일을 .config\_secret 폴더에 만든다.

```json
{
  "django": {
    "allowed_hosts": [
        "localhost",
        "127.0.0.1"
    ]
  }
}
```

- settings\_deploy.json파일을 .config\_secret 폴더에 만든다.

```json
{
  "django": {
    "allowed_hosts": [
      ".compute.amazonaws.com"
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

- settings/deploy.py 파일을 만들고 아래 내용 작성

```
# base 파일의 내용을 모두 상속받음
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = False

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']
```

- local에서 작동 확인

```
# settings 파일이 이동되고 이름이 변경되었으므로 runserver 옵션 필요
$ ./manage.py runserver --settings=config.settings.debug
```

- .gitignore에 내용 추가

```
.config_secret/
```
