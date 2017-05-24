## 모듈 module

### 모듈(module) 불러오기

- import [filename]
- 파이썬 파일은 각각의 하나의 모듈로 취급되며 다른 파일에서 불러와 사용 가능하다.
- 함수, 변수 등을 선택적으로 불러올 수 있다.

### \_\_name\_\_ 변수

- 파이썬 인터프리터를 이용해 실행된 코드는 `__name__` 값이 `__main__` 값을 가진다.
- 직접 실행된 파일에만 `__main__` 값이 나온다.
- `if`문을 사용해 `__name__`값을 확인하여 결과가 나오는 것을 선택할 수 있다.

```python
# 파일을 불러올 경우 / game모듈의 play_game 사용할때 위치를 표시해준다.
import game
...
game.play_game()

# 각 모듈은 독립된 네임스페이스를 가진다. namespace
# 패키지 functions의 game 모듈에서 play_game, title을 불러온다.
# 이 경우, 함수를 호출할때, 모듈을 따로 표시하지 않는다.
from functions.game import play_game, title
...
play_game()

# 불러온 함수나 변수가 같은 이름이 있을때 불러올때 별칭을 정해줄 수 있다.
from functions.game import title as game_title 

# 패키지 functions에서 game 모듈을 불러올 경우 / game모듈의 play_game 사용할때 위치를 표시해준다.
from functions import game
...
game.play_game()
```

### 커맨드라인에서 인자 전달

- 프로그램 실행 시 인자를 전달할 수 있다.
- 내장 `sys` 모듈을 import하여 `argv` 리스트로 확인

```python
import sys
print(sys.argv)

$ python 파일이름, arg1, arg2
[파일이름, arg1, arg2]
```

## 패키지

- 모듈을 모아놓은 특별한 폴더
- 계층 구조를 가질 수 있으며 모튤들을 모아놓을 수 있다.
- 패키지로 사용할 폴더에 `__init__.py` 파일을 넣어주면 해당 폴더는 패키지로 취급된다.(3부터는 필요없음)
- 모듈과 동일하게 import할 수 있다.
- 

```python
# functions라는 패키지에서 game 모듈에서 play_game와 title을 불러옴
from functions.game import play_game, title
```

```python
├── func
│   ├── __init__.py
│   ├── game.py
│   └── shop.py
└── lol.py
```


### `*`, `__all__`

- 모듈을 불러올때 `*`를 사용하면 모든 식별자를 불러오게 된다.
- 이때 모듈에 `__all__`을 지정해두면 불러오고 싶은 식별자만 불러온다.

```python
# 모듈 처음에 아래와 같이 지정하면 title, play_game만 불러오게 된다.
__all__ = (
    'title',
    'play_game',
)
```

## 클래스

### 객체지향 프로그래밍

- 파이썬의 모든 것은 객체이며, 객체를 사용할 때에는 변수에 해당 객체를 참조 reference 시켜 사용한다.
- 객체는 함수와 변수를 가지며, 객체가 가진 변수는 속성(attribute), 함수는 매서드(method)라고 부른다.
- 객체는 특정한 클래스의 형태를 가진 인스턴스를 나타낸다.  

- 불러오는 방법

```python
# 파일 이름 앞에 .을 붙이면 같은 폴더에서 찾는다.
# 팩키지로 가정한다.
from .class_sample import 클래스
# 파일 이름 앞에 .을 붙이면 같은 폴더에서 찾는다.
from (폴더이름).class_sample import 클래스

# 파일 이름 앞에 아무것도 없으면 해당 프로젝트의 루트 폴더에서 찾는다.
from class_sample import 클래스

# 인터프리터에서 모듈 위치를 정해준다.
$ pyrhon -m practice.calss_practice
```

### 클래스

- 객체를 만들기 위한 틀.
- 대문자로 시작한다.

```python
# class_sample.py

class Shop:
	def __init__(self, name):
		self.name = name
```

- `__init__`는 클래스를 사용한 객체의 초기화 매서드
- 객체를 생성할때 인자를 어떻게 전달받고, 받은 인자를 이용해 어떤 객체를 생성할지 정의

##### 객체 생성

```python
from class_sample import Shop
lotteria = Shop('Lotteria')
```

1. Shop 클래스를 찾는다.
2. Shop 클래스형 객체를 메모리에 생성한다.
3. 생성한 객체의 초기화 매서드 `__init__`를 호출한다.
4. name 값을 정하고, 만들어진 객체를 반환한다.
5. lotteria 변수에 반환된 객체를 할당한다.

- 첫번째 인수로 항상 `self`를 가진다.
- 인스턴스를 이용해 매서드를 호출할때 호출한 인스턴스가 자동으로 전달된다.
- 하나의 매서드를 여러 객체가 공유할 수 있다.

##### 파이참에서 프로젝트 폴더에 `mark as source root`를 해주면 자동완성 됨

##### 클래스 변수 

- 클래스 정의 아래, 매서드들 위에 사용된 변수.
- 해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수
- 외부에서는 `클래스명.변수`로 접근 가능

##### 인스턴스 변수

- 인스턴스 내부에서 사용되는 변수.
- `self.변수명`은 인스턴스 변수. 객체별로 다른 값을 갖는다.
- 클래스 내부에서는 `self.변수명`로 엑세스, 클래스 밖에서는 `객체변수.인스턴스변수`와 같이 엑세스

## 매서드 method

