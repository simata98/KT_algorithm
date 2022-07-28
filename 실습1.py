print('네 정수의 최댓값을 구합니다.')
a = int(input('정수 a 값을 입력하세요 : '))
b = int(input('정수 b 값을 입력하세요 : '))
c = int(input('정수 c 값을 입력하세요 : '))
d = int(input('정수 d 값을 입력하세요 : '))

maximum = a


if b > maximum:
  maximum = b
if c > maximum:
  maximum = c
if d > maximum:
  maximum = d
    
print(f'최댓값은 {maximum} 입니다.')
  