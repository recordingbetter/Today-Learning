

# 시쿼스 타입

## 리스트

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

### 특정 위치에 리스트 항목 추가

```
>>> fruits.insert(0, 'mango')		//fruits 리스트의 첫번째 공간에 'mango' 데이터를 추가
```


%hist -> 인터프리터에 입력했던 모든 히스토리가 나옴
%reset -> 인터프리터에 입력했던 모든 변수를 초기화



### sort. sorted
sorted(list) -> 리스트 자체를 정렬
l.sort(list) -> 리스트를 정렬한 복사본을 반환


### 

- 리스트는 다른 변수에 대입할 경우, 같은 리스트를 가리키므로 값이 같이 바뀐다.
- list2 = list1.copy() -> list1의 데이터로 list2를 새로 만든다.
- list3 = list1[:] -> list1의 데이터로 list3을 새로 만든다.


## 튜플
- 리스트와 비슷하지만 내부 항목의 삭제나 수정이 불가능하다.
- 요소가 1개일 경우 뒤에 꼭 `,`를 넣어줘야 한다.
- 리스트보다 메모리는 적게 차지한다.

```python
>>> t = (100, 200)
>>> t1, t2 = t
>>> t1
100
>>> t2
200


>>> l=['a', 'b', 'c']
>>> t = tuple(l)
>>> t
('a', 'b', 'c')
>>> t2 = tuple('ABCD')
>>> t2
('A', 'B', 'C', 'D')
```

## 딕셔너리
- 키:값 형태의 데이터 집합
- 각각의 키는 중복되지 않아야 한다.
- 순서가 없다.





### clear 
- 딕셔너리 전체 삭제

### del
- del 딕셔너리[키]

### in 으로 검색
검색어 in 딕셔너리
True/False


### items()
딕셔너리의 모든 값이 리스트 안에 들어있는 튜플 형태로 나옴

### keys()
딕셔너리의 모든 키 값이 리스트로 나옴?


## set
- 순서가 없고 중복된 값을 없애버림
- 딕셔너리를 set으로 바꾸면 키 값만 남는다.

### 셋 생성

### 형변환

### 집합 연산이 가능하다






실습 6
lol = {
     ...:     'champions' : {'lux', 'ahri', 'ezreal'},
     ...:     'items' : [
     ...:         {'Doran Ring':400},
     ...:         {'Doran Blade':450},
     ...:     ]
     ...: }
     
 - 중간에 들어가는 괄호 종류는 상관없음...?



# 제어문

## if, elif else (조건문)


print('Good') if is_holiday == True else print('Bad')
print('Good') if is_holiday else print('Bad')		//==True는 생략 가능

print('Good') if vacation >= 7 else print('Normal') if vacation >= 5 else print('Bad')


리스트, 딕트 등의 값이 있으면 True
값이 없으면 False



## for (조건에 따른 순회)

```python
for 항목 in 순회가능(iterable)객체:
   <항목을 사용한 코드>					//들여쓰기 주의
```



### for, else
- else : break가 호출되지 않을때 실행되는 부분

### range 숫자 시퀀스
- 메모리에 개별 값을 저장하지 않음.

for x in range(0, 10):



### zip
- 여러 시퀀스를 동시 순회
- 시퀀스 순회한 결과 값을 저장하고 있지 않음.

```python
>>> fruits = ['apple', 'banana', 'melon']
>>> colors = ['red', 'yellow', 'green', 'purple']
>>> for fruit, color in zip(fruits, colors):
>>> 	print(fruit)
>>> 	print(color)
```

#### zip은 tuple이나 list로 변경 가능하다.

- 순회 결과값(데이터)을 가지고 있지 않기때문에 1번 변환되면 값이 없어진다.

```python
>>> z = zip(fruits, colors)		//zip
<zip at 0x106305788>
>>> t = tuple(z)					//zip을 tuple로 변경 가능 (한번만 사용가능)
(('apple', 'red'), ('banana', 'yellow'), ('melon', 'green'))

>>> z = zip(fruits, colors)		//zip
>>> l = list(z)					//zip을 list로 변경 가능 (한번만 사용가능)
[('apple', 'red'), ('banana', 'yellow'), ('melon', 'green')]
```

