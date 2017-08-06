# Django CORS

## Cross-Domain
- Cross Domain이란 서로 다른 도메인에서 Javascript로 접근하려 하거나 다른 서버에 Ajax통신의 결과를 받는 행위 
## 동일 출처 정책(Cross-Domain Policy)
- 스크립트는 자신을 포함한 문서와 다른 서버에서 불러온 문서의 내용은 읽을 수 없고 다른 서버에서 불러운 문서에는 이벤트 리스너를 등록할 수 없다.  이것은 스크립트가 사용자의 입력을 캐내어 다른 페이지로 흘려보내는 것을 막기 위함이다.(보안상의 이유)

## CORS (Cross-Origin Resource Sharing)
- 요즘 사용되는 모던 브라우저는 자바스크립트 인터프린터가 도입됐으며 보안상의 문제를 막기위해 JS의 동일 출처 정책으로 Cross-Domain 이슈를 제한함(Cross-Domain Policy)
- 보안상의 문제 없이 Ajax등의 통신을 하기 위해 사용되는 메커니즘이 CORS임
- CORS 표준은 웹 브라우저가 사용하는 정보를 읽을 수 있도록 허가된 출처 집합를 서버에게 알려주도록 허용하는 HTTP 헤더를 추가함으로써 동작

## Django REST API에 CORS 적용
- Django App에서 CORS 메커니즘을 적용하기위해 Response Header에 CORS Header를 추가
- JSON-P는 유용하지만 GET 요청에 엄격히 제한되기 때문에 XMLHttpRequest를 기반으로 동일안 도메인 요청과 마찬가지로 서로 다른 도메인 간 요청을 할 수 있게끔 함

1. Django CORS Headers 설치 - pip install django-cors-headers  
2. Django CORS Headers 설치 반영 - settings.py INSATLLED_APP에  ‘corsheaders’ 추가

3. Response 수신을 위한 middleware 추가 - settings.py MIDDLEWARE에 ‘corsheaders.middleware.CorsMiddleware’ 추가 - corsheaders 미들웨어를 추가할 때는 반드시 MIDDLEWARE 최상단에 위치시키도록 해야 함 
4. Django에서 CORS 미들웨어의 대한 구성 설정 - CORS\_ORIGIN\_WHITELIST에 사이트 간 요청을 허용하는 호스트를 추가하거나 CORS\_ORIGIN\_ALLOW_ALL을 True로 설정하여 모든 호스트를 허용해야함 - CORS\_ALLOW\_CREDENTIALS : True면 쿠키가 사이트 간 HTTP 요청에 포함되도록 허용. 기본값은 Flase - CORS\_ORIGIN\_WHITELIST : 사이트 간 HTTP 요청을 할 수 있도록 허가 된 원본 호스트 이름 목록 보통 배포 환경에 특정 호스트만 추가하여 허용한다. - CORS\_ORIGIN\_ALLOW\_ALL : 모든 사이트들간 HTTP 요청을 가능하게 하며 보통 개발 환경에서 True로 설정함 - 나머지 구성은 Django-CORS-Headers Git 참고 (https://github.com/ottoyiu/django-cors-headers)

