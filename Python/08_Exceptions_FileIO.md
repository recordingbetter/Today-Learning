# 예외 처리

- 에러가 났을때 프로그램이 종료된다는 등의 원치 않는 상황을 피하기 위해 사용한다.

```python
try:
	시도할 코드
	
except:
	에러가 발생했을때 실행할 코드
	
else:
	에러가 발생하지 않았을때 실행할 코드
```

##### 여러가지 에러를 구분할 경우

```python
try:
	시도할 코드

except <예외클래스1>:
	<예외클래스1> 경우에 실행할 코드
	
except <예외클래스2>:
	<예외클래스2> 경우에 실행할 코드
	
except <예외클래스3>:
	<예외클래스3> 경우에 실행할 코드
...
else:
	에러가 발생하지 않았을때 실행할 코드
```

##### 예외사항을 변수로 사용할 경우

```pyhton
import random


l = random.sample(range(10), 10)
dic = {'apple': 'red'}


try:
    print(l[20])
    print(dic['yellow'])
    
# 에러의 클래스를 변수 e로 지정
except IndexError as e:
    print('리스트의 범위를 벗어났습니다.')
    print(e)
    
# 위에서 에러가 걸리면 처음 걸린 부분만 실행된다.
except KeyError as e:
    print('입력한 {}는 해당 딕셔너리에 키로 존재하지 않습니다.'.format(e))
    
print('program terminated')
```

### try ~ else

- else는 try 이후 예외가 발생하지 않았을때 사용

```python
try:
	시도할 코드
	
except:
	에러가 발생했을때 실행할 코드
	
else:
	에러가 발생하지 않았을때 실행할 코드
```

### try ~ finally

- finally는 try에서 에러가 발생하든 발생하지 않은 마지막에 실행된다.

```python
try:
	시도할 코드
	
except:
	에러가 발생했을때 실행할 코드
	
else:
	에러가 발생하지 않았을때 실행할 코드
	
finally:
	에러가 발생하든 발생하지 않은 마지막에 실행할 코드

```

### 예외 발생시키기 raise

- 예외를 발생시킬때 `raise`를 사용한다.

```python
"""
1. 정규표현식으로 검사했을때 일치하는 패턴이 없을 경우 발생할 NotMatchedException을 정의
2. 패턴문자열과 소스문자열을 매개변수로 갖는 search_from_source함수를 정의하고, re.search에 소스 문자열을 전달했을때 MatchObject를 찾지 못하면 NotMatchedException을 발생시킴
3. try~except 구문에서 위 함수를 실행해 예외를 발생시킴 (raise NotMatchedException(arg1, arg2))
4. 위 구문에서 else절을 추가해서 예외가 발생하지 않았을 경우 검색결과를 출력
5. 위 구문에 finally절을 추가해서 프로그램이 끝났음을 출력
"""

import re


class NotMatchedException(Exception):
    """
    패턴과 소스를 받아 매치되지 않았음을 알려주는 Exception 클래스
    """
    def __init__(self, pattern_string, source_string):
        self.pattern_string = pattern_string
        self.source_string = source_string
	
	# 스트링을 출력하는 내장함수, 클래스가 호출되면 항상 아래 내용이 출력됨
    def __str__(self):
        return 'Pattern "{}" is not matched in source "{}"'.format(
            self.pattern_string,
            self.source_string,
        )


def search_from_source(pattern_string, source_string):
    # re.search는 찾으면 찾은 문자열을 반환, 못찾으면 None을 반환
    result = re.search(pattern_string, source_string)
    # 결과가 나오면 결과를 반환
    if result:
        return result
    # 결과가 나오지 않으면 예외로 NoMatchedException를 발생시킨다.
    raise NotMatchedException(pattern_string, source_string)

try:
    source = 'Lux, the Lady of ewrwerer'
    pattern = "Man"
    # pattern = r'L\w{3}\b'
    m = search_from_source(pattern, source)
    
    # NotMatchedException 예외가 발생했을 경우
except NotMatchedException as e:
    print(e)
    
    # 에러가 발생하지 않았을 경우
else:
    print('Search result : {}'.format(m.group()))
    
    # 에러가 발생하든 발생하지 않든 아래 내용이 실행
finally:
    print('Program terminated')
```

