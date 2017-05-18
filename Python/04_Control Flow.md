
# if, elif else (조건문)

```python
if 조건1:
	조건1이 참일 경우 수행
elif 조건2:
	조건 1이 거짓, 조건2가 참일 경우 수행
else:
	조건 1와 조건 2가 모두 거짓을 경우 수행
```

### 조건 표현식

```python
>>> print('Good') if is_holiday == True else print('Bad')
>>> print('Good') if is_holiday else print('Bad')		//==True는 생략 가능

>>> print('Good') if vacation >= 7 else print('Normal') if vacation >= 5 else print('Bad')
```

##### 리스트, 딕트 등의 값이 있으면 True, 값이 없으면 False

# for (조건에 따른 순회)

```python
for 항목 in 순회가능(iterable)객체:
   <항목을 사용한 코드>					//들여쓰기 주의
```

```python
>>> champion_list = ['lux', 'ahri', 'ezreal', 'zed']
>>> for champion in champion_list:
...		print(champion)
...
lux
ahri
ezreal
zed
```
- 딕셔너리에서 키나 값을 순회할 때는, iterable한 객체의 위치에 dict.keys()나 dict.values()를 사용한다.
키, 값을 모두 순회할 때에는 dict.items()를 사용한다.

### 중단하기 break

- 데이터를 순회하는 중, 특정 조건에서 순회를 멈추고 반복을 빠져나갈때 사용

```python
>>> for champion in champion_list:
...     print(champion)
...     if champion == 'ahri':
...         break
...
lux
ahri
```

### 건너뛰기 continue

- 데이터를 순회하는 중, 특정 조건에서 반복 내부 코드를 실행하지 않고 다음 반복으로 건너뛸때

```python
>>> for champion in champion_list:
...     if champion == 'ahri':
...         continue
...     print(champion)
...
lux
ezreal
zed
```

### for, else

- else : break가 호출되지 않을때 실행되는 부분

```python
for 항목 in 순회할 객체:
	pass
else:
	break가 한번도 호출되지 않았을 경우의 코드
```

### range 숫자 시퀀스

- 메모리에 개별 값을 저장하지 않음.

```
range(시작, 종료, step)
```

```python
>>> for x in range(0, 10):				/0부터 10개의 숫자 범위
... 	print(x)

0
1
2
3
4
5
6
7
8
9
```

## zip

- 여러 시퀀스를 동시 순회 (적은 수의 시퀀스 데이터 갯수만큼 순회)
- 시퀀스 순회한 결과 값을 저장하고 있지 않음.

```python
>>> fruits = ['apple', 'banana', 'melon']
>>> colors = ['red', 'yellow', 'green', 'purple']
>>> for fruit, color in zip(fruits, colors):
>>> 	print(fruit)
>>> 	print(color)
apple
red
banana
yellow
melon
green
```

### zip은 tuple이나 list로 변경 가능하다.

- list() 함수를 이용하여 zip을 튜플을 값으로 가지는 리스트를 만들 수 있다.
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

# while

조건이 참일경우 반복

```python
>>> while i > 10:
... 	print(i)
...		i += 1
```


# 컴프리헨션 comprehension

리스트보다 빠르다.

```python
[표현식 for 항목 in iterable객체]
```


### while로 리스트를 만드는 경우

```python
>>> a = []
>>> i = 1
>>> while i < 101:
...     a.append(i)
...     i += 1
...
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
```

### for로 리스트를 만드는 경우

```python
>>> a = []
>>> i = 0
>>> for i in range(1, 101):
...     a.append(i)
...
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
```

### 컴프리헨션으로 리스트를 만드는 경우

```python
>>> [a for a in range(1, 101)]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
```

#### item의 값을 2배로 하는 리스트

```python
[item*2 for item in range(10)]
```

#### 1~10까지의 수 중에 짝수만 리스트로 만들기

```python
[item for item in range(10) if item % 2 == 0]
```

### 리스트 컴프리헨션 중첩

```python
>>> fruits = ['apple', 'banana', 'melon']
>>> colors = ['red', 'yellow', 'green', 'purple']
>>> [(color, fruit) for color in colors for fruit in fruits]
[('red', 'apple'), ('red', 'banana'), ('red', 'melon'), ('yellow', 'apple'), ('yellow', 'banana'), ('yellow', 'melon'), ('green', 'apple'), ('green', 'banana'), ('green', 'melon'), ('purple', 'apple'), ('purple', 'banana'), ('purple', 'melon')]
```

### 셋 컴프리헨션 set comprehension

```python
{표현식 for 표현식 in iterable객체}
```

### 제네레이터 컴프리헨션 generator comprehension

```python
(표현식 for 표현식 in interable객체)
```

- `(``)`로 되어 있지만 튜플을 생성하지 않는다. (튜플은 컴프리헨션이 없음)
- 제네레이터 객체는 순회 가능하며, 리스트형태로 만들 수 있다.


##### 실습 5

```python
>>> a = 0
>>> b = 0
>>> l = ['{} * {} = {}'.format(a, b, a*b if b != 9 else '{}\n'.format(a*b)) for a in range(2,10) for b in range(1,10)]
>>> for i in l:
...    print(i)
```

a*b를 문자열 str로 치환할 경우

```python
['{} * {} = {}'.format(a, b, a*b if b != 9 else str(a*b)+'\n') for a in range(1,10) for b in range(1,10)]
```


### 실습 6

```
l2 = [x for x in range(100) if not x % 7 or not x % 9]
```


##### 파이썬 내장 함수

built-in function

sum() 리스트 등을 더해줌.
sum([x for x in range(1000, 2001) if x%2 ==1])

##### 특정 변수 리셋 

del 변수이름





