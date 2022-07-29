N = int(input())
store_list = set(map(int, input().split()))

M = int(input())
customer_list = list(map(int, input().split()))

for i in customer_list:
  if i in store_list:
    print('yes', end=' ')
  else:
    print('no', end=' ')
  