### 인스턴스 매서드

- 첫번째 인수로 항상 `self`를 가진다.
- 인스턴스를 이용해 매서드를 호출할때 호출한 인스턴스가 자동으로 전달된다.
- 가장 많이 사용되는 형태

```python
class Shop:
	def __init__(self, name, shop_type, address):
		self.name = name
		self.shop_type = shop_type
		self.address = address
		
	def show_info(self):
		
		
	def change_type(self, shop_type):
		self.shop_type = shop_type
		
```
		
### 클래스 매서드

- 클래스 속성(클래스 변수 등)에 대해 동작하는 매서드
- 호출 주체가 클래스, 첫번째 인자도 클래스.
- 인스턴스가 첫번째 인자로 주어져도 해당 인자의 클래스로 자동으로 바꾸어 전달된다.
- @classmethod 데코레이터를 붙여 선언, 첫번재 인자는 관용적으로 `cls`

### 스태틱 매서드

- 인자를 받지 않는다.
- 접근만 가능하고 해당 클래스나 인스턴스에 영향을 주지 않는다.
- @staticmethod 데코레이터를 붙여 선언

```python
# class_sample.py

class Shop:
    description = 'Python Shop'
    def __init__(self, name, shop_type, address):
        self.name = name
        self.shop_type = shop_type
        self.address = address

# self는 객체자신을 대입한다.('class_practice.py' 함수를 호출하는 형태 참고)
    def show_info(self):
        print('Store info:{}\nStore type:{}\nAddress:{}'.format(self.name, self.shop_type, self.address))

    # shop_type을 변경하는 인스턴스
    def change_type(self, shop_type):
        self.shop_type = shop_type

    # 인스턴스 메서드에 임의로 스태틱 매서드를 지정할 경우
    @staticmethod
    def change_type2(shop, shop_type):
        shop.shop_type = shop_type

    # class method
    @classmethod
    def change_description(cls, description):
        cls.description = description

    # 스태틱 매서드는 인자를 받지 않는다.
    @staticmethod
    def print_hello():
        print('hello')
```

```python
# class_practice.py

# class_sample 파일에서 Shop 클래스를 불러온다.
from class_sample import Shop

# 객체들의 초기값을 설정한다.
lotteria = Shop('롯데리아', '패스트푸드', '서울시 강남구')
burgerking = Shop('버거킹', '햄버거', '서울시 서초구')

# 인스턴스 매소드 호출
lotteria.show_info()
burgerking.show_info()
burgerking.change_type('패스트')
burgerking.show_info()

# 초기값을 변경하는 인스턴스 호출
lotteria.change_type2(lotteria, 'PC방')
lotteria.show_info()

# class method 호출
# class method는 클래스단위이므로 객체를 지정해도 값은 같게 나온다.
print(Shop.description)

# description 값 변경
Shop.change_description('Changed description')
print(Shop.description)

# description 값 변경. 객체를 지정해도 결과는 같다.
lotteria.change_description('Change')
print(lotteria.description)
print(Shop.description)

print(Shop)
```

## 속성 접근 지정자

- public : 외부에서 제한없이 접근, 수정가능 (change_type)
- protected : 외부에서 접근 불가능, 상속받은 클래스에서는 접근 가능 (_change_type)
- private : 내부에서만 접근, 수정 가능 -> 외부 접근 가능하도록 property 사용 (__change_type)

### 캡슐화

- 반드시 알아야 할 부분이나 보여주고 싶은 부분만 보여주고 나머지는 가리는 방식
- 객체의 속성(데이터)과 행위(매소드)를 하나로 묶고,
- 실제 구현 내용 일부를 외부에 감추어 은닉한다.  

- privite 지정자 : 속성 이름 시작을 `__` 로 바꿔준다. 실제 이름은 `_클래스__속성__` (name mangling)
- 상속할(부모) 가능성이 있는 클래스에는 쓰지 않는 것이 좋다. (protected를 사용한다)  

> public : 외부에서제한없이 접근, 수정가능  
> protected : `_매서드` 외부에서접근 불가능, 상속받은 클래스에서는 접근 가능  
> private : `__매서드` 내부에서만 접근, 수정 가능 -> 외부 접근 가능하도록 property 사용  

- 함수, 클래스 이름 바꿀 때 : refactor -> rename (사용된데에 한꺼번에 다 바뀜)
- search fot reference 체크 -> 참조된 곳도 다 바꿈
-



## get/set 프로퍼티

- 타 프로그래밍에서 getter/setter를 파이썬에선 property로 사용한다.
- private으로 정해진 값을 읽어와서 변경해야할때 사용한다.
- 함수 이름이 같아야 한다.
- 함수처럼 사용하지 않고 속성처럼 사용한다.








## 상속 Inheritance

- 어떤 클래스와 비슷한 기능을 수행하지만 약간 추가적인 기능이 필요한 다른 클래스가 필요할 경우 기존 클래스의 상속을 받은 새로운 클래스를 만들 수 있다.
- 상속하는 클래스(부모클래스) - 상속받는 클래스(자식클래스)
- 자식 클래스 정의의 괄호 안에 부모 클래스를 적어준다.

```python
class Child(Parent):
	pass
```



### 매서드 오버라이드 method override


### 부모 클래스의 매서드 호출




## 다형성과 덕타이핑

다형성 - 동일한 실행이지만, 다른 동작을 수행할 수 있도록 허용하는 것.
