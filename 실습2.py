company = str(input('수도 회사를 입력하세요 : '))
usage = int(input('사용량을 입력하세요 : '))

def waterusage(company, usage):
  if company == 'A':
    usage_result = usage * 100
    print(f'요금은 {usage_result} 입니다.')
  elif company == 'B':
    if usage <= 50:
      usage_result = usage * 150
    else:
      usage_result = usage * 75
    print(f'요금은 {usage_result} 입니다.')
    
waterusage(company, usage)