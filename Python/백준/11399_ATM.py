cnt = int(input())
type = list(map(int, input().split()))
sum = 0
total = 0

type.sort()

for i in type:
  sum += i
  total += sum

print(total)