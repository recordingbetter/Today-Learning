### Models


        
        
- 데이터베이스 테이블 설정
- 1개의 클래스는 1개의 데이터베이스 테이블
- 각 모델은 파이썬의 클래스이며 django.db.models.Model의 서브클래스
- 모델의 각 속성은 데이터베이스의 필드
- Django는 database-access API를 자동으로 만들어준다.  


        
        
```python
# models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# 실제 데이터베이스 명령어
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);

```
        
        
        
Person이라는 테이블에 문자열 필드인 first_name, last_name 필드를 만든다.
id라는 primary key 필드는 자동으로 생성된다.  


        
    

        
### model 사용하기


        
        
- settings.py 파일의 INSTALLED_APPS에 사용할 app을 설정해준다.  


        
        
```python
INSTALLED_APPS = (
    #...
    'myapp',
    #...
)

```
        
        
        
- 이후 터미널에서 ./manage.py migrate 를 실행하여 데이터베이스를 생성한다.
- models.py가 변경되었을 경우, 터미널에서 ./manage.py makemigrations를 실행하여 model의 변경사항을 기록한 뒤, migrate를 샐행하여 데이터베이스에 적용한다.  


        
    

        
### Field types


        
        
- 필드는 모델 클래스의 인스턴스로 표기된다.
- 데이터베이스의 컬럼
  


        
        
```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

```
        
        
        
#### 필드의 종류

- BooleanField : True / False
- NullBooleanField : True / False / null
- CharField : 문자열 필드. 항상 max_length 옵션을 줘야한다. 200자 이하.
- TextField : 문자열 필드. 많은 문자 입력 가능
- DateField : 날짜 필드.
- DateTimeField : 타임스탬프 필드. 
- IntegerField : 정수 필드
- FloatField : 실수 필드
- 이 외에도 많음. custom field 생성 가능..  


        
    

        
### Field options


        
        
- 각 필드에 옵션 설정 가능.
- 필드 타입에 따라 사용 가능한 옵션이 정해져 있음.
  


        
        
        
        
#### 공통 옵션

- null : true (null 허용) / false (허용 안함)
- blank : true (비어있는 값 허용) / false (허용 안함)
- choices : 실제 저장될 값과 화면에 보여질 값이 다를때 사용. 2중 튜플이나 리스트이어야 한다.
- default : 필드의 기본값 정의. 함수를 지정할 수 있다.
- help_text : 폼 위젯으로 표시될때 함께 표시될 도움말
- primary_key : true -> 해당 필드를 pk 필드로 지정 (자동으로 생성된 pk외에 추가로 생성됨)
- unique : 해당 필드에는 고유한 값만 허용  


        
    

        
### Automatic primary key fields


        
        
- 각 테이블 별로 id 필드를 자동 생성한다. (Primary Key)  


        
        
```python
id = models.AutoField(primary_key=True)

```
        
        
        
- 자동증가(auto increment)하는 primary key 필드.
- 모델의 필드 중에 primary_key=True 옵션이 명시적으로 선언된 필드가 있다면 자동적으로 id 필드를 생성하지 않음.  


        
    

        
### Verbose field names


        
        
- 모델에서 verbose field name은 읽기좋은 형태의 필드이름.
- 필드들은 공통적으로 첫번째 인자(optional)로 verbose name 값을 가진다.(ForeignKey, ManyToManyField, OneToOneField 는 키워드 인자로 전달))
- 값이 주어지지 않는 경우 해당 필드의 어트리뷰트 이름을 verbose name으로 사용
- 언더스코어 `_`는 공백으로 치환된다.
- 소문자로...  


        
        
```python
# verbose name 'person's first name'
first_name = models.CharField("person's first name", max_length=30)

# verbose name 'first name'
first_name = models.CharField(max_length=30)

# 관계용 필드는 키워드 인자로 전달
poll = models.ForeignKey(Poll, verbose_name="the related poll")
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(Place, verbose_name="related place")

```
        
        
    

        
### 관계 - many to one / one to many?


        
        
- 자식이 될 모델 클래스에 django.db.models.ForeignKey 클래스를 이용하여 선언 (부모 모델 클래스를 인자로)  


        
        
