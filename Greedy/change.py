# 거스름돈
# 내가 푼 코드

price = 1260
have = [500, 100, 50, 10]
count = 0

for i in range(4):
  if i == 0:
    count += price // have[i]
  else:
    count += price % have[i - 1] // have[i]

print(count)

# 동빈나 코드

n = 1260
count = 0

coin_types = [500,100,50,10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)