input_num = int(input('몇 개 출력할까요? : '))


if input_num == 0:
  print('')
elif input_num % 2 == 0:
  print('+-' * int(input_num / 2))
elif input_num % 2 == 1:
  print('+-' * int(input_num / 2) + '+')
    
