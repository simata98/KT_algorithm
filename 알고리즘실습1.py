electric_val = int(input('전기 사용량 : '))

def electricPay(electric_val):
  sum = 0
  if electric_val < 100:
    sum = 410 + (60.7 * electric_val)
  elif electric_val >= 100 and electric_val < 200:
    sum = (60.7 * 100) + 910 + (125.9 * (electric_val - 100))
  elif electric_val >= 200:
    sum = (60.7 * 100) + (125.9 * 100) + 1600 + (187.9 * (electric_val - 200))
    
  return int(sum + sum * 0.1 + sum * 0.037)

print(electricPay(electric_val))
    