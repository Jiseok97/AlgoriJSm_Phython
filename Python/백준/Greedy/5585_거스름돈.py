value = int(input())
coin_types = [500, 100, 50, 10, 5, 1]
f_value = 1000 - value
cnt = 0

for i in coin_types:
  cnt += f_value // i
  f_value %= i

print(cnt)