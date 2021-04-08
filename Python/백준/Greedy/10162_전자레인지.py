t = int(input())
button_type = [300, 60, 10]
result = []

if t % 10 == 0:
  for i in button_type:
    result.append(t//i)
    t %= i
  
  for j in range(len(result)):
    print(result[j], end=' ')

else:
  print(-1)