```python
from django.db import models

# 부모 모델
class Manufacturer(models.Model):
    ...
    pass

# 자식 모델
class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    ...

# 재귀형태 (클래스 이름을 문자열로)
class Employee(models.Model):
    boss = models.ForeignKey('Employee')

```
        
        
    

        
### 관계 - many to many


        
        
- 다대다 관계는 ManyToManyField.
- 관계를 가지는 모델 클래스를 첫번째 인자로 받음.
- 관계를 가지는 두 모델 클래스 중 1개에만 설정하면 된다.
- 재귀형태 가능. 클래스 이름을 문자열로 전달.  


        
        
```python
# 피자에는 여러가지 토핑이 올라가며, 토핑은 여러 피자에 사용된다.
from django.db import models

class Topping(models.Model):
    ...
    pass

class Pizza(models.Model):
    ...
    toppings = models.ManyToManyField(Topping)

```
        
        
    

        
### 관계 - many to many 추가 필드


        
        
- 다대다 관계를 가지는 두 모델 클래스에 관계와 관련한 추가 데이터 저장이 필요한 경우 중간 모델을 만든다.
- 중간 모델은 원본 모델 클래스의 ForeignKey를 1개만 가지고 있어야 한다.
- ManyToManyField에 through_fields 옵션으로 관계에 사용되는 클래스이름을 정해주면 ForeignKey 2개를 가질 수 있음.
- 재귀형태일 경우, 중간 모델에 동일한 원본 모델의 ForeignField 2개를 선언할 수 있다.
- 3개 이상일 경우는 through_fields 옵션으로 설정
- 중간모델의 데이터를 생성하는 경우 중간모델에서 직접 생성
  


        
        
```python
# 학생은 여러 동아리에 가입할 수 있고, 각 동아리는 여러명의 학생들을 회원으로 갖습니다. 
# 동아리에 가입한 날짜를 저장.

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


# 중간 모델에서 clear() 사용 가능, remove() 사용 불가
>>> # Beatles have broken up
>>> beatles.members.clear()
>>> # Note that this deletes the intermediate model instances
>>> Membership.objects.all()
[]


# Paul로 시작하는 멤버가 속한 그룹
>>> Group.objects.filter(members__name__startswith='Paul')
[<Group: The Beatles>]


# 특정 날짜 이후 합류 필터(중간 모델 데이터)
>>> Person.objects.filter(
...     group__name='The Beatles',
...     membership__date_joined__gt=date(1961,1,1))
[<Person: Ringo Starr]


# 중간 모델 쿼리
>>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'


# 한쪽 객체로 부터 역참조
>>> ringos_membership = ringo.membership_set.get(group=beatles)
>>> ringos_membership.date_joined
datetime.date(1962, 8, 16)
>>> ringos_membership.invite_reason
'Needed a new drummer.'

```
        
        
    

        
### 관계 - one to one


        
        
- 일대일 관계 정의시 OneToOneField
- 어떤 모델을 확장하여 새로운 모델을 만들 경우 사용.
- OneToOneField 필드는 parent_link 라는 옵션을 제공. True 일때 부모 모델 클래스를 상속받는다.
-  primary_key=True 로 지정하여 Primary Key로 만들 수 있다.
- 하나의 모델이 여러개의 OneToOneField를 가질 수 있다.  


        
        
        
    

        
### 다른 앱의 모델과의 관계


        
        
- 다른 앱에서 선언된 모델과 관계를 가질 수 있다.
- 다른 앱의 모델을 import하여 선언  


        
        
```python
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    # ...
    zip_code = models.ForeignKey(ZipCode)

```
        
        
    

        
### 필드 이름 규정


        
        
- 파이썬 예약어는 필드 이름으로 사용할 수 없다.
- 언더스코어 2개 (\_\_)를 연속으로 사용할 수 없다. (파이썬의 매직매소드) db_column 옵션을 사용
- SQL 예약어는 필드이름으로 사용 가능.  


        
        
        
    

        
### Meta options


        
        
