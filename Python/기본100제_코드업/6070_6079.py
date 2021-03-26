# 6070
data = int(input())

if data // 3 == 1:
  print("spring")

elif data // 3 == 2:
  print("summer")

elif data // 3 == 3:
  print("fall")

else:
  print("winter")



# 6071
n = 1

while n != 0:
  n = int(input())
  if n != 0:
    print(n)


# 6072
data = int(input())

while data != 0:
  print(data)
  data -= 1



# 6073
data = int(input())

while data != 0:
  data -= 1
  print(data)



# 6074
data = ord(input())
compare = ord('a')

while compare <= data:
  print(chr(compare), end=' ')
  compare += 1



# 6075
data = int(input())
n = 0

while n <= data:
  print(n)
  n += 1



# 6076
data = int(input())

for i in range(data + 1):
  print(i)




# 6077
data = int(input())
total = 0

for i in range(data + 1):
  if i % 2 == 0:
    total += i

print(total)



# 6078
while True:
  data = input()
  print(data)
  if data == 'q':
    break


# 6079
data = int(input())
total = 0

for i in range(1000):
  total += i
  if total >= data:
    print(i)
    break