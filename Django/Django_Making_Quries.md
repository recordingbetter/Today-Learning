# Making Quries

- 데이터 모델을 만들면 Django는 자동으로 객체를 생성, 검색, 업데이트 및 삭제할 수있는 데이터베이스 추상화 API를 제공한다.

### 객체 만들기

- 객체를 생성하려면 모델 클래스에 인자를 전달하여 호출하고 save()를 한다.(insert)
- 데이터베이스에 데이터로 저장된다.

### 객체의 변경 저장

- 이미 존재하는 데이터를 변경하려면 save()를 사용한다.(update)

#### ForeignKeyField, ManyToManyField 저장, 업데이트

- ForeignKey 필드를 업데이트하는 것은 객체 업데이트 방법과 같다. save()
- ManyToMany 필드에서는 add()를 사용해야 하며, 중간 테이블에 레코드를 하나 생성한다. 한꺼번에 여러 인자를 넘길 수 있다.

```
# ForeignKeyField의 저장, 업데이트
>>> from blog.models import Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()


# ManyToManyField 저장, 업데이트
>>> from blog.models import Author
>>> joe = Author.objects.create(name="Joe")
>>> entry.authors.add(joe)
# 중간 테이블에 레코드가 생성됨

# 여러 인자 전달
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
```

### 객체 검색 Retrieving objects

- 검색하기 위해서는 모델의 Manager를 통해 QuerySet을 만든다.
- QuerySet은 데이터베이스 객체의 모음 (SELECT)
- 필터 사용 가능 (WHERE, LIMIT)
- Manager는 모델 클래스를 통해서만 액세스 가능.
- all() 매소드는 오브젝트의 전체 쿼리셋을 반환

### 필터를 사용하는 검색

- filter(**kwargs) : 지정된 매개변수워 일치하는 쿼리셋 반환
- exclude(**kwargs) : 지정된 매개변수에 포함되지 않는 쿼리셋 반환

```python
# pub_date가 2006인 Entry 객체 쿼리셋을 반환
Entry.objects.filter(pub_date__year=2006)
# 아래와 같다
Entry.objects.all().filter(pub_date__year=2006)
```

- 필터는 여러개 연결하여 사용 가능

```
# headline이 'What'으로 시작하고, pub_date가 오늘보다 크지 않고, 2005, 1, 30보다 큰 Entry 쿼리셋 반환
Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime(2005, 1, 30)
```

### 필터를 사용한 쿼리셋은 고유하다.

- QuerySet을 선언할 때마다 이전 QuerySet에 바인딩 된 새로운 QuerySet을 얻게됩니다. 
- 각 상세 검색은 저장되고 사용되며 재사용 될 수있는 별개의 고유 한 QuerySet을 생성합니다.

```
# q2, q3은 q1의 하위 집합
>>> q1 = Entry.objects.filter(headline__startswith="What")
>>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
>>> q3 = q1.filter(pub_date__gte=datetime.date.today())
```

### 사용자가 쿼리셋을 호출할때까지 데이터베이스를 읽지 않음

```
# 3번째만 데이터베이스에서 읽어온다.
# 사용자가 쿼리셋을 호출할때까지 데이터베이스를 읽지 않음.
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)
```

### get() 으로 1개의 데이터를 가지고 올 수 있음

- 지정된 데이터가 없으면 DoesNotExist 예외 발생
- 지정된 데이터가 하나 이상이면 MultipleObjectsReturned 예외 발생

```
>>> one_entry = Entry.objects.get(pk=1)
```

### QuerySet 제한

- Python의 슬라이스를 사용할 수 있다.

```
# 5개
>>> Entry.objects.all()[:5]

# 5번째부터 10번째까지
>>> Entry.objects.all()[5:10]

# 아래는 지원되지 않음
>>> Entry.objects.all()[-1]
```

```
# headline을 알파벳 순으로 정렬 후 첫번째
>>> Entry.objects.order_by('headline')[0]
```

### Field lookups

- SQL의 WHERE
- 기본 형태는 `field__lookuptype=value`

```
>>> Entry.objects.filter(pub_date__lte='2006-01-01')

# 아래 SQL과 같다
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
```

- FK로 연결된 경우, 다른 모델의 필드의 쿼리셋을 가지고 올 수 있다.


