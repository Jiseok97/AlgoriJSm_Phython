cnt, total = map(int, input().split())
coin_type = []
check = 0
for i in range(cnt):
  i = int(input())
  coin_type.append(i)

coin_type.sort(reverse=True)

for i in coin_type:
  check += total // i
  total %= i

print(check)