- 모델클래스 내부에 Meta 라는 이름의 클래스 선언해서 모델에 메타데이터를 추가할 수 있다.
- 모델 단위의 옵션 (정렬, 테이블 이름, 닉네임, 복수 표현(verbose_name, verbose_name_plural) 등..)  


        
        
```python
from django.db import models

class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"

```
        
        
    

        
### Model attributes - objects


        
        
- 모델 클래스에서 가장 중요한 속성은 Manager.
- Manager 객체는 모델 클래스 선언을 기반으로 실제 데이터베이스에 대한 쿼리 인터페이스를 제공하며, 데이터베이스 레코드를 모델 객체로 인스턴스화 하는데 사용.
- Manager를 할당하지 않으면 Django는 Default Manager 객체를 클래스 어트리뷰트로 자동 할당. (objects)
- Manager는 모델 클래스를 통해 접근할 수 있으며, 모델 인스턴스(객체)를 통해서는 접근 할 수 없습니다.   


        
        
        
    

        
### Model methods


        
        
- 레코드 단위의 기능 구현 : 모델 클래스의 메서드
- 테이블 단위의 기능 구현 : Manager에서 구현
  


        
        
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

  # Person 객체의 특정 값의 범위에 따라 다른 값을 반환하는 커스텀 메서드
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

   #  Person 객체의 full name을 반환하는 커스텀 메서드
    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

```
        
        
    

        
### Override predefined model methods


        
        
- 모델 클래스에 자동으로 주어지는 메서드들을 필요한 기능으로 override 할 수 있다.
- `__str__()` : 클래스가 출력되면 필요한 데이터가 나올 수 있게 한다.
- `get_absolute_url()` : 해당 모델 객체의 URL을 계산한다. 모델 객체를 url로 표현하는 경우 사용. 모델 객체가 유일한 URL을 가지는 경우에 이 메서드를 구현해주어야 한다.
  


        
        
```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    
   # 저장 시, 특정한 동작을 수행하기 위해 save()를 재정의
    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        do_something_else()


   # 또는, save()를 실행해도 저장이 되지 않게 함.
    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.

```
        
        
        
- 부모클래스의 메서드를 호출해야한다. 위 예제 코드에서 super(Blog, self).save(*args, **kwargs) 를 호출함으로써, 실제로 데이터베이스에 객체가 저장되었습니다. 부모 클래스의 메서드를 호출해주지 않는다면, 실제 데이터베이스에는 아무런 동작도 일어나지 않습니다.
- 오버라이드한 메서드의 인자를 그대로 부모 클래스의 메서드에 넘겨주어야 한다.(*args, **kwargs)  
  
- 재정의된 모델 메서드는 벌크 조작(여러 개체를 한꺼번에 다룰때)시 호출되지 않는다.
- delete는 "pre_delete", "post_delete" 시그널을 이용해야 한다.
- 생성이나 수정은 오버라이드된 메서드 실행 불가능.
  


        
    

        
### Model inheritance - 모델 상속


        
        
- 파이썬의 클래스 상속과 거의 동일하다.
- 베이스 클래스는 django.db.models.Model을 상속받았어야 한다.

#### 모델 클래스 상속 스타일 3가지

1. abstract class
- 부모클래스는 실제로 데이터베이스 테이블을 만들지 않고, 자식 클래스에 필드 선언, 메서드 선언 만 상속해준다.
- 상속 받은 자식 모델은 데이터베이스 테이블에 부모 클래스와 자기 자신에 선언된 필드들을 가진다.
  
2. Multi-table inheritance
- (다른 앱에서 사용중인) 다른 모델 클래스를 상속
- 부모 모델은 자신의 데이터베이스 테이블을 가지며 자식 모델과는 별개로 독립적으로 사용 가능

3. Proxy models
- 모델의 필드 선언은 전혀 변경하지 않고 파이썬 레벨의 코드만 수정하고자 하는 경우 사용  


        
        
        
    

        
### 모델 상속 1. Abstract base classes


        
        
- 여러개의 모델 클래스가 공통적인 정보를 가지게 하고 싶은 경우.
- Meta 클래스에 `abstract = True` 옵션을 주면 추상클래스가 된다.(데이터베이스를 생성하지 않음)
- 자식 클래스들만 이 클래스에 정의된 필드들을 가지는 데이터베이스를 생성한다.(자식 자신이 가진 필드 포함)
- 추상클래스(부모), 자식 클래스 간 동일한 이름의 필드가 있으면 에러.
- 추상클래스는 테이블을 만들지 않고, Manager도 없고 인스턴스화도 할 수 없다.
  


        
        
```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

