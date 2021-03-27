# 6080
n1, n2 = input().split()

n1 = int(n1)
n2 = int(n2)

for i in range(1, n1+1):
  for j in range(1, n2+1):
    print(i, j)


# 6081
data = int(input(), 16)

for i in range(1, 16):
  print('%X*%X=%X' %(data, i, data * i))


# 6082
data = int(input())

for i in range(1, data + 1):
  if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
    print("X", end = ' ')
  else:
    print(i, end= ' ')



# 6083
r, g, b = input().split()
count = 0

r = int(r)
g = int(g)
b = int(b)

for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      count += 1

print(count)