|키워드|설명|사용예|
|---|---|---|
|\_\_lt / \_\_gt</br>\_\_lte / \_\_gte|~보다 작다 / ~보다 크다</br>~보다 작거나 같다. ~보다 크거나 같다.|id가 1보다 큰 데이터 검색</br>model1.objects.filter(id\_\_gt=1)|
|\_\_in|주어진 리스트 안에 존재하는 데이터 검색|model1.objects.filter(id\_\_in[2, 3, 5]|
|\_\_year</br>\_\_month</br>\_\_day|해당 년도, 월, 일 검색|model1.objects.filter(published_date\_\_year=2015)|
|\_\_isnull|해당 열의 값이 null인 데이터 검색|model1.objects.filter(name__isnull=True)|
|\_\_contains</br>\_\_icontains|해당 열의 값이 지정한 문자열을 포함하는 데이터 검색</br>\_\_icontains는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_contains='com')|
|\_\_startswith</br>\_\_istartswith|해당 열의 값이 지정한 문자열로 시작하는 데이터 검색</br>\_\_istartswith는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_startswith='com')|
|\_\_endswith</br>\_\_iendswith|해당 열의 값이 지정한 문자열로 끝나는 데이터 검색</br>\_\_iendswith는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_endswith='com')|
|\_\_exact</br>\_\_iexact|해당 열의 값이 지정한 문자과 일치하는 데이터 검색</br>\_\_iexact는 대소문자를 구별하지 않음.|model1.objects.filter(name\_\_exact='com')|
|\_\_range|문자, 숫자, 날짜의 범위를 지정|model1.objects.filter(id\_\_range(2, 10)|

### 관계를 통한 조회

- 두 모델의 관계를 통해 쿼리셋을 가지고 올 수 있다.

```
# Blog 모델의 이름이 Beatles Blog인 데이터과 관계있는 Entry 객체 반환
>>> Entry.objects.filter(blog__name='Beatles Blog')

# Entry의 헤드라인 필드에 'Lennon'이 포함된 데이터과 관계있는 Blog 객체 반환 
>>> Blog.objects.filter(entry__headline__contains='Lennon')
```

- 관계 있는 모델들을 거치면서 하나라도 조건에 맞지 않아면 Null 반환

```
# Entry에 author과 name이 비어있는 Blog과 관계있는 객체 반환
>>> Blog.objects.filter(entry__authors__name__isnull=True)

# Entry에 author에 값이 있고 name이 비어있는 Blog과 관계있는 객체 반환
>>> Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)
```

### 다중 관계

- 단일 filter () 호출 내부의 모든 항목이 동시에 적용되어 모든 요구 사항과 일치하는 항목을 필터링합니다. 
- 연속적인 filter () 호출은 객체 세트를 추가로 제한하지만 다중 값 관계는 이전 filter () 호출로 선택된 객체가 아닌 기본 모델에 링크 된 모든 객체에 적용됩니다.

```
# Entry 모델의 headline 필드에 Lennon을 포함하고, pub_date의 연도가 2008년인 Blog 객체
>>> Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)

>>> Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```

### 필터는 모델을 참조할 수 있다.

- 필드의 값을 같은 모델의 다른 필드와 비교하려면 F() (동일한 인스턴스 비교)

```
# n_pingbacks의 값보다 n_comments의 값이 큰 Entry 객체
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))

# 연산 가능
Entry.objects.filter(n_comments__gt=F('n_pingbacks') * 2)
Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))

# 관계 있는 객체로 확장 가능
Entry.objects.filter(authors__name=F('blog__name'))

# timedelta로 시간 연산 가능
Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))

# .bitand(), .bitor(), .bitrightshift(), .bitleftshift()의 비트 연산 가능
F('somefield').bitand(16)
``` 

### PK 조회 shortcut

- pk는 줄여서 조회 가능하다.

```
# 3개는 모두 값은 값을 반환
>>> Blog.objects.get(id__exact=14)
>>> Blog.objects.get(id=14)
>>> Blog.objects.get(pk=14)

# Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__in=[1,4,7])

# Get all blog entries with id > 14
>>> Blog.objects.filter(pk__gt=14)

# 관계 이용 가능
>>> Entry.objects.filter(blog__id__exact=3)
>>> Entry.objects.filter(blog__id=3)
>>> Entry.objects.filter(blog__pk=3) 
```

### 와일드카드 % LIKE

- iexact, contains, icontains, startswith, istartswith, endswith, iendswith 에서 와일드카드 `%` 사용가능
- `%`는 여러 문자 와일드 카드를 나타내며 `_`는 한 문자 와일드 카드를 나타냅니다.









