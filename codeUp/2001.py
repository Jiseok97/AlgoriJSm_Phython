p1 = int(input())
p2 = int(input())
p3 = int(input())
d1 = int(input())
d2 = int(input())

pasta = []
drink = []
pasta.append(p1)
pasta.append(p2)
pasta.append(p3)
drink.append(d1)
drink.append(d2)

result = []
for i in drink:
  for j in pasta:
    price = 0
    price = j + i + ((j + i) / 10)
    result.append(price)

result.sort()
print(result[0])