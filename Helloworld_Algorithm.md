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

