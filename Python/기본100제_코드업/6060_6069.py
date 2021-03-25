# 6060
a, b = input().split()
print(int(a) & int(b))


# 6061
a, b = input().split()
print(int(a) | int(b))


# 6062
a, b = input().split()
print(int(a) ^ int(b))


# 6063
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a >= b) else b)  # 삼항 연산자
print(c)


# 6064
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

# a랑 b를 먼저 비교한 후, c와 대조해서 false => a or b 중 하나,
# true => c
d = (a if a < b else b) if ((a if a < b else b) < c) else c
print(d)


# 6065
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
  print(a)

if b % 2 == 0:
  print(b)

if c % 2 == 0:
  print(c)


# 6066
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a % 2 == 0:
  print("even")
else:
  print("odd")

if b % 2 == 0:
  print("even")
else:
  print("odd")

if c % 2 == 0:
  print("even")
else: 
  print("odd")


# 6067
data = int(input())

if data < 0:
  if data % 2 == 0:
    print('A')
  else:
    print('B')

else:
  if data % 2 == 0:
    print('C')
  else:
    print('D')


# 6068
data = int(input())

if data >= 90 and data <= 100:
  print('A')

elif data >= 70 and data < 90:
  print('B')

elif data >= 40 and data < 70:
  print('C')

else:
  print('D')


# 6069
data = input()

if data == 'A':
  print("best!!!")

elif data == 'B':
  print("good!!")

elif data == 'C':
  print("run!")

elif data == 'D':
  print("slowly~")

else:
  print("what?")