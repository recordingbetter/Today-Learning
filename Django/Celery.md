# Celery

- 분산 작업 큐
- 처리 시간이 긴 작업들을 task queue로 모아서 백그라운드에서 처리할 수 있게 한다.

### Celery 설치

- 이후 redis를 사용하기 위해 번들로 설치

```
$ pip install 'celery[redis]'
```

### Broker

- Celery에 작업을 요청할때 사용된다.
- 작업 태스크가 쌓이는 공간.
- RabbitMQ, Redis 등이 있고 DB를 사용할 수도 있다.
- DB를 Broker로 사용하는 것은 권장하지 않는다.




django signal dispatcher


$ brew install redis
실행
$ redis-server

$ celery -A config worker -l info

AWS ElastiCashe
-> Celery 사용








임시로 필드 값끼리 계산
django aggregate / annotate

F 표현식 - 자신의 필드값을 참조하게 함


