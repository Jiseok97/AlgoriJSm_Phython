lst = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(lst)):
  min_index = i  # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(lst)):
    if lst[min_index] > lst[j]:
      min_index = j
    
  # 가장 앞쪽 원소랑 가장 작은 원소의 위치를 바꿔줌
  lst[i], lst[min_index] = lst[min_index], lst[i]  # Swap

print(lst)