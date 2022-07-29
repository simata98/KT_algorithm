print('리스트를 역순으로 출력합니다.')
input_num = int(input('원소 수를 입력하세요 : '))
num_list = []
for i in range(input_num):
  num_list.append(input('x[i]의 값을 입력하세요 : '))
  
print('리스트를 역순으로 출력합니다.')
reversed_list = list(reversed(num_list))
for i in reversed_list:
  print(f'x[0] = {i}')
  