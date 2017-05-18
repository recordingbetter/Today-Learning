



# 함수

### 함수의 정의, 실행

```python
# 문자열 'call func'를 출력하는 함수 정의
>>> def func():
...    print('call func')
...

# 함수 자체는 function 객체를 참조하는 변수
>>> func
<functoin func at 메모리주소>

# 함수를 실행시키기 위해 ()사용
>>> func()
call func
```

### 리턴값이 있는 함수의 정의

```python
>>> def return_true():
...    return True
...
>>> True
```

- 함수 결과로 bool 값을 갖는 데이터를 리턴하여 조건문에 사용 가능하다.

### 매개변수값

```python
>>> def print_arg(something):
...		print(something)

>>> print_arg('ABC')
ABC
```

### 매개변수(parameter)와 인자(argument)의 차이

```python
# 함수를 정의할때에는 매개변수
>>> def func(매개변수1, 매개변수2):

# 함수 호출 시에는 인자 (전달되는 값)
>>> func(인자1, 인자 2)
```




### 리턴값이 없는 함수

- 함수에서 return 하는 값이 없을 경우 `None` 객체를 얻는다.
- `None`는 True나 False가 아니다. 그냥 없는 값.

### 위치 인자 (positional argument)

- 매개변수의 순서대로 인자를 전달

```python
>>> def student(name, age, gender):
...   return {'name': name, 'age': age, 'gender': gender}
... 
>>> student('hanyeong.lee', 30, 'male')
{'name': 'hanyeong.lee', 'age': 30, 'gender': 'male'}
```

### 키워드 인자 (keyword argument)

- 매개변수의 이름을 지정하여 인자로 전달

```python
>>> student(age=30, name='hanyeong.lee', gender='male')
{'name': 'hanyeong.lee', 'age': 30, 'gender': 'male'}
```

### 기본 매개변수값 지정

- 인자가 제공되지 않을 경우, 기본 매개변수로 사용할 값을 지정할 수 있다.

```python
# 함수 student는 위치 매개변수 3개, 키워드 매개변수 1개를 가지며
>>> def student(name, age, gender, cls='WPS'):
...   return {'name': name, 'age': age, 'gender': gender, 'class': cls}
... 
# 호출 시 인자가 주어지지 않았을때 매개변수에 정의된 기본 값을 가진다.
>>> student('hanyeong.lee', 30, 'male')
{'name': 'hanyeong.lee', 'age': 30, 'gender': 'male', 'class': 'WPS'}
```

### 기본 매개변수값의 정의 시점

- 기본 매개변수값은 함수가 정의되는 시점에 한번 계산되어 계속 그 값이 사용된다.

```python
# 함수를 정의할때 result를 빈리스트로 정의한다.
>>> def return_list(value, result=[]):
...   result.append(value)
...   return result
... 
# 함수를 호출할때마다 result 리스트에 값이 누적된다.
>>> return_list('apple')
['apple']
>>> return_list('banana')
['apple', 'banana']


# 함수를 정의할때 result를 None으로 정의한다.
>>> def return_list(value, result=None):
		# 매개변수 result의 값이 없을때만 빈 리스트를 생성한다.
...   if result is None:
...     result = []
...   result.append(value)
...   return result
... 
# 함수를 여러번 호출해도 result 리스트의 값이 누적되지 않음.
>>> return_list('apple')
['apple']
>>> return_list('banana')
['banana']
```

### 위치인자 묶음 *args

- 함수에 위치인자로 주어진 변수들의 묶음
- 관용적으로 `*args`를 사용한다.

```python
>>> def print_args(*args):
...		print(args)
```

### 키워드인자 묶음 **kwargs

- 함수에 키워드인자로 주어진 변수들의 묶음.
- 관용적으로 `**kwargs`를 사용한다.

```python
>>> def print_kwargs(**kwargs):
... 	print(kwargs)
```

### docstring

- 함수를 정의한 문서 역할을 한다.
- 함수 정의 후, 문자열로 시작하며, 여러줄 작성 가능

```python
>>> def print_args(*args):
...   'Print positional arguments'
...   print(args)
... 
>>> help(print_args)
```

### 함수를 인자로 전달

- 파이썬에서는 함수 역시 다른 객체와 동등하게 취급되므로, 함수에서 인자로 함수를 전달, 실행, 리턴하는 형태로 프로그래밍이 가능하다.


