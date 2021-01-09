price = int(input())

coin_types=[50000,10000,5000,1000,500,100,50,10]
result = 0
for i in coin_types:
  result += price // i
  price %= i

print(int(result))