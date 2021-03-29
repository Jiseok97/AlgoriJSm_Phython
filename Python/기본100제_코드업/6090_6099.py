# 6090
a, m, d, n = map(int, input().split())
total = a

for _ in range(1, n):
  total *= m
  total += d

print(total)



# 6091
a, b, c = map(int, input().split())
day = 1

# a, b, c가 day를 나누었을 때, 나머지가 안남을 때가 최소 공배수와 같은 의미
while day % a != 0 or day % b != 0 or day % c != 0:
  day +=1

print(day)



# 6092
ct = int(input())
students = input().split() 

for i in range(ct):
  students[i] = int(students[i])

# students 번호에 맞는 횟수를 세줄 빈 list 생성
count = []
for i in range(24):
  count.append(0)

# 해당 학생 n번호가 불릴 시 count list의 n번 + 1
for i in range(ct):
  count[students[i]] += 1

# 1번부터 23번까지 총 불린 횟수 출력
for i in range(1, 24):
  print(count[i], end=' ')



# 6093
# 배열의 순서 바꾸기
n = int(input())
number = input().split()

for i in range(n):
  number[i] = int(number[i])

for i in range(n-1, -1, -1):
  print(number[i], end=' ')



# 6094
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0])