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

### 문자열 내 p와 y의 개수

numPY함수는 대문자와 소문자가 섞여있는 문자열 s를 매개변수로 입력받습니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 리턴하도록 함수를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
예를들어 s가 "pPoooyY"면 True를 리턴하고 "Pyy"라면 False를 리턴합니다.

```python
def numPY(s):
    s_lower = s.lower()
    if s_lower.count('p') == s_lower.count('y'):
        return True
    else:
        return False

print( numPY("pPoooyY") )
print( numPY("Pyy") )
```

### 문자열 내 마음대로 정렬하기

strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.

예를들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로 결과는 ["car", "bed", "sun"]이 됩니다.
strange_sort함수를 완성해 보세요.

```python
def strange_sort(strings, n):
    s = sorted(strings, key = lambda strings: strings[n])
    return s

print( strange_sort(["sun", "bed", "car"], 1) )
```


### 딕셔너리 정렬

딕셔너리는 들어있는 값에 순서가 없지만, 키를 기준으로 정렬하고 싶습니다. 그래서 키와 값을 튜플로 구성하고, 이를 순서대로 리스트에 넣으려고 합니다.
예를들어 {"김철수":78, "이하나":97, "정진원":88}이 있다면 각각의 키와 값을  

("김철수", 78)  
("이하나", 97)  
("정진원", 88)  
과 같이 튜플로 분리하고 키를 기준으로 정렬해서 다음과 같은 리스트를 만들면 됩니다.  
[ ("김철수", 78), ("이하나", 97), ("정진원", 88) ]

다음 sort_dictionary 함수를 완성해 보세요.

```python
def sort_dictionary(dic):
    t = [(i, dic[i]) for i in dic]
    return sorted(t)

print( sort_dictionary( {"김철수":78, "이하나":97, "정진원":88} ))
```

### 같은 숫자는 싫어

no_continuous함수는 스트링 s를 매개변수로 입력받습니다.  

s의 글자들의 순서를 유지하면서, 글자들 중 연속적으로 나타나는 아이템은 제거된 배열(파이썬은 list)을 리턴하도록 함수를 완성하세요.  
예를들어 다음과 같이 동작하면 됩니다.  

s가 '133303'이라면 ['1', '3', '0', '3']를 리턴  
s가 '47330'이라면 [4, 7, 3, 0]을 리턴  

```python
def no_continuous(s):
    l = [s[0]]
    i = 0    
    while i < (len(s)-1):
        if s[i] != s[i+1]:
            l.append(s[i+1])
        else:
            pass
        i += 1
    return l
    
print( no_continuous( "133303" ))
```

### 가운데 글자 가져오기

getMiddle메소드는 하나의 단어를 입력 받습니다. 단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요. 단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.  
예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.  

```python
def string_middle(str):
    lenth = len(str)
    if lenth % 2 == 0:
        return str[lenth//2-1]+str[lenth//2]
    else:
        return str[lenth//2]

print(string_middle("test"))
```

### 행렬의 덧셈

행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬을 입력받는 sumMatrix 함수를 완성하여 행렬 덧셈의 결과를 반환해 주세요.

예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.(어떠한 행렬에도 대응하는 함수를 완성해주세요.)

```python
def sumMatrix(A,B):
    answer = []
    for i in range(0, len(A)):
        answer_pre = []
        for j in range(0, len(B)):
            answer_pre.append(A[i][j]+B[i][j])
        answer.append(answer_pre)
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
```

### 피보나치 수

피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 예를 들어 n = 3이라면 2를 반환해주면 됩니다.

```python

```


### 약수의 합

어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sumDivisor 함수를 완성해 보세요.   
예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.

```python
def sumDivisor(num):
    answer = []
    for i in range(1, num+1):
        if num % i == 0:
            answer.append(i)
    return sum(answer)

print(sumDivisor(12))
```

### 하샤드수

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.

Harshad함수는 양의 정수 n을 매개변수로 입력받습니다. 이 n이 하샤드수인지 아닌지 판단하는 함수를 완성하세요.
예를들어 n이 10, 12, 18이면 True를 리턴 11, 13이면 False를 리턴하면 됩니다.

```python
def Harshad(n):
    str_n = str(n)
    l = len(str_n)
    sum = 0
    i = 0
    while i < l:
        sum += int(str_n[i])
        i += 1
    return True if n % sum == 0 else False

print(Harshad(12))
```


### JadenCase문자열 만들기

Jaden_Case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 "3people unFollowed me for the last week"라면 "3people Unfollowed Me For The Last Week"를 리턴하면 됩니다.


```python
def Jaden_Case(s):
    l = s.split()
    sl = []
    for i in range(0, len(l)):
        sl.append(l[i].capitalize())
    s = ' '.join(sl)
    return s  

print(Jaden_Case("3people unFollowed me for the last week"))
```

```python
def Jaden_Case(s):
    return s.title()  
    
print(Jaden_Case("3people unFollowed me for the last week"))
```

### 자연수를 뒤집어 리스트로 만들기

digit_reverse함수는 양의 정수 n을 매개변수로 입력받습니다.
n을 뒤집어 숫자 하나하나를 list로 표현해주세요
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴하면 됩니다.


```python
def digit_reverse(n):
    lenth = len(str(n)) - 1
    n_list = []
    while lenth >= 0:
        n_list.append(int(str(n)[lenth]))
        lenth -= 1
    return n_list

print("결과 : {}".format(digit_reverse(12345)));
```

