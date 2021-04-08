S = input().split('-')
tResult = []

for i in S:
  cnt = 0
  k = i.split('+')
  for j in k:
    cnt += int(j)
  tResult.append(cnt)

result = tResult[0]
for i in range(1, len(tResult)):
  result -= tResult[i]
  
print(result)