```
        
        
        
- Student 모델은 3개의 필드(name, age, home_group)를 가진다.

  


        
    

        
### 모델 상속 1-1. Meta inheritance


        
        
- 자식 클래스가 Meta 클래스를 가지지 않는 경우, 부모의 Meta 클래스를 상속받는다.
- 부모 클래스에 선언된 Meta 클래스로부터 상속 받으면 된다.  


        
        
```python
from django.db import models

class CommonInfo(models.Model):
    ...
# 부모클래스는 추상클래스
    class Meta:
        abstract = True
        ordering = ['name']

# 부모 클래스를 상속
class Student(CommonInfo):
    ...
    # 부모의 Meta 클래스를 상속
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'

```
        
        
        
- 자식에게 상속된 Meta 클래스는 `abstract = False`로 변경됨.
- 자식도 추상 클래스가 되길 원하면 `abstract = True`로 다시 선언하면 됨.
- 추상 클래스의 Meta 옵션은 사용상 주의해야할 옵션들이 있다.  


        
    

        
### 모델 상속 1-2. Be careful with related_name


        
        
- 관계에 이름을 부여할 수 있다. (related_name)
- 관계를 가지는 테이블 별로 다른 related_name을 가져야 한다.
- 추상클래스의 관계 필드에 related_name이 지정되었을 경우, 자식 클래스들이 같은 related_name을 가질 수 있다.
- '%(class)s' 는 자식 클래스의 소문자화된 이름으로 치환.
- '%(app_label)s'는 자식 클래스가 선언된 앱의 소문자 이름.  


        
        
```python
# common/models.py

from django.db import models

