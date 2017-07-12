## REST의 탄생 배경

#### 프론트엔드Front-End와 백엔드Back-End가 분리되기 시작

* 새로운 서비스 개발을 위해 개발작업 진행
* JSON 형태로 데이터를 제공하는 API를 제공하자고 동의
* RequestMethod(HTTP: GET, POST, PUT, DELETE)와 URL을 이용한 정의
* View 영역이 포함되지 않은 서버사이드Server-side 개발을 진행

#### 멀티플랫폼에 대한 지원을 위해 서비스 자원에 대한 아키텍처를 세우고 이용하는 방법을 모색

* 웹 + 모바일 웹
* 아이폰, 안드로이드

#### OPEN API

* 웹 2.0 시대 이후 다양한 매시업Mashup 서비스들이 출현할 수 있었던 밑바탕에는 깔끔하게 정리된 REST API 덕분이 아닐까?

## REST API 란 무엇인가?

### API(Application Programming Interface)란 무엇인가?

* 데이터와 기능의 집합을 제공하여 컴퓨터 프로그램간 상호작용을 촉진하며, 서로 정보를 교환가능 하도록 한다.

### REST

* 2000년 로이 필딩(Roy Fielding)이 박사학위 청구 논문에서 REST(Representational State Transfer)를 소프트웨어 아키텍처 스타일로 제안한 후 OPEN API를 개발하는 기본으로 급속도로 확산되고 있다.
* REST는 SOAP이 서비스 지향 구조인 것과 달리 자원지향구조(ROA: Resource Oriented Architecture)로 웹 사이트의 컨텐츠(Text, 이미지, 동영상), DB의 내용 등을 전부 하나의 자원으로 파악하여 각 자원의 고유한 URI(Uniform Resource Identifier)를 부여하고, 해당 자원에 대한 CRUD(Create, Read, Update, Delete) 작업을 HTTP의 기본 명령어인 POST, GET, PUT, DELETE를 통해서 처리한다.


### 메소드, CRUD, SQL 비교

|Method|CRUD|SQL|
|---|---|---|
|POST|Create|INSERT|
|GET|Read|SELECT|
|PUT|Update|UPDATE|
|DELETE|Delete|DELETE|

### REST API

* REST 구조 스타일에 적합한 Web API를 REST API라고 한다.


### REST API 정보제공 방식
* XML
* JSON
* RSS


### REST API 설계 전

##### 제공하려고 하는 자원(리소스, Resource)은 무엇인가?

##### 지원할 Content-type은 어떤 것들이 있는가?

* XML
* JSON
* RSS

##### 구현한 REST API 이용방법을 어떻게 설명할 것인가?
* Javadoc?
* 별도로 REST API를 사용하는 방법을 기술한 메뉴얼?
* 둘다!

### REST API 설계

* REST API를 통해 제공하려고 하는 자원(리소스, Resource)는 무엇인가?
* URI 경로path는 언제 복수로 써야하는가?
* 리소스의 상태를 업데이트하려면, 어떤 메소드를 사용해야 하는가?
* CRUD 가 아닌 연산을 어떻게 URL에 매핑하는가?
* 특정한 시나리오에 가장 적합한 HTTP응답은 무엇인가?
* 리소스 상태 표현의 버전은 어떻게 관리할 수 있는가?
* JSON에 포함된 하이퍼링크는 어떻게 구조화 하는가?

### URI(Uniform Resource Identifier) - URL 식별자 설계

* 식별자라고 할 수 있는 유일한 일은 대상을 나타내는 것이다. 역참조를 할 때가 아니라면 다른 정보를 얻기 위해서 URI의 내용을 들여다보지 말아야 한다.
* URI를 만들때부터 REST API 리소스 모델을 클라이언트 모델에 전달할 수 있어야 한다.

#### URI 형태

1. 규칙 : 슬래시 구분자(/)는 계층관계를 나타내는 데 사용한다.
1. 규칙 : URI 마지막 문자로 슬래시(/)를 포함하지 않는다.
1. 규칙 : 하이픈(-)은 URI 가독성을 높이는 데 사용한다.
1. 규칙 : 밑줄(_)은 URI에 사용하지 않는다.
1. 규칙 : URI 경로는 소문자가 적합하다.
1. 규칙 : 파일 확장자(ex: .json, .xml)는 URI에 포함시키지 않는다.
 
##### 리소스 모델링

- 웹서비스의 기반이 되는 URI는 REST API의 자원(리소스, Resource)가 된다.
 
##### 리소스 원형

* 도큐먼트 : 객체 인스턴스나 데이터베이스 레코드와 유사한 개념
* 컬렉션 : 서버에서 관리하는 디렉터리라는 리소스
* 스토어 : 클라이언트에서 관리하는 리소스 저장소
 
##### URI 경로 디자인

1. 규칙 : 도큐먼트 이름으로는 단수 명사를 사용해야 한다.
1. 규칙 : 컬렉션 이름으로는 복수 명사를 사용해야 한다.
1. 규칙 : 스토어 이름으로는 복수 명사를 사용해야 한다.
1. 규칙 : 경로 부분 중 변하는 부분은 유일한 값으로 대체한다.
1. 규칙 : CRUD 기능을 나타내는 것은 URI에 사용하지 않는다.

### 요청메소드(GET/POST/PUT/DELETE)

##### 메소드별 용도

GET : 리소스 상태의 표현을 얻을 때 사용
POST : 컬렉션에 새로운 리소스를 만들거나 컨트롤러를 실행할 때 사용
PUT : 새로운 리소스를 스토어에 추가하거나 기존 리소스를 갱신할 때 사용
DELETE : 리소스 제거
HEAD
OPTIONS

##### REST의 문제점

**사용할 수 있는 메소드가 4가지 밖에 없다!**

- Send mail 이라던가, Log Writer와 같은 기능(Function or method)은 어떻게 표현해야할까?

**이 문제를 해결할 것인가?**

- ‘메일을 보낸다send mail’라는 행위의 의미를 바꾼다.
- ‘POST /employees/1/send-mail’ : 직원 1에게 메일을 보낸다!

**문맥상으로 의미 변환이 불가능한 경우**

- ‘PUT’과 URI를 사용하여 제어control의 의미를 부여
- ‘PUT /employees/1/grade’ : 직원 1의 등급을 변경한다.
	- 	REST 기반의 아키텍처를 설계하려면 가장 어려운 것이 이 URI를 어떻게 정의하는 것이다. REST의 장점 중 하나는 이 URI와 HTTP Method만으로도 쉽게 의미를 파악할 수 있다는 것이기 때문에, URI 정의에 많은 노력을 기울이는 것이 좋다.

### 응답상태코드

* 1xx : 전송 프로토콜 수준의 정보 교환
* 2xx : 클라어인트 요청이 성공적으로 수행됨
* 3xx : 클라이언트는 요청을 완료하기 위해 추가적인 행동을 취해야 함
* 4xx : 클라이언트의 잘못된 요청
* 5xx : 서버쪽 오류로 인한 상태코드

###REST 장점/단점

* 장점 : 기존 웹 인프라를 그대로 이용할 있다. 쉽다.
* 단점 : 표준이 없어 관리가 어렵다.
  
  
    
참고한 [문서](https://slipp.net/wiki/pages/viewpage.action?pageId=12878219)