#### 참고 

##### style guide for python

- 코딩 스타일을 정해놓았음

##### 파이참에서 reformat code 

- 파이참에서 알아서 문서를 정리해줌. 띄어쓰기, 줄 나누기 등...
- 커맨드+알트+L  



# 파일입출력

- 프로그램 실행 중에 파일에 데이터를 저장하거나, 파일의 데이터를 불러오는 작업

## 파일 열기 open()

- 내장함수 open을 사용하고, 파일명에 파일 경로를 적어준다.
- **파일을 열고나면 꼭 닫아야 한다. 닫지 않으면 계속 메모리에 남아있음...**

```python
변수 = open(파일명, 모드)
```

### 모드

- 2개의 문자로 표시한다.

#### 모드의 첫번째 문자

|모드|설명|
|---|---|
|r|읽기|
|w|쓰기 - 이미 파일이 존재한다면 덮어쓴다.|
|x|쓰기 - 이미 파일이 존재한다면 에러 발생|
|a|추가 - 이미 파일이 존재할 경우 기존 데이터 뒤에 추가한다. 파일이 없을 경우 만든다.|

#### 모드의 두번째 문자

|모드|설명|
|---|---|
|t|텍스트 타입. 생략 가능하다.|
|b|이진데이터. 텍스트가 아닌 모든 타입|

## 파일 쓰기 write()

 - 파일에 데이터를 쓴다.

```python
# skills.txt 파일을 쓰기모드로 열고,
f = open('skills.txt', 'wt')

# skills 변수에 저장된 데이터를 skills.txt 파일에 쓴다.
f.write(skills)

# skills.txt 파일을 닫는다.
f.close()
```

#### 써야하는 문자열이 큰 경우, 일정 단위로 나누어 파일에 쓴다.

```python

skills = '''
Illumination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark
Illumination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark
Illumination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark
Illumination
Light Binding
Prismatic Barrier
Lucent Singularity
Final Spark
Illumination
'''

f = open('skills.txt', 'wt')
size = len(skills)
offset = 0
chunk = 5

# 5글자씩 파일에 쓴다.
while True:
	if offset > size:
		break
	f.write(skills[offset:offset+chunk])
	offset += chunk
```
	
## 텍스트파일 전체 읽기 read()

- 파일 전체를 한번에 읽어온다.
- 메모리 사용에 유의해야한다.

```python
f = open('skills.txt', 'rt')
skills = f.read()
f.close()
len(skills)
```

#### 한번에 읽을 최대 문자 수를 제한할 수 있다.

```python
f = open('skills.txt, 'rt')
chunk = 30

# 30글자씩 읽어 skills 변수에 추가한다.
while True:
	part = f.read(chunk)
	
	# 파일을 전부 읽고나면 빈 문자열이 리턴되어 if에서 반복을 중단한다.
	if not part:
		break
	skills += part

f.close()
```

##### 빈 라인 `\n`은 길이가 1이다.

## 이터레이터를 사용한 텍스트파일 읽기

- `readline()`과 같은 결과

```python
skills = ''
f = open('skills.txt', 'rt')

for line in f:
	skills += line
	
f.close()
print(skills)
```

## 텍스트파일을 줄단위 문자열 리스트로 리턴 readline()

- 각 줄에 줄바꿈 문자 `\n`은 `end=''`으로 없앨 수 있다.

```python
f = open('skills.txt', 'rt')
lines = f.readlines()
f.close()
for line in lines:
    print(line, end='')

```

## 자동으로 파일 닫기 with

- 파이썬에서는 해당 파일이 더이상 사용되지 않을때 파일을 자동으로 닫아준다.
- 하지만 메인프로그램이나 오랫동안 동작하는 함수에서 파일을 열고 닫지 않을 경우 문제가 발생한다.
- `with`를 사용하여 내부 구문이 종료되면 파일을 자동으로 파일을 닫아준다

```python
with open('skills.txt', 'wt') as f:
	f.write(skills)
```







  	



	