class Base(models.Model):
    m2m = models.ManyToManyField(OtherModel, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True

# related_name = 'common_childa_related'
class ChildA(Base):
    pass

# related_name = 'common_childb_related'
class ChildB(Base):
    pass



# rare/models.py:

from common.models import Base

# related_name = 'rare_childb_related'
class ChildB(Base):
    pass

```
        
        
    

        
### 모델 상속 2. Multi-table inheritance


        
        
- 부모 모델이든 자식 모델이든 모두 각자의 데이터베이스 테이블을 가진다.
- 공통 필드는 부모 모델 클래스에서 설정, 데이터도 부모에 저장.
- 자식 모델의 데이터는 자식 모델 테이블에 저장. (부모에 대한 링크(OneToOne)를 가진다.)
- OneToOneField를 직접 지정하고 싶다면, OneToOneField 를 추가하고 필드 옵션에 parent_link=True로 설정해주면 된다.  


        
        
```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

# Place를 상속받았으므로 부모테이블의 name, address 필드도 사용 가능.
class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

```
        
        
        
- 자식 모델 클래스를 통해 부모 모델에 접근 가능하다.

```python
>>> p = Place.objects.get(id=12)
# If p is a Restaurant object, this will give the child class:
>>> p.restaurant
<Restaurant: ...>

# If p in not a Restaurant object, 
>>> p.restaurant  # Restaurant.DoesNowExist 예외 발생
```
- 자동으로 제공되는 restaurant 어트리뷰트를 통해 Restaurant 객체에 접근 할 수도 있는데 이때, 어트리뷰트 이름은 자식 클래스의 이름을 소문자화한 이름  


        
    

        
### 모델 상속 2-1. Meta and multi-table inheritance


        
        
- multi-table 상속의 경우 기본적으로 자식모델은 부모모델의 Meta 클래스를 상속받지 않는다. (각각의 테이블을 가지기 때문)
- 자식모델에 ordering, get_latest_by 옵션이 지정되지 않은 경우에 한해, 부모 모델의 해당 설정값을 상속받는다.
  


        
        
```python
class ChildModel(ParentModel):
    ...
    class Meta:
        # 부모 모델 클래스의 ordering 옵션을 무효화 한다.
        ordering = []

```
        
        
    

        
### 모델 상속 2-2. Inheritance and reverse relations


        
        
- 상속받는 모델 클래스와 ManyToMany 관계를 가지려면 related_name을 설정해준다.  


        
        
```python
class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

```
        
        
    

        
### 모델 상속 3. Proxy models


        
        
- 테이블을 가지고 있는 부모 모델 클래스는 상속받되 자식 모델은 테이블을 만들 필요가 없는 경우
- proxy 모델(자식 모델)을 이용해서 부모 모델의 객체를 만들고 수정, 삭제...(부모 테이블 상에서)
- 부모(원본)모델의 설정 변경없이 proxy(자식)모델에서 설정 변경 가능
- 자식 모델의 Meta 클래스에 `proxy=True` 로 선언


        
        
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# Person 클래스를 상속받는 클래스의 Meta 클래스에 proxy = True 선언 --> proxy model이 된다.
class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        ...
        pass


# Person 테이블에 추가된 레코드를 MyPerson 클래스로 조회 가능
>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>


# 기본 옵션 재정의 가능(정렬 등..)
class OrderedPerson(Person):
    class Meta:
        ordering = ["last_name"]
        proxy = True

```
        
        
        
- 어떤 모델 클래스로 쿼리 했는지에 따라 객체의 타입이 결정된다. proxy model의 속성들은 부모 모델이 영향을 주지 않음.
- proxy 모델은 추상클래스가 아닌 하나의 모델만 상속받을 수 있다.(Meta 옵션 상속받음)
- 추상클래스를 상속받을 경우 그 추상클래스가 필드를 가지지 않아야 하며. 이 경우 몇개든 상속 가능.
  


        
    

        
### 모델 상속 3-1. Proxy models manager


        
        
- proxy 모델에 manager를 지정하지 않은 경우 부모의 manager를 상속받는다.
  


        
        
```python
# 기본 manager 변경 방법
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class NewManager(models.Manager):
    ...
    pass

# Person을 상속받지만 새로운 매니저 지정
class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

```
        
        
        

# 부모의 클래스의 manager를 상속받되, 새로운 manager를 추가하려면 추상클래스에 새로운 manager를 선언하고 그 클래스를 상속받는다.

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

# NewManager가 될 새로운 추상클래스 선언
class ExtraManagers(models.Model):
    secondary = NewManager()

    class Meta:
        abstract = True

class MyPerson(Person, ExtraManagers):
    class Meta:
        proxy = True
```  


        
    

        
### 모델 상속 3-2. Differences between proxy inheritance and unmanaged models


        
        
#### unmanaged model

- 자동으로 테이블을 생성하지 않게 `managed=False`옵션을 준 모델은 proxy 클래스와는 다르다.
- 원본테이블이 변경될 때마다 데이터베이스 테이블을 직접 생성, 수정해야한다.
- 원본 모델의 manager와 상관없음. 자체 모델의 manager 선언을 따름.


#### proxy model

- 원본 모델이 변경되어도 수정할 필요 없다.
- 원본 모델의 디폴트 manager를 포함한 모든 manager를 상속받는다.  


        
        
        
        
#### 두가지 옵션의 사용

- 만약에 당신이 이미 존재하는 모델이나 데이터베이스 테이블을 참조하되, 원본 테이블의 모든 컬럼이 필요하지 않다면, Meta.managed=False 옵션을 사용하세요. Django에 의해 제어되지 않는 데이터베이스 뷰나 테이블을 사용하는 경우에 유용합니다.

- 만약에 기존 모델의 파이썬 코드들을 오버라이드 하되, 원본 모델과 동일한 필드를 가지도록 하고 싶다면 Meta.proxy=True 옵션을 사용하세요.  


        
    

        
### 모델 상속 3-3. 다중 상속 Multiple Inheritance


        
        
- 파이썬의 `name resolution rules`이 적용된다.
- 부모가 여럿일때 첫번째 부모의 Meta 클래스를 상속받는다.
  