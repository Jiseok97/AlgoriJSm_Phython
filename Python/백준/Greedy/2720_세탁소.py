num = int(input())
prices = []
money_types = [25, 10, 5, 1]

for i in range(num):
  i = int(input())
  prices.append(i)

for j in range(num):
  for k in money_types:
    tot = prices[j] // k
    prices[j] %= k
    print(tot, end=' ')
  print()