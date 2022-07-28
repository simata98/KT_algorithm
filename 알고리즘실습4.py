input_num = int(input('숫자를 입력하세요 : '))
li = []

for i in range(1, input_num+1):
  for j in range(2, 7):
    if (i ** j) == input_num:
      li.append((i, j))

if len(li) == 0:
  print('결과 없음')
else:
  print(li)