```python
# 42를 출력하는 함수
def answer():
    print(42)

# 다른 함수를 매개변수로 받아서 그 함수를 호출하는 함수
def run_something(func):
    func()

# 매개변수로 answer함수를 받아 42를 출력한다.
run_something(answer)

# 2개의 매개변수를 받아 합을 출력하는 함수
def add_args(arg1, arg2):
    print(arg1 + arg2)

# 다른 함수 1개와 매개변수 2개를 받아 그 함수에 매개변수를 넣어 출력한다.
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

# 매개변수 5, 9를 함수 add_args에 대입한다.
run_something_with_args(add_args, 5, 9)

# 위치인자로 주어진 모든 변수들의 합을 구하여 리턴하는 함수
def sum_args(*args):
    return sum(args)

# 다른 함수와 위치인자 여러개를 매개변수로 받아 그 함수에 매개변수들을 대입한 값을 이턴하는 함수
def run_with_positional_args(func, *args):
    return func(*args)

# 리턴된 값은 10, 함수 내부에 print 구문이 없어 출력은 하지 않는다.
run_with_positional_args(sum_args, 1, 2, 3, 4)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))
```

### 함수 안에 함수

- 함수 안에서 또 다른 함수를 정의해 사용할 수 있다.

```python
# 1. 숫자 1개를 입력받아 해당하는 숫자 단수의 (x, y, z)형 튜플의 리스트로 곱할 수 1, 2와 결과를 저장하는 함수 make_gugu(num) 작성
# ex) make_gugu(3) -> return [(3, 1, 3), (3, 2, 6), ....(3, 9, 27)]

# 2. 매개변수 print_type과 gugu_list를 가지며 print_type에 따라 gugu_list를 단순출력 또는 '{} x {} = {}'형으로 출력해주는 함수 print_gugu(print_type, gugu_list) 작성
# ex) print_gugu('simple', <어떤리스트>) -> print((3, 1, 3), (3, 2, 6)...)
# print_type은 'simple'과 'normal'로 나눠지며, simple은 튜플을 그냥 출력, normal은 위의 format string 형태로 출력

# 3. 매개변수 range, print_type, make_gugu_function, print_gugu_function을 가지고 range에 해당하는 볌위의 구구단을 생성하고 출력하는 gugu함수 작성
# gugu함수에서는 매 단마다 줄바꿈 및 이번이 몇 단인지 알려주는 문자열 출력

# _function으로 끝나는 매개변수는 함수 자체를 전달
# ex) gugu(range(3, 7), 'normal', make_gugu, print_gugu)
# ===== 3단 =====
# 3 x 1 = 3
# ...
#
# ===== 6단 =====
# 6 x 1 = 6
# ...

def make_gugu(num):
    return [(num, y, num * y) for y in range(1, 10)]

#result = make_gugu(3)
#print(result)

'''
def print_gugu(print_type, gugu_list):
    if print_type == 'simple':
        for item in gugu_list:
            print(item)
    elif print_type == 'normal':
        for x, y, z in gugu_list:
            print('{} x {} = {}'.format(x, y, z))
'''

def print_gugu(print_type, gugu_list):
    def print_gugu_simple():
        for item in gugu_list:
            print(item)

    def print_gugu_normal():
        for x, y, z in gugu_list:
            print('{} x {} = {}'.format(x, y, z))

    if print_type == 'simple':
        print_gugu_simple()

    if print_type == 'normal':
        print_gugu_normal()



#g_list = make_gugu(3)
#print_gugu('simple', g_list)

def gugu(range_, print_type, make_gugu_function, print_gugu_function):
    # range_변수에는 iterable한 range형 객체가 주어졌다고 가정
    for num in range_:
        print('{val:=^10s}'.format(val=' '+ str(num) + '단'))
        # make_gugu_function을 이용해 (x, y, x*y)형태의 원소를 갖는 리스트를 생성
        cur_gugu_list = make_gugu_function(num)
        # 생성한 리스트를 인자로 전달해 출력
        print_gugu_function(print_type, cur_gugu_list)

        print(' ')

gugu(range(2, 4), 'normal', make_gugu, print_gugu)
```

### 스코프 (영역)

- 각 함수마다 영역을 가진다.
- 동작하는 프로그램의 최 상위 위치는 Global Scope(전역)라고 하며, 
- 전역 스코프 내부에 독립적인 영역을 가지는 경우 Local Scope라고 한다.
