
# 리스트 list []

- 순서가 있는 데이터의 집합
- 내부 데이터 변경 가능

### 리스트 생성

```python
>>> list1 = []			//empty list
>>> list2 = list()		//empty list
>>> sample_list = ['a', 'b', 'c', 'd']
>>> sample_list2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
```

### 다른 데이터를 리스트로 변환 list 함수

```python
>>> list('League of legends')			//공백도 리스트에 포함
['L', 'e', 'a', 'g', 'u', 'e', ' ', 'o', 'f', ' ', 'l', 'e', 'g', 'e', 'n', 'd', 's']
>>> 'apple banana melon'.split()		//공백으로 나누어진 리스트 생성
['apple', 'banan', 'melon']
```

### 리스트 항목 변경

```python
>>> list1[2] = 'a'			//list1의 3번째 항목을 a로 변경
```

### 슬라이스 연산

```python
>>> list_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
>>> list_month[:3]			//앞에서부터 3개
>>> list_month[4:6]			//4번째부터 5번째까지
>>> list_month[2:7:3]		//2번째부터 6번째까지 3개씩 건나뛰어서
>>> list_month[-3:]			//뒤에서부터 3개
>>> list_month[::-1]		//역순으로
```

### 리스트 항목 추가 (append)

```python
>>> list1 = ['a', 'b', 'c', 'd']
>>> list1.append('e')
>>> list1
['a', 'b', 'c', 'd', 'e']

# list1에 list2를 추가
>>> list2 = ['f', 'g']
>>> list1.append(list1)
>>> list1
['a', 'b', 'c', 'd', 'e', ['f', 'g']]
```

### 리스트 병합 (extend, +=)

```python
>>> list1 = ['a', 'b', 'c', 'd']
>>> list2 = ['f', 'g']
>>> list1.extend(lsit2)
>>> list1
['a', 'b', 'c', 'd', 'f', 'g']
```

### 특정 위치에 리스트 항목 삭제 del

**del은 리스트 함수가 아닌 파이썬 구문이므로 del 리스트[오프셋] 형태로 사용한다.**

```python
>>> del list1[0]			//리스트의 왼쪽에서 첫번째 데이터를 삭제
```

### 특정 위치에 리스트 항목 삭제 pop

``` python
>>> fruits.pop()					//뒤에서 부터 없어지며 지워지는 데이터를 반환한다.
>>> fruits.pop(-2)				//오른쪽에서 2번째 데이터가 지워지며 지워지는 데이터를 반환
>>> fruits.pop(3)				//왼쪽에서 4번째 데이터가 지워지며 지워지는 데이터를 반환
```

### 값으로 리스트 항목 삭제 remove

```python
>>> list1.remove('b')
```

### 특정 위치에 리스트 항목 추가 insert

```python
>>> fruits.insert(0, 'mango')		//fruits 리스트의 첫번째 공간에 'mango' 데이터를 추가
```

### 값으로 리스트 항목 오프셋 찾기 index

```python
>>> list1.index('c')				//list1의 'c'의 인덱스를 반환
```

### 존재여부 확인 in

```python
>>> 'c' in list1					//True or False인 Bool 값을 반환
True
```

### 값 갯수 세기 count

```python
>>> list2 = ['a', 'a', 'b', 'c', 'd']
>>> list2.count('a')
2
```

### 리스트 정렬 sort. sorted

```python
>>> list1.sort() : 리스트 함수. 리스트 자체를 소트 한다.
>>> sorted(list1) : 파이썬 함수. 리스트는 그래도 두고 복사본을 소트한 후 반환. 튜플이나 딕트에 사용 가능.
```

### 리스트 복사 copy

- 리스트는 다른 변수에 대입할 경우, 같은 리스트를 가리키므로 값이 같이 바뀐다.
- list2 = list1.copy() -> list1의 데이터로 list2를 새로 만든다.
- list3 = list1[:] -> list1의 데이터로 list3을 새로 만든다.


# 튜플 tuple ()

- 리스트와 비슷하지만 내부 항목의 삭제나 수정이 불가능하다.
- 요소가 1개일 경우 뒤에 꼭 `,`를 넣어줘야 한다.
- 리스트보다 메모리는 적게 차지한다.

### 튜플 생성

```python
>>> empty_tuple = ()
>>> 
>>> colors = 'red',			//튜플이 1개의 값만 가지는 경우 뒤에 꼭 ,를 넣어준다.
>>> fruits = 'apple', 'banana'	//()로 묶지 않아도 되지만 구문을 위해 묶어준다.
```

### 튜플 언팩킹

```python
>>> t = (100, 200)
>>> t1, t2 = t
>>> t1
100
>>> t2
200
```

### 튜플 형변환

```python
# 리스트를 튜플로 변환
>>> l=['a', 'b', 'c']
>>> t = tuple(l)
>>> t
('a', 'b', 'c')

# 문자열을 튜플로 변환
>>> t2 = tuple('ABCD')
>>> t2
('A', 'B', 'C', 'D')
```


# 딕셔너리 dictionary {:}

- 키:값 형태의 데이터 집합
- 각각의 키는 중복되지 않아야 한다.
- 순서가 없다.

