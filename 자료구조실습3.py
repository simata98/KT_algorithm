def linear_search(val, num_list):
  num_list.append(val)
  
  for i in range(len(num_list)):
    if num_list[i] == val:
      return num_list[i]
    
  return None

num_list = [2, 5, 1, 3, 9, 6, 7]
search = 5

idx = linear_search(search, num_list)

if (idx == -1):
  print("검색 실패")
else:
  print(f'{search}는 list[{idx}]에 있습니다.')