# Field options

### null

- `null = True`일 경우, 해당 필드에 null을 허용한다.

### blank

- `blank = True`일 경우, 해당 필드에 blank를 허용한다.

### choices

- 실제 데이터 베이스에 저장되는 값과 사용자에게 보여줄 값을 다르게 할 수 있다.

```python
from django.db import models

class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)        
```

### db_column

- 데이터베이스의 컬럼의 이름. 생략되면 필드 이름을 사용한다.
- 파이썬, SQL의 예약어 사용 불가

### db_index

- `db_index = True` 이면 이 필드에 대한 인덱스가 생성됨

### db_tablespace

- 필드 인덱스를 위한 테이블 공간의 이름

### defalut

- 필드의 기본 값. 새로운 객체가 생성될때마다 호출된다.
- 변경 가능한 오브젝트 (모델 인스턴스, 목록, 세트 등) 일 수 없습니다.


### editable

- `editable = False`인 경우, admin이나 다른 ModelForm에서 보이지 않는다.
- 모델 유효성 검사도 지나친다.
- 기본값은 True

### error_messages

- error_messages 인수를 사용하면 필드에서 발생시키는 기본 메시지를 대체 
- 덮어 쓰려는 오류 메시지와 일치하는 키가 있는 딕셔너리를 전달해야 함.

### help_text

- 지정한 도움말이 보이게 한다.
- html 포함 가능하다.

```python
help_text="Please use the following format: <em>YYYY-MM-DD</em>."
```

### primary_key

- `primary_key = True` 일 경우 지정한 필드를 모델의 pk로 만든다.
- 자동으로 정해주는 pk를 사용하지 않을 경우에 사용한다.
- 자동으로 AutoField가 되고 `null=False`, `unique=True`가 적용된다.

### unique

- `unique=True` 일 경우, 해당 필드의 레코드는 유일한 값을 가져야 한다.
- 레코드 저장 시, 유일한 값이 아닐 경우, IntegrityError 발생.

### unique\_for\_date, unique\_for\_month, unique\_for\_year

- DateField, DateTimeField에 날짜가 유일한 값이어야 하는 경우 사용.
- title이라는 필드에 `unique_for_date="pub_date"` 옵션을 주면, 같은 title과 pub_date를 가진 레코드는 생성할 수 없다.

### verbose_name

- 필드에 사람이 읽기 좋은 이름을 붙이고 싶을때 사용.
- verbose_name을 붙이지 않았을 경우, Django는 필드 이름에 언더스코어를 공백으로 바꾸어 자동으로 생성한다.

### validators

- 해당 필드의 유효성 검사를 위한 검사기 리스트


# Field Types

### AutoField

- 숫자가 자동으로 늘어나는 정수필드. primary key

### BigAutoField

- 숫자가 자동으로 늘어나는 64bit 정수필드.

### IntegerField

- 정수인 숫자 필드
- -2147483648 ~ 2147483647
- `localize = False`일때 default form widget은 NumberInput, 아닐땐 TextInput

### BigIntegerField

- 큰 정수를 입력하기 위한 64bit 정수 필드
- default form widget은 TextInput 

### SmallIntegerField

- 적은 정수 필드
- -32768 ~ 32767

### PositiveIntegerField

- 양의 정수 필드
- 0 ~ 2147483647

### PositiveSmallIntegerField

- 양의 정수 필드 (적은 숫자)
- 0 ~ 32767

### DecimalField(max_digits=None, decimal_places=None, **options)

- 고정 소숫점 숫자를 위한 필드.
- Decimal 인스턴스
- DecimalField.max_digits : 허용하는 최대 자릿수(소숫점 포함)
- DecimalField.decimal_places : 소숫점 자릿수
- `localize = False`일때 default form widget은 NumberInput, 아닐땐 TextInput

### FloatField

- 부동소숫점 숫자 필드
- `localize = False`일때 default form widget은 NumberInput, 아닐땐 TextInput

### CommaSeparatedIntegerField(max_length=None, **options)

- `,`로 나누어진 숫자 필드.
- max_length를 정해줘야 한다.

### BinaryField

- 이진데이터 필드.
- ModelForm에 포함시킬 수 없음. 파일 저장을 위한 필드가 아님

### BooleanField

- True/False 필드.
- null을 허용하지 않음.
- default form widget은 CheckboxInput

### NullBooleanField

- True/False 필드.
- null을 허용하지 않음.

### CharField

- 문자열 필드
- max_length를 정해줘야 한다.
- default form widget은 TextInput
- 긴 문자열은 TextField를 사용해야한다.

### TextField(max_length=None, **options)

- 큰 문자열 필드
- default form widget은 Textarea

### SlugField(max_length=50, **options)

- 문자, 숫자, 언더스코어와 하이픈으로 이루어진 짥은 레이블
- 주로 url에 사용한다.
- `allow_unicode = True` 일때 유니코드 문자도 사용 가능

### DateField(auto_now=False, auto\_now\_add=False, **options)

- 날짜 필드.
- datetime.date의 인스턴스
- auto_now : 필드의 데이터가 저장(save)될때마다 오늘 날짜를 기록. (최종 수정날짜) QuerySet.update()은 오늘 날짜를 기록하지 않음.
- auto\_now\_add : 레코드가 처음 기록될때 오늘 날짜를 기록한다. (생성 날짜) 데이터를 바꿀 수 없음.
- default form widget은 TextInput

### TimeField(auto_now=False, auto_now_add=False, **options)

- 시간 필드
- datetime.time의 인스턴스
- DateField와 동일하다.

### DateTimeField(auto_now=False, auto\_now\_add=False, **options)

- 타임스탬프 필드
- datetime.datetime의 인스턴스
- DateField와 동일하다.

### DurationField

- 데이터 저장 주기 필드

### EmailField(max_length=254, **options)

- 데이터 입력 형태가 email 형태인지 검사해주는 CharField

### ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)

- 이미지를 위한 FileField
- 가로, 세로 옵션이 필요하다.
- default form widget은 ClearableFileInput

### GenericIPAddressField(protocol=’both’, unpack_ipv4=False, **options)

- IPv4 또느 IPv6의 입력을 위한 필드

### UUIDField

- universally unique identifier 필드
- pk 처럼 사용할 수 있다.

```python
import uuid
from django.db import models

class MyUUIDModel(models.Model):
	# UUID 인스턴스가 아니라 호출 가능 객체 (괄호 생략)가 기본값으로 전달
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

# 관계 필드

### ForeignKey(othermodel, on_delete, **options)

- 일대다 관계에서 자식필드가 부모 필드의 PK값을 가지는 필드
- ricursive 관계에서는 `models.ForeignKey('self', on_delete=models.CASCADE)` 사용.
- models.py 파일의 코드에서 부모 모델이 자식의 아래쪽에 올때에는 부모클래스를 따옴표로 묶인 문자열로 정의한다.





### ManyToMany(othermodel, **options)

- 다대다 관계에서 상대 모델을 표시
- 중간 테이블을 생성한다.





### OneToOne(othermodel, on_delete, parent_link=False, **options)

- 일대일 관계. ForeignKey와 비슷하지만 관계를 반대로 봤을때 1개의 객체만 반환한다.
- 어떤 모델을 확장할때 유용하다.