### 딕셔너리 생성

```python
>>> empty_dict1 = {}
>>> empty_dict2 = dict()

>>> champion_dict = {
... 'Lux': 'the Lady of Luminosity',
... 'Ahri': 'the Nine-Tailed Fox',
... 'Ezreal': 'the Prodigal Explorer',
... 'Teemo': 'the Swift Scout',
... }
```

### 딕셔너리 형변환

- dict 함수로 두 값이 짝지어진 리스트나 튜플을 딕셔너리로 변환한다.

```python
>>> sample = [[1,2], [3,4], [5,6]]
>>> dict(sample)
{1: 2, 3: 4, 5: 6}

>>> sample = ([1,2], [3,4], [5,6])
>>> dict(sample)
{1: 2, 3: 4, 5: 6}
```

### 딕셔너리의 항목 찾기, 추가, 변경

```python
# 키가 'Lux'인 데이터를 반환
>>> champion_dict['Lux']
'the Lady of Luminosity'

# 키가 'Sona', 데이터가 'Maven of the Strings' 값이 추가됨.
>>> champion_dict['Sona'] = 'Maven of the Strings'

# 키가 'Lux'의 값을 'Demacia'로 변경
>>> champion_dict['Lux'] = 'Demacia'
```

### 딕셔너리의 결합

```python
>>> item_dict = {
... "Doran's Ring": 400,
... "Doran's Blade": 450,
... "Doran's Shield": 450,
... }
>>> com_dict = {}						//새로운 딕셔너리를 만들어
>>> com_dict.update(champion_dict)	//champion_dict를 추가하고
>>> com_dict.update(item_dict)		//item_dict를 추가
>>> com_dict
{'Ahri': 'the Nine-Tailed Fox',
 "Doran's Blade": 450,
 "Doran's Ring": 400,
 "Doran's Shield": 450,
 'Ezreal': 'the Prodigal Explorer',
 'Lux': 'Demacia',
 'Sona': 'Maven of the Strings',
 'Teemo': 'the Swift Scout'}
```

- 서로 같은 키가 있을 경우, update에 주어진 딕셔너리(괄호 안의 딕셔너리)의 값이 할당된다.

### 딕셔너리 삭제 del

```python
>>> del com_dict["Doran's Ring"]			//키가 "Doran's Ring"인 데이터 쌍이 삭제됨.
```

### clear 

딕셔너리 전체 삭제

### in 으로 검색

- 검색어 in 딕셔너리
- True/False

### keys()

딕셔너리의 모든 키 값이 리스트로 나옴

```python
>>> com_dict.keys()
dict_keys(['Ezreal', "Doran's Shield", 'Teemo', 'Lux', 'Sona', "Doran's Blade", 'Ahri'])
```

### values()

딕셔너리의 모든 값이 리스트로 나옴

```python
>>> com_dict.values()
dict_values(['the Prodigal Explorer', 450, 'the Swift Scout', 'Demacia', 'Maven of the Strings', 450, 'test'])
```

### items()

딕셔너리의 모든 값이 리스트 안에 들어있는 튜플 형태로 나옴

```python
>>> com_dict.items()
dict_items([('Ezreal', 'the Prodigal Explorer'), ("Doran's Shield", 450), ('Teemo', 'the Swift Scout'), ('Lux', 'Demacia'), ('Sona', 'Maven of the Strings'), ("Doran's Blade", 450), ('Ahri', 'test')])
```

### get()

딕셔너리에 있는 값의 키로 value를 가져옴

```python
>>> com_dict.get('Ezreal')
'the Prodigal Explorer'
```

### copy()

딕셔너리 복사

```python
>>> copy_dict = com_dict.copy()
>>> copy_dict
{'Ahri': 'test',
 "Doran's Blade": 450,
 "Doran's Shield": 450,
 'Ezreal': 'the Prodigal Explorer',
 'Lux': 'Demacia',
 'Sona': 'Maven of the Strings',
 'Teemo': 'the Swift Scout'}
```


# set

- 순서가 없고 중복된 값을 없애버림
- 딕셔너리를 set으로 바꾸면 키 값만 남는다.

### set 생성

```python
>>> empty_set = set()
>>> champions = {'lux', 'ahri', 'ezreal'}
```

### 형변환

- 문자열, 리스트, 튜플, 딕셔너리를 set으로 변환할 수 있다.
- 중복된 값은 사라진다.
- 순서가 없다.

```python
# 문자열 -> 중복된 값은 사라짐
>>> set('Fastcampus')
{'F', 'a', 'c', 'm', 'p', 's', 't', 'u'}

# 딕셔너리 -> set으로 변환하면 key만 남는다.
>>> set(com_dict)
{'Ahri', "Doran's Blade", "Doran's Shield", 'Ezreal', 'Lux', 'Sona', 'Teemo'}
```

### 집합 연산이 가능하다

|연산자|설명|Description|
|---|---|---|
|\\|합집합|Union|
|&|교집합|Intersection|
|-|차집합|Difference|
|^|대칭차집합|Exclusive|
|<=|부분집합|Subset|
|<|진부분집합|Proper subset|
|>=|상위집합|Superset|
|>|진상위집합|Proper superset|




