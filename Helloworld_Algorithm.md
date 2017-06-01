# Hello World 알고리즘 문제풀이

## Level 1

### x만큼 간격이 있는 n개의 숫자
`number_generator`함수는 x와 n을 입력 받습니다.
2와 5를 입력 받으면 2부터 시작해서 2씩 증가하는 숫자를 5개 가지는 리스트를 만들어서 리턴합니다.  
[2,4,6,8,10]  
4와 3을 입력 받으면 4부터 시작해서 4씩 증가하는 숫자를 3개 가지는 리스트를 만들어서 리턴합니다.  
[4,8,12]  
이를 일반화 하면 x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트를 리턴하도록 함수 number_generator를 완성하면 됩니다.  

```python
def number_generator(x, n):
    return [x for x in range(x, x*n+1, x)]

print(number_generator(3,5))
```
  

### 핸드폰 번호 가리기
별이는 헬로월드텔레콤에서 고지서를 보내는 일을 하고 있습니다. 개인정보 보호를 위해 고객들의 전화번호는 맨 뒷자리 4자리를 제외한 나머지를 `"*"`으로 바꿔야 합니다.  
전화번호를 문자열 s로 입력받는 hide_numbers함수를 완성해 별이를 도와주세요.  
예를들어 s가 `"01033334444"`면 `"*******4444"`를 리턴하고, `"027778888"`인 경우는 `"*****8888"`을 리턴하면 됩니다.  

```python
def hide_numbers(s):
    l = len(s)
    return "*"*(l-4)+s[l-4:]

print("결과 : " + hide_numbers('01033334444'))
```
  
  
### 평균구하기

def average(list):  
함수를 완성해서 매개변수 list의 평균값을 return하도록 만들어 보세요.  
어떠한 크기의 list가 와도 평균값을 구할 수 있어야 합니다.  

```python
def average(list):
    return sum(list)/len(list)

list = [5,3,4, 6, 8, 3, 2] 
print("평균값 : {}".format(average(list)))
```

### 짝수와 홀수

evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.

```python
def evenOrOdd(num):
    if num%2:
        s = "Odd"
    else:
        s = "Even"
    return s

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
```

### 제일 작은 수 제거하기

rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.
예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.

```python
def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist
    
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
```

### 정수제곱근판별하기

nextSqaure함수는 정수 n을 매개변수로 입력받습니다.
n이 임의의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 임의의 정수 x의 제곱이 아니라면 'no'을 리턴하는 함수를 완성하세요.
예를들어 n이 121이라면 이는 정수 11의 제곱이므로 (11+1)의 제곱인 144를 리턴하고, 3이라면 'no'을 리턴하면 됩니다.

```python
def nextSqure(n):
    x = n ** 0.5
    if x == int(x):
        result = (x + 1)**2
    else:
        result = 'no'
    return result

print("결과 : {}".format(nextSqure(121)));
```

### 자릿수더하기

sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
sum_digit함수를 완성해보세요.

```python
def sum_digit(number):
    str1 = str(number)
    str_len = len(str1)
    sums = 0
    for i in range(str_len):
        sums += int(str1[i])
    return sums
    
print("결과 : {}".format(sum_digit(123)));
```

### 스트링을 숫자로 바꾸기

strToInt 메소드는 String형 str을 매개변수로 받습니다.
str을 숫자로 변환한 결과를 반환하도록 strToInt를 완성하세요.
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

```python
def strToInt(str):
    return int(str)

print(strToInt("-1234"));
```

### 수박수박수박수박수박수?

water_melon함수는 정수 n을 매개변수로 입력받습니다.
길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.
예를들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.

```python
def water_melon(n):
    i = n // 2
    j = n % 2
    if j == 0:
        str = '수박'*i
    else:
        str = '수박'*i + '수'
    return str

print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));
```

### 서울에서김서방찾기

findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.
seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요.
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

```python
def findKim(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
        	kimIdx = i
    return "김서방은 {}에 있다".format(kimIdx)

print(findKim(["Queen", "Tod", "Kim"]))
```

### 삼각형출력하기

printTriangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 printTriangle 메소드를 완성하세요
printTriangle이 return하는 String은 개행문자('\n')로 끝나야 합니다.

```python
def printTriangle(num):
    s = ''
    for i in range(num):
        s += '*' * (i+1) + '\n'
    return s

print( printTriangle(3) )
```

### 문자열 다루기 기본

alpha_string46함수는 문자열 s를 매개변수로 입력받습니다.
s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
예를들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다

```python
def alpha_string46(s):
    a = len(s)
    if a == 4 or a == 6:
        try:
            s == int(s)
        except ValueError:
            return False
        else:
            return True
    else:
        return False

print( alpha_string46("a234") )
print( alpha_string46("1234") )
```