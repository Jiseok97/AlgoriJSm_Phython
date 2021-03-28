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
# 이 코드는 시간 초과
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


# 시간초과를 해결하기 위한 .format (= 문자열 추가)
r, g, b = map(int, input().split())
count = 0


for i in range(r):
  for j in range(g):
    for k in range(b):
      print('{} {} {}'.format(i, j, k))  # {}하나당 하나의 인수가 문자열에 들어감
      count += 1

print(count)


# input()보다 readline()이 한 줄에 여러 개 받을 때 더 빠르다고는 함
# 결과는 2번째가 제일 빨랐음
from sys import stdin

r, g, b = map(int, stdin.readline().split())
count = 0


for i in range(r):
  for j in range(g):
    for k in range(b):
      print('{} {} {}'.format(i, j, k))
      count += 1

print(count)



# 6084
# 시간 25
h, b, c, s = map(int, input().split())

total = h * b * c * s
print(round((total/8/1024/1024), 1),'MB')


# stdin.readline() 사용했을 때, 시간 26
from sys import stdin

h, b, c, s = map(int, stdin.readline().split())

total = h * b * c * s
print(round((total/8/1024/1024), 1),'MB')



# 6085
# 소숫점을 위해 %.2f 사용, round => 불필요한 0은 출력되지 않기 때문
# 무조건 특정 자리 수 까지 출력해야 하는 경우 print의 서식 문자를 이용해 출력하기 !!
w, h, b = map(int, input().split())

total = w * h * b
print('%.2f'%(total/8/1024/1024),'MB')



# 6086
# while문 풀이
data = int(input())
sub = 1
total = 0

while True:
  total += sub
  sub += 1
  if total >= data:
    print(total)
    break



# 6087
data = int(input())

for i in range(1, data+1):
  if i % 3 == 0:
    continue
  print(i, end=' ')



# 6088
a, d, n = map(int, input().split())
count = 1

while True:
  a += d
  count += 1
  if count == n:
    print(a)
    break



# 6089
a, d, n = map(int, input().split())
count = 1

while True:
  a *= d
  count += 1
  if count == n:
    print(a)
    break