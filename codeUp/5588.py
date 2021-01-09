product = list(map(int, input().split()))
drink = list(map(int, input().split()))

result = []
for i in drink:
  for j in product:
    prev_total = 0
    prev_total += i + j + ((i + j) / 10)
    result.append(prev_total)
    
result.sort()
print(round